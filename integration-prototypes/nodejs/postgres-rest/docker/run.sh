#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/nodejs-postgres-rest:latest"
PORT="${PORT:-8080}"
docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
docker_args=(--rm -p "$PORT:$PORT" -e PORT="$PORT")
docker_args+=(-e PG_CONNECTION_STRING="${PG_CONNECTION_STRING:-postgresql://prototype_user:prototype_pass@localhost:5432/prototype_db}")
docker run "${docker_args[@]}" "$IMAGE"
