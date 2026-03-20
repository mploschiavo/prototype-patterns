#!/usr/bin/env sh
set -eu
mode="${KAFKA_CLIENT_MODE:-producer}"
if [ "$mode" = "consumer" ]; then
  exec python consumer.py
fi
exec python producer.py
