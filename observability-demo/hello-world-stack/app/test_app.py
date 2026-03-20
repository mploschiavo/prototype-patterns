from __future__ import annotations

import os
import tempfile
import unittest

os.environ.setdefault("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "http://localhost:4318/v1/traces")

from app import create_app  # noqa: E402


class AppTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        os.environ["APP_LOG_DIR"] = self.temp_dir.name
        self.app = create_app().test_client()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_root(self) -> None:
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("hello observability", response.get_data(as_text=True))

    def test_metrics(self) -> None:
        self.app.get("/")
        response = self.app.get("/metrics")
        self.assertEqual(response.status_code, 200)
        self.assertIn("demo_requests_total", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
