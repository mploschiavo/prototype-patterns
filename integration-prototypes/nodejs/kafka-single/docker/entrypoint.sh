#!/usr/bin/env sh
set -eu
mode="${KAFKA_CLIENT_MODE:-producer}"
if [ "$mode" = "consumer" ]; then
  exec node consumer.js
fi
exec node producer.js
