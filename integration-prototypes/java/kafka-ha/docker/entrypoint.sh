#!/usr/bin/env sh
set -eu
mode="${KAFKA_CLIENT_MODE:-producer}"
if [ "$mode" = "consumer" ]; then
  exec java -cp "/app/classes:/app/dependency/*" "$JAVA_CONSUMER_CLASS"
fi
exec java -cp "/app/classes:/app/dependency/*" "$JAVA_PRODUCER_CLASS"
