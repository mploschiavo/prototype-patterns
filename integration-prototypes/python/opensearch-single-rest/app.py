"""Python REST prototype for OpenSearch single-node value retrieval."""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Callable
from urllib.parse import parse_qs, urlparse


OPENSEARCH_URL = os.getenv("OPENSEARCH_URL", "http://localhost:9200")


def fetch_value(
    index: str = "prototype_docs",
    doc_id: str = "1",
    opensearch_url: str = OPENSEARCH_URL,
    get_fn: Callable[..., Any] | None = None,
) -> str | None:
    if get_fn is None:
        import requests

        response = requests.get(f"{opensearch_url}/{index}/_doc/{doc_id}", timeout=5)
    else:
        response = get_fn(opensearch_url, index, doc_id)

    if response.status_code == 404:
        return None

    payload = response.json()
    if payload.get("found") is False:
        return None

    source = payload.get("_source", {})
    return source.get("message")


class OpenSearchSingleHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/value":
            self._send(404, {"error": "not found"})
            return

        query = parse_qs(parsed.query)
        index = query.get("index", ["prototype_docs"])[0]
        doc_id = query.get("id", ["1"])[0]

        value = fetch_value(index=index, doc_id=doc_id)
        if value is None:
            self._send(404, {"error": "document not found"})
            return

        self._send(200, {"index": index, "id": doc_id, "value": value})

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
    return HTTPServer(("0.0.0.0", port), OpenSearchSingleHandler)


def main() -> None:
    port = int(os.getenv("PORT", "8080"))
    server = create_server(port)
    print(f"opensearch-single-rest listening on :{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
