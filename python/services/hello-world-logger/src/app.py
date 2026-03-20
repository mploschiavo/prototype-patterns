"""Simple Python REST service returning hello world with logger."""

from __future__ import annotations

import logging
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

logger = logging.getLogger("hello-world-logger")


def build_message(active_logger: logging.Logger | None = None) -> str:
    current_logger = active_logger or logger
    current_logger.info("Handling hello-world-logger request")
    return "hello world with logger"


class HelloWorldLoggerHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 (stdlib method name)
        if self.path != "/":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"not found")
            return

        message = build_message().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003
        return


def create_server(port: int) -> HTTPServer:
    return HTTPServer(("0.0.0.0", port), HelloWorldLoggerHandler)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")
    port = int(os.getenv("PORT", "8080"))
    server = create_server(port)
    print(f"Python hello-world-logger listening on :{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
