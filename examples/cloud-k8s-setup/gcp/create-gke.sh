#!/usr/bin/env bash
set -euo pipefail

PROJECT_ID="${PROJECT_ID:-prototype-project}"
CLUSTER_NAME="${CLUSTER_NAME:-prototype-gke}"
REGION="${REGION:-us-central1}"
NODE_COUNT="${NODE_COUNT:-2}"
MACHINE_TYPE="${MACHINE_TYPE:-e2-standard-4}"
EXECUTE="${EXECUTE:-0}"

COMMANDS=(
  "gcloud config set project ${PROJECT_ID}"
  "gcloud container clusters create ${CLUSTER_NAME} --region ${REGION} --num-nodes ${NODE_COUNT} --machine-type ${MACHINE_TYPE}"
  "gcloud container clusters get-credentials ${CLUSTER_NAME} --region ${REGION}"
)

for command in "${COMMANDS[@]}"; do
  echo "$command"
  if [[ "$EXECUTE" == "1" ]]; then
    eval "$command"
  fi
done
