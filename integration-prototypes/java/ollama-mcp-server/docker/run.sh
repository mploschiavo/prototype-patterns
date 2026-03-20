#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/java-ollama-mcp-server:latest"
PORT="${PORT:-8090}"
docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
docker_args=(--rm -p "$PORT:$PORT" -e PORT="$PORT")
docker_args+=(-e OLLAMA_URL="${OLLAMA_URL:-http://localhost:11434}")
docker_args+=(-e OLLAMA_MODEL="${OLLAMA_MODEL:-tinyllama}")
docker run "${docker_args[@]}" "$IMAGE"
