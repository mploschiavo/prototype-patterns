#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/python-redis-ha-rest:latest"
PORT="${PORT:-8080}"
docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
docker_args=(--rm -p "$PORT:$PORT" -e PORT="$PORT")
docker_args+=(-e REDIS_CLUSTER_NODES="${REDIS_CLUSTER_NODES:-localhost:6379,localhost:6380,localhost:6381}")
docker run "${docker_args[@]}" "$IMAGE"
