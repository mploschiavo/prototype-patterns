from __future__ import annotations

import unittest

from app import fetch_value


class _FakeResponse:
    def __init__(self, status_code: int, payload: dict):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        return self._payload


class OpenSearchSingleRestTests(unittest.TestCase):
    def test_fetch_value_found(self) -> None:
        def fake_get(_url: str, _index: str, _doc_id: str):
            return _FakeResponse(200, {"found": True, "_source": {"message": "hello opensearch single"}})

        value = fetch_value(get_fn=fake_get)
        self.assertEqual(value, "hello opensearch single")

    def test_fetch_value_not_found(self) -> None:
        def fake_get(_url: str, _index: str, _doc_id: str):
            return _FakeResponse(200, {"found": False})

        value = fetch_value(get_fn=fake_get)
        self.assertIsNone(value)


if __name__ == "__main__":
    unittest.main()
