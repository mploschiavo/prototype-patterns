#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/csharp-opensearch-single-rest:latest"
PORT="${PORT:-8080}"
docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
docker_args=(--rm -p "$PORT:$PORT" -e PORT="$PORT")
docker_args+=(-e OPENSEARCH_URL="${OPENSEARCH_URL:-http://localhost:9200}")
docker run "${docker_args[@]}" "$IMAGE"
