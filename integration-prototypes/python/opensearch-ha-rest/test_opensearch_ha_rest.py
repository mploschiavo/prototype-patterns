from __future__ import annotations

import unittest

from app import fetch_value, parse_nodes


class _FakeResponse:
    def __init__(self, status_code: int, payload: dict):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        return self._payload


class OpenSearchHaRestTests(unittest.TestCase):
    def test_parse_nodes(self) -> None:
        parsed = parse_nodes("http://localhost:9200,http://localhost:9201,http://localhost:9202")
        self.assertEqual(parsed, ["http://localhost:9200", "http://localhost:9201", "http://localhost:9202"])

    def test_fetch_value_failover(self) -> None:
        calls = []

        def fake_get(node: str, _index: str, _doc_id: str):
            calls.append(node)
            if node.endswith(":9200"):
                raise RuntimeError("node unavailable")
            return _FakeResponse(200, {"found": True, "_source": {"message": "hello opensearch ha"}})

        value = fetch_value(nodes="http://localhost:9200,http://localhost:9201", get_fn=fake_get)
        self.assertEqual(value, "hello opensearch ha")
        self.assertEqual(calls, ["http://localhost:9200", "http://localhost:9201"])


if __name__ == "__main__":
    unittest.main()
