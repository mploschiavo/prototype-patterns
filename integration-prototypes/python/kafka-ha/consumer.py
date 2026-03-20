"""Kafka HA consumer prototype."""

from __future__ import annotations

import json
import os
from typing import Any, Callable

try:
    from kafka import KafkaConsumer
except ImportError:  # pragma: no cover
    KafkaConsumer = None  # type: ignore[assignment]


def consume_once(
    topic: str,
    bootstrap_servers: str | None = None,
    group_id: str = "python-kafka-ha-consumer",
    consumer_factory: Callable[..., Any] | None = None,
) -> dict[str, Any] | None:
    servers = bootstrap_servers or os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092,localhost:9094,localhost:9096")
    factory = consumer_factory or KafkaConsumer
    if factory is None:
        raise RuntimeError("kafka-python is not installed")

    consumer = factory(
        topic,
        bootstrap_servers=servers,
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        group_id=group_id,
        value_deserializer=lambda value: json.loads(value.decode("utf-8")),
    )
    try:
        for record in consumer:
            return record.value
        return None
    finally:
        consumer.close()


def main() -> None:
    topic = os.getenv("KAFKA_TOPIC", "prototype-topic-ha")
    message = consume_once(topic=topic)
    print(f"received from {topic}: {message}")


if __name__ == "__main__":
    main()
