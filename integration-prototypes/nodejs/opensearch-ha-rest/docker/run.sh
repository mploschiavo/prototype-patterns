#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/nodejs-opensearch-ha-rest:latest"
PORT="${PORT:-8080}"
docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
docker_args=(--rm -p "$PORT:$PORT" -e PORT="$PORT")
docker_args+=(-e OPENSEARCH_NODES="${OPENSEARCH_NODES:-http://localhost:9200,http://localhost:9201,http://localhost:9202}")
docker run "${docker_args[@]}" "$IMAGE"
