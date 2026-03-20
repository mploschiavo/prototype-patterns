from __future__ import annotations

import unittest

from app import fetch_value


class _FakeRedis:
    def __init__(self, values):
        self._values = values

    def get(self, key):
        return self._values.get(key)


class RedisSingleRestTests(unittest.TestCase):
    def test_fetch_value_json(self) -> None:
        def fake_factory(_url: str):
            return _FakeRedis({"demo:key": '{"id":1,"value":"hello redis single"}'})

        value = fetch_value(client_factory=fake_factory)
        self.assertEqual(value, {"id": 1, "value": "hello redis single"})

    def test_fetch_value_missing(self) -> None:
        def fake_factory(_url: str):
            return _FakeRedis({})

        value = fetch_value(client_factory=fake_factory)
        self.assertIsNone(value)


if __name__ == "__main__":
    unittest.main()
