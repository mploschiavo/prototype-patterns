"""Kafka HA producer prototype."""

from __future__ import annotations

import json
import os
from typing import Any, Callable

try:
    from kafka import KafkaProducer
except ImportError:  # pragma: no cover
    KafkaProducer = None  # type: ignore[assignment]


def build_message(message_id: str, text: str) -> dict[str, str]:
    return {"id": message_id, "text": text}


def send_message(
    topic: str,
    message: dict[str, Any],
    bootstrap_servers: str | None = None,
    producer_factory: Callable[..., Any] | None = None,
) -> None:
    servers = bootstrap_servers or os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092,localhost:9094,localhost:9096")
    factory = producer_factory or KafkaProducer
    if factory is None:
        raise RuntimeError("kafka-python is not installed")

    producer = factory(
        bootstrap_servers=servers,
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    )
    producer.send(topic, message).get(timeout=10)
    producer.flush()
    producer.close()


def main() -> None:
    topic = os.getenv("KAFKA_TOPIC", "prototype-topic-ha")
    payload = build_message("1", "hello from python kafka ha producer")
    send_message(topic=topic, message=payload)
    print(f"sent message to {topic}: {payload}")


if __name__ == "__main__":
    main()
