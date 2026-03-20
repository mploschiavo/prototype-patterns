from __future__ import annotations

import threading
import unittest
import urllib.request

from src.app import build_message, create_server


class HelloWorldTests(unittest.TestCase):
    def test_build_message(self) -> None:
        self.assertEqual(build_message(), "hello world")

    def test_http_response(self) -> None:
        server = create_server(0)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()

        try:
            url = f"http://127.0.0.1:{server.server_port}/"
            with urllib.request.urlopen(url, timeout=2) as response:
                self.assertEqual(response.status, 200)
                body = response.read().decode("utf-8")
            self.assertEqual(body, "hello world")
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
