"""Python REST prototype for Redis single-node value retrieval."""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from typing import Any, Callable


REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")


def fetch_value(key: str = "demo:key", redis_url: str = REDIS_URL, client_factory: Callable[..., Any] | None = None) -> Any:
    factory = client_factory
    if factory is None:
        from redis import Redis

        client = Redis.from_url(redis_url, decode_responses=True)
    else:
        client = factory(redis_url)

    raw = client.get(key)
    if raw is None:
        return None

    try:
        return json.loads(raw)
    except (TypeError, json.JSONDecodeError):
        return raw


class RedisSingleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/value":
            self._send(404, {"error": "not found"})
            return

        key = parse_qs(parsed.query).get("key", ["demo:key"])[0]
        value = fetch_value(key=key)
        if value is None:
            self._send(404, {"error": "key not found"})
            return

        self._send(200, {"key": key, "value": value})

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
    return HTTPServer(("0.0.0.0", port), RedisSingleHandler)


def main() -> None:
    port = int(os.getenv("PORT", "8080"))
    server = create_server(port)
    print(f"redis-single-rest listening on :{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
