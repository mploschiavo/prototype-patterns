from __future__ import annotations

import unittest

from producer import build_message, send_message
from consumer import consume_once


class _FakeFuture:
    def get(self, timeout: int) -> None:
        _ = timeout


class _FakeProducer:
    def __init__(self, *args, **kwargs) -> None:
        self.sent: list[tuple[str, object]] = []

    def send(self, topic: str, payload: object) -> _FakeFuture:
        self.sent.append((topic, payload))
        return _FakeFuture()

    def flush(self) -> None:
        return

    def close(self) -> None:
        return


class _FakeRecord:
    def __init__(self, value: object) -> None:
        self.value = value


class _FakeConsumer:
    def __init__(self, *_args, **_kwargs) -> None:
        self._records = [_FakeRecord({"id": "1", "text": "hello-ha"})]

    def __iter__(self):
        return iter(self._records)

    def close(self) -> None:
        return


class KafkaHaTests(unittest.TestCase):
    def test_build_message(self) -> None:
        self.assertEqual(build_message("a", "b"), {"id": "a", "text": "b"})

    def test_send_message(self) -> None:
        send_message("topic-ha", {"id": "1"}, producer_factory=_FakeProducer)

    def test_consume_once(self) -> None:
        value = consume_once("topic-ha", consumer_factory=_FakeConsumer)
        self.assertEqual(value, {"id": "1", "text": "hello-ha"})


if __name__ == "__main__":
    unittest.main()
