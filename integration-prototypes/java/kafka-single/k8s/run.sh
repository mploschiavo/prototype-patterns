#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="prototype/java-kafka-single:latest"
ACTION="${1:-apply}"
case "$ACTION" in
  apply)
    docker build -f "$ROOT_DIR/docker/Dockerfile" -t "$IMAGE" "$ROOT_DIR"
    archive="$(mktemp --suffix=.tar)"
    trap "rm -f $archive" EXIT
    docker save "$IMAGE" -o "$archive"
    microk8s ctr image import "$archive"
    microk8s kubectl delete -f "$ROOT_DIR/k8s/workload.yaml" --ignore-not-found
    microk8s kubectl apply -k "$ROOT_DIR/k8s"
    echo "Use: microk8s kubectl logs -n integration-clients job/java-kafka-single-producer"
    ;;
  delete)
    microk8s kubectl delete -k "$ROOT_DIR/k8s" --ignore-not-found
    ;;
  *)
    echo "Usage: ./k8s/run.sh [apply|delete]" >&2
    exit 1
    ;;
esac
