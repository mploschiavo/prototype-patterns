#!/usr/bin/env bash
set -euo pipefail

CLUSTER_NAME="${CLUSTER_NAME:-prototype-eks}"
REGION="${REGION:-us-east-1}"
NODEGROUP_NAME="${NODEGROUP_NAME:-prototype-ng}"
NODE_COUNT="${NODE_COUNT:-2}"
NODE_TYPE="${NODE_TYPE:-t3.medium}"
EXECUTE="${EXECUTE:-0}"

COMMANDS=(
  "aws eks create-cluster --name ${CLUSTER_NAME} --region ${REGION} --kubernetes-version 1.30 --role-arn <replace-with-eks-role-arn> --resources-vpc-config subnetIds=<subnet-ids>,securityGroupIds=<security-group-ids>"
  "aws eks create-nodegroup --cluster-name ${CLUSTER_NAME} --region ${REGION} --nodegroup-name ${NODEGROUP_NAME} --node-role <replace-with-node-role-arn> --subnets <subnet-ids> --scaling-config minSize=1,maxSize=4,desiredSize=${NODE_COUNT} --instance-types ${NODE_TYPE}"
  "aws eks update-kubeconfig --name ${CLUSTER_NAME} --region ${REGION}"
)

for command in "${COMMANDS[@]}"; do
  echo "$command"
  if [[ "$EXECUTE" == "1" ]]; then
    eval "$command"
  fi
done
