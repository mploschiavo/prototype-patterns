#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="localhost:32000/observability-demo-app:latest"

docker build -t "$IMAGE" -f "$ROOT_DIR/app/Dockerfile" "$ROOT_DIR"
docker push "$IMAGE"
