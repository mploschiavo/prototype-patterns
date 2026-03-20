#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/csharp-kafka-single:latest"
MODE="${1:-producer}"
if [[ "$MODE" != "producer" && "$MODE" != "consumer" ]]; then
  echo "Usage: ./docker/run.sh [producer|consumer]" >&2
  exit 1
fi
docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
docker_args=(--rm -e KAFKA_CLIENT_MODE="$MODE")
docker_args+=(-e KAFKA_BOOTSTRAP_SERVERS="${KAFKA_BOOTSTRAP_SERVERS:-localhost:9092}")
docker_args+=(-e KAFKA_TOPIC="${KAFKA_TOPIC:-prototype-topic}")
docker run "${docker_args[@]}" "$IMAGE"
