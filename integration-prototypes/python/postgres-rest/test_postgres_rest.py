from __future__ import annotations

import unittest

from app import fetch_item


class _FakeCursor:
    def __init__(self, row):
        self._row = row

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        _ = (exc_type, exc, tb)

    def execute(self, query, params):
        _ = (query, params)

    def fetchone(self):
        return self._row


class _FakeConnection:
    def __init__(self, row):
        self._row = row

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        _ = (exc_type, exc, tb)

    def cursor(self):
        return _FakeCursor(self._row)


class PostgresRestTests(unittest.TestCase):
    def test_fetch_item_found(self) -> None:
        def fake_connect(_dsn: str):
            return _FakeConnection((1, "alpha", "seed row alpha"))

        item = fetch_item(1, connect_fn=fake_connect)
        self.assertEqual(item, {"id": 1, "name": "alpha", "description": "seed row alpha"})

    def test_fetch_item_not_found(self) -> None:
        def fake_connect(_dsn: str):
            return _FakeConnection(None)

        item = fetch_item(999, connect_fn=fake_connect)
        self.assertIsNone(item)


if __name__ == "__main__":
    unittest.main()
