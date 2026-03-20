#!/usr/bin/env bash
set -euo pipefail

RESOURCE_GROUP="${RESOURCE_GROUP:-prototype-rg}"
CLUSTER_NAME="${CLUSTER_NAME:-prototype-aks}"
REGION="${REGION:-eastus}"
NODE_COUNT="${NODE_COUNT:-2}"
VM_SIZE="${VM_SIZE:-Standard_D4s_v5}"
EXECUTE="${EXECUTE:-0}"

COMMANDS=(
  "az group create --name ${RESOURCE_GROUP} --location ${REGION}"
  "az aks create --resource-group ${RESOURCE_GROUP} --name ${CLUSTER_NAME} --node-count ${NODE_COUNT} --node-vm-size ${VM_SIZE} --generate-ssh-keys"
  "az aks get-credentials --resource-group ${RESOURCE_GROUP} --name ${CLUSTER_NAME} --overwrite-existing"
)

for command in "${COMMANDS[@]}"; do
  echo "$command"
  if [[ "$EXECUTE" == "1" ]]; then
    eval "$command"
  fi
done
