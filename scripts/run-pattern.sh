#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  echo "Usage:"
  echo "  ./scripts/run-pattern.sh <python|nodejs|java|csharp> --list"
  echo "  ./scripts/run-pattern.sh <python|nodejs|java|csharp> --pattern <pattern-id>"
  echo "  ./scripts/run-pattern.sh <python|nodejs|java|csharp> --all"
}

if [[ $# -lt 2 ]]; then
  usage
  exit 1
fi

language="$1"
shift

case "$language" in
  python)
    "$ROOT_DIR/python/patterns/scripts/run-pattern.sh" "$@"
    ;;
  nodejs)
    "$ROOT_DIR/nodejs/patterns/scripts/run-pattern.sh" "$@"
    ;;
  java)
    "$ROOT_DIR/java/patterns/scripts/run-pattern.sh" "$@"
    ;;
  csharp)
    "$ROOT_DIR/csharp/patterns/scripts/run-pattern.sh" "$@"
    ;;
  *)
    echo "Unsupported language: $language" >&2
    usage
    exit 2
    ;;
esac
