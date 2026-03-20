#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <scenario> [apply|delete]"
  exit 1
fi

SCENARIO="$1"
ACTION="${2:-apply}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
K8S_DIR="$ROOT_DIR/$SCENARIO/k8s"

if [[ ! -d "$K8S_DIR" ]]; then
  echo "No microk8s manifests found for scenario: $SCENARIO"
  exit 1
fi

KUBECTL="kubectl"
if command -v microk8s >/dev/null 2>&1; then
  KUBECTL="microk8s kubectl"
fi

if [[ "$ACTION" == "delete" ]]; then
  $KUBECTL delete -k "$K8S_DIR" --ignore-not-found
else
  $KUBECTL apply -k "$K8S_DIR"
fi
