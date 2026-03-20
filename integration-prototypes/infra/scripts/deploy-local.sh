#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <scenario> [up|down]"
  exit 1
fi

SCENARIO="$1"
ACTION="${2:-up}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COMPOSE_FILE="$ROOT_DIR/$SCENARIO/docker-compose.yml"

if [[ ! -f "$COMPOSE_FILE" ]]; then
  echo "Unknown scenario: $SCENARIO"
  exit 1
fi

if [[ "$ACTION" == "down" ]]; then
  docker compose -f "$COMPOSE_FILE" down
else
  docker compose -f "$COMPOSE_FILE" up -d
fi
