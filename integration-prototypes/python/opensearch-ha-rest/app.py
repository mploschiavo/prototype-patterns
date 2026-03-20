"""Python REST prototype for OpenSearch HA value retrieval."""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Callable
from urllib.parse import parse_qs, urlparse


OPENSEARCH_NODES = os.getenv("OPENSEARCH_NODES", "http://localhost:9200,http://localhost:9201,http://localhost:9202")


def parse_nodes(nodes: str) -> list[str]:
    return [node.strip() for node in nodes.split(",") if node.strip()]


def fetch_value(
    index: str = "prototype_docs",
    doc_id: str = "1",
    nodes: str = OPENSEARCH_NODES,
    get_fn: Callable[..., Any] | None = None,
) -> str | None:
    if get_fn is None:
        import requests

        def _default_get(node_url: str, in_index: str, in_doc_id: str) -> Any:
            return requests.get(f"{node_url}/{in_index}/_doc/{in_doc_id}", timeout=5)

        getter = _default_get
    else:
        getter = get_fn

    for node in parse_nodes(nodes):
        try:
            response = getter(node, index, doc_id)
            if response.status_code == 404:
                return None

            payload = response.json()
            if payload.get("found") is False:
                return None

            source = payload.get("_source", {})
            return source.get("message")
        except Exception:
            continue

    raise RuntimeError("all OpenSearch nodes unreachable")


class OpenSearchHaHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/value":
            self._send(404, {"error": "not found"})
            return

        query = parse_qs(parsed.query)
        index = query.get("index", ["prototype_docs"])[0]
        doc_id = query.get("id", ["1"])[0]

        try:
            value = fetch_value(index=index, doc_id=doc_id)
        except RuntimeError:
            self._send(503, {"error": "opensearch unavailable"})
            return

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
    return HTTPServer(("0.0.0.0", port), OpenSearchHaHandler)


def main() -> None:
    port = int(os.getenv("PORT", "8080"))
    server = create_server(port)
    print(f"opensearch-ha-rest listening on :{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
