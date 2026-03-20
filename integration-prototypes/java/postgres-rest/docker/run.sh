#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/java-postgres-rest:latest"
PORT="${PORT:-8080}"
docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
docker_args=(--rm -p "$PORT:$PORT" -e PORT="$PORT")
docker_args+=(-e POSTGRES_JDBC_URL="${POSTGRES_JDBC_URL:-jdbc:postgresql://localhost:5432/prototype_db}")
docker_args+=(-e POSTGRES_USER="${POSTGRES_USER:-prototype_user}")
docker_args+=(-e POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-prototype_pass}")
docker run "${docker_args[@]}" "$IMAGE"
