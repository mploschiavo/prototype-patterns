from __future__ import annotations

import argparse
import subprocess


def build_commands(cluster_name: str, region: str, nodegroup_name: str, node_count: int, node_type: str) -> list[str]:
    return [
        (
            "aws eks create-cluster "
            f"--name {cluster_name} --region {region} --kubernetes-version 1.30 "
            "--role-arn <replace-with-eks-role-arn> "
            "--resources-vpc-config subnetIds=<subnet-ids>,securityGroupIds=<security-group-ids>"
        ),
        (
            "aws eks create-nodegroup "
            f"--cluster-name {cluster_name} --region {region} --nodegroup-name {nodegroup_name} "
            "--node-role <replace-with-node-role-arn> --subnets <subnet-ids> "
            f"--scaling-config minSize=1,maxSize=4,desiredSize={node_count} --instance-types {node_type}"
        ),
        f"aws eks update-kubeconfig --name {cluster_name} --region {region}",
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an AWS EKS cluster (dry-run by default)")
    parser.add_argument("--cluster-name", default="prototype-eks")
    parser.add_argument("--region", default="us-east-1")
    parser.add_argument("--nodegroup-name", default="prototype-ng")
    parser.add_argument("--node-count", type=int, default=2)
    parser.add_argument("--node-type", default="t3.medium")
    parser.add_argument("--execute", action="store_true", help="Execute commands instead of printing")
    args = parser.parse_args()

    commands = build_commands(args.cluster_name, args.region, args.nodegroup_name, args.node_count, args.node_type)
    for command in commands:
        print(command)
        if args.execute:
            subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    main()
