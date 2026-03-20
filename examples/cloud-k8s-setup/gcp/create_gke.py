from __future__ import annotations

import argparse
import subprocess


def build_commands(project_id: str, cluster_name: str, region: str, node_count: int, machine_type: str) -> list[str]:
    return [
        f"gcloud config set project {project_id}",
        (
            "gcloud container clusters create "
            f"{cluster_name} --region {region} --num-nodes {node_count} --machine-type {machine_type}"
        ),
        f"gcloud container clusters get-credentials {cluster_name} --region {region}",
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a GCP GKE cluster (dry-run by default)")
    parser.add_argument("--project-id", default="prototype-project")
    parser.add_argument("--cluster-name", default="prototype-gke")
    parser.add_argument("--region", default="us-central1")
    parser.add_argument("--node-count", type=int, default=2)
    parser.add_argument("--machine-type", default="e2-standard-4")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    commands = build_commands(args.project_id, args.cluster_name, args.region, args.node_count, args.machine_type)
    for command in commands:
        print(command)
        if args.execute:
            subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    main()
