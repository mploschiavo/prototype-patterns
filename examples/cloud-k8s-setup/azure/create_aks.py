from __future__ import annotations

import argparse
import subprocess


def build_commands(resource_group: str, cluster_name: str, region: str, node_count: int, vm_size: str) -> list[str]:
    return [
        f"az group create --name {resource_group} --location {region}",
        (
            "az aks create "
            f"--resource-group {resource_group} --name {cluster_name} "
            f"--node-count {node_count} --node-vm-size {vm_size} --generate-ssh-keys"
        ),
        f"az aks get-credentials --resource-group {resource_group} --name {cluster_name} --overwrite-existing",
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an Azure AKS cluster (dry-run by default)")
    parser.add_argument("--resource-group", default="prototype-rg")
    parser.add_argument("--cluster-name", default="prototype-aks")
    parser.add_argument("--region", default="eastus")
    parser.add_argument("--node-count", type=int, default=2)
    parser.add_argument("--vm-size", default="Standard_D4s_v5")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    commands = build_commands(args.resource_group, args.cluster_name, args.region, args.node_count, args.vm_size)
    for command in commands:
        print(command)
        if args.execute:
            subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    main()
