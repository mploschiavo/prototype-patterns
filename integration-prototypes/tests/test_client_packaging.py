from __future__ import annotations

import os
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("python", "nodejs", "java", "csharp")
PROJECTS = (
    "kafka-single",
    "kafka-ha",
    "postgres-rest",
    "redis-single-rest",
    "redis-ha-rest",
    "opensearch-single-rest",
    "opensearch-ha-rest",
    "ollama-mcp-server",
)


class ClientPackagingTests(unittest.TestCase):
    def test_packaging_files_exist_for_all_projects(self) -> None:
        required_common = (
            ".dockerignore",
            "docker/Dockerfile",
            "docker/run.sh",
            "k8s/namespace.yaml",
            "k8s/workload.yaml",
            "k8s/kustomization.yaml",
            "k8s/run.sh",
        )

        for language in LANGUAGES:
            for project in PROJECTS:
                project_dir = ROOT / language / project
                self.assertTrue(project_dir.exists(), f"missing project dir: {project_dir}")

                for rel_path in required_common:
                    target = project_dir / rel_path
                    self.assertTrue(target.exists(), f"missing {rel_path} for {language}/{project}")

                if project.startswith("kafka-"):
                    self.assertTrue((project_dir / "docker/entrypoint.sh").exists())

    def test_run_scripts_are_executable(self) -> None:
        for language in LANGUAGES:
            for project in PROJECTS:
                for rel_path in ("docker/run.sh", "k8s/run.sh"):
                    target = ROOT / language / project / rel_path
                    self.assertTrue(os.access(target, os.X_OK), f"not executable: {target}")

    def test_workload_shapes_match_project_type(self) -> None:
        for language in LANGUAGES:
            for project in PROJECTS:
                workload = (ROOT / language / project / "k8s/workload.yaml").read_text(encoding="utf-8")

                if project.startswith("kafka-"):
                    self.assertIn("kind: Job", workload)
                    self.assertIn("KAFKA_CLIENT_MODE", workload)
                else:
                    self.assertIn("kind: Deployment", workload)
                    self.assertIn("kind: Service", workload)

    def test_client_listing_script_reports_all_projects(self) -> None:
        script = ROOT / "scripts" / "list-client-projects.sh"
        output = subprocess.check_output([str(script)], text=True)
        lines = [line.strip() for line in output.splitlines() if line.strip()]

        self.assertEqual(len(lines), len(LANGUAGES) * len(PROJECTS))

        expected = {f"{language}/{project}" for language in LANGUAGES for project in PROJECTS}
        self.assertEqual(set(lines), expected)


if __name__ == "__main__":
    unittest.main()
