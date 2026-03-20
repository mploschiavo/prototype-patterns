from __future__ import annotations

import logging
import threading
import unittest
import urllib.request

from src.app import build_message, create_server


class CaptureHandler(logging.Handler):
    def __init__(self) -> None:
        super().__init__()
        self.messages: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.messages.append(record.getMessage())


class HelloWorldLoggerTests(unittest.TestCase):
    def test_build_message(self) -> None:
        self.assertEqual(build_message(), "hello world with logger")

    def test_build_message_logs(self) -> None:
        test_logger = logging.getLogger("hello-world-logger-test")
        capture = CaptureHandler()
        test_logger.addHandler(capture)
        test_logger.setLevel(logging.INFO)

        try:
            build_message(test_logger)
            self.assertTrue(any("Handling hello-world-logger request" in msg for msg in capture.messages))
        finally:
            test_logger.removeHandler(capture)

    def test_http_response(self) -> None:
        server = create_server(0)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()

        try:
            url = f"http://127.0.0.1:{server.server_port}/"
            with urllib.request.urlopen(url, timeout=2) as response:
                self.assertEqual(response.status, 200)
                body = response.read().decode("utf-8")
            self.assertEqual(body, "hello world with logger")
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
