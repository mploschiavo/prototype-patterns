#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ $# -lt 2 ]]; then
  echo "Usage: ./scripts/deploy-client-microk8s.sh <python|nodejs|java|csharp> <project> [apply|delete]" >&2
  exit 1
fi

language="$1"
project="$2"
action="${3:-apply}"

project_dir="$ROOT_DIR/$language/$project"
runner="$project_dir/k8s/run.sh"

if [[ ! -x "$runner" ]]; then
  echo "Missing runner: $runner" >&2
  exit 2
fi

exec "$runner" "$action"
