from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InfraHealthChecksContractTests(unittest.TestCase):
    def test_all_docker_compose_files_define_healthcheck(self) -> None:
        compose_files = sorted(ROOT.rglob("docker-compose.yml"))
        self.assertTrue(compose_files, "no docker-compose.yml files found")

        for compose_file in compose_files:
            content = compose_file.read_text(encoding="utf-8")
            self.assertIn("healthcheck:", content, f"missing healthcheck in {compose_file}")

    def test_k8s_deployments_and_statefulsets_define_readiness_and_liveness(self) -> None:
        k8s_files = sorted(ROOT.rglob("k8s/*.yaml"))
        self.assertTrue(k8s_files, "no k8s/*.yaml files found")

        workload_kind = re.compile(r"^kind:\s*(Deployment|StatefulSet)\s*$", re.MULTILINE)

        for manifest_file in k8s_files:
            content = manifest_file.read_text(encoding="utf-8")
            if workload_kind.search(content):
                self.assertIn("readinessProbe:", content, f"missing readinessProbe in {manifest_file}")
                self.assertIn("livenessProbe:", content, f"missing livenessProbe in {manifest_file}")


if __name__ == "__main__":
    unittest.main()
