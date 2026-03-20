"""Python REST prototype for Postgres record retrieval."""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from typing import Any, Callable


DEFAULT_DSN = os.getenv(
    "POSTGRES_DSN",
    "postgresql://prototype_user:prototype_pass@localhost:5432/prototype_db",
)


def fetch_item(item_id: int, dsn: str = DEFAULT_DSN, connect_fn: Callable[..., Any] | None = None) -> dict[str, Any] | None:
    connector = connect_fn
    if connector is None:
        import psycopg

        connector = psycopg.connect

    with connector(dsn) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, description FROM demo_items WHERE id = %s",
                (item_id,),
            )
            row = cursor.fetchone()

    if row is None:
        return None

    return {"id": row[0], "name": row[1], "description": row[2]}


class PostgresHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/item":
            self._send(404, {"error": "not found"})
            return

        item_id = int(parse_qs(parsed.query).get("id", ["1"])[0])
        payload = fetch_item(item_id)
        if payload is None:
            self._send(404, {"error": "item not found"})
            return

        self._send(200, payload)

    def _send(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args: object) -> None:
        _ = (fmt, args)


def create_server(port: int) -> HTTPServer:
    return HTTPServer(("0.0.0.0", port), PostgresHandler)


def main() -> None:
    port = int(os.getenv("PORT", "8080"))
    server = create_server(port)
    print(f"postgres-rest listening on :{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
