#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/csharp-postgres-rest:latest"
PORT="${PORT:-8080}"
docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
docker_args=(--rm -p "$PORT:$PORT" -e PORT="$PORT")
docker_args+=(-e POSTGRES_CONNECTION_STRING="${POSTGRES_CONNECTION_STRING:-Host=localhost;Port=5432;Username=prototype_user;Password=prototype_pass;Database=prototype_db}")
docker run "${docker_args[@]}" "$IMAGE"
