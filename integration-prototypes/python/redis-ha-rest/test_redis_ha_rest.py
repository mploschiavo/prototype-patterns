from __future__ import annotations

import unittest

from app import _parse_nodes, fetch_value


class _FakeRedisCluster:
    def __init__(self, values):
        self._values = values

    def get(self, key):
        return self._values.get(key)


class RedisHaRestTests(unittest.TestCase):
    def test_parse_nodes(self) -> None:
        parsed = _parse_nodes("localhost:6379,localhost:6380")
        self.assertEqual(parsed, [{"host": "localhost", "port": 6379}, {"host": "localhost", "port": 6380}])

    def test_fetch_value_json(self) -> None:
        def fake_factory(_nodes: str):
            return _FakeRedisCluster({"demo:key": '{"id":1,"value":"hello redis ha"}'})

        value = fetch_value(client_factory=fake_factory)
        self.assertEqual(value, {"id": 1, "value": "hello redis ha"})


if __name__ == "__main__":
    unittest.main()
