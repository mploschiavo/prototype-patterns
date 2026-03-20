#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ $# -lt 2 ]]; then
  echo "Usage: ./scripts/run-client-local.sh <python|nodejs|java|csharp> <project> [producer|consumer]" >&2
  exit 1
fi

language="$1"
project="$2"
shift 2

project_dir="$ROOT_DIR/$language/$project"
runner="$project_dir/docker/run.sh"

if [[ ! -x "$runner" ]]; then
  echo "Missing runner: $runner" >&2
  exit 2
fi

exec "$runner" "$@"
