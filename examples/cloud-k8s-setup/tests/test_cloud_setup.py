from __future__ import annotations

import unittest

from aws.create_eks import build_commands as build_eks
from azure.create_aks import build_commands as build_aks
from gcp.create_gke import build_commands as build_gke


class CloudSetupTests(unittest.TestCase):
    def test_aws_commands(self) -> None:
        commands = build_eks("demo-eks", "us-east-2", "demo-ng", 3, "t3.large")
        self.assertEqual(len(commands), 3)
        self.assertIn("demo-eks", commands[0])

    def test_azure_commands(self) -> None:
        commands = build_aks("demo-rg", "demo-aks", "eastus", 2, "Standard_D4s_v5")
        self.assertEqual(len(commands), 3)
        self.assertIn("demo-aks", commands[1])

    def test_gcp_commands(self) -> None:
        commands = build_gke("demo-project", "demo-gke", "us-central1", 2, "e2-standard-4")
        self.assertEqual(len(commands), 3)
        self.assertIn("demo-gke", commands[1])


if __name__ == "__main__":
    unittest.main()
