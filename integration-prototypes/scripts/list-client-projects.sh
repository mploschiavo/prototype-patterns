#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

for language in python nodejs java csharp; do
  for project_dir in "$ROOT_DIR/$language"/*; do
    project="$(basename "$project_dir")"
    if [[ -x "$project_dir/docker/run.sh" && -x "$project_dir/k8s/run.sh" ]]; then
      echo "$language/$project"
    fi
  done
done
