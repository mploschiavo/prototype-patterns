"""Simple Python REST service returning hello world."""

from __future__ import annotations

import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def build_message() -> str:
    return "hello world"


class HelloWorldHandler(BaseHTTPRequestHandler):
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
        # Keep example output clean for academic walkthroughs.
        return


def create_server(port: int) -> HTTPServer:
    return HTTPServer(("0.0.0.0", port), HelloWorldHandler)


def main() -> None:
    port = int(os.getenv("PORT", "8080"))
    server = create_server(port)
    print(f"Python hello-world listening on :{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
