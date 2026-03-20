#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/csharp-redis-ha-rest:latest"
PORT="${PORT:-8080}"
docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
docker_args=(--rm -p "$PORT:$PORT" -e PORT="$PORT")
docker_args+=(-e REDIS_CLUSTER_ENDPOINTS="${REDIS_CLUSTER_ENDPOINTS:-localhost:6379,localhost:6380,localhost:6381}")
docker run "${docker_args[@]}" "$IMAGE"
