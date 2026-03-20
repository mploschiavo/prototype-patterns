# Integration Prototypes (Kafka / Postgres / Redis / OpenSearch / Ollama)

This workspace provides academic, language-by-language prototypes for integration patterns:

- Kafka producer/consumer clients:
  - single-node Kafka
  - three-node Kafka cluster
- REST + Postgres:
  - fetch one record from seeded table
- REST + Redis:
  - fetch one value from single-node Redis
  - fetch one value from three-node Redis cluster
- REST + OpenSearch:
  - fetch one value from single-node OpenSearch
  - fetch one value from three-node OpenSearch cluster
- MCP + Ollama + RAG:
  - single-node Ollama infra with seeded model/documents
  - language-specific MCP-style agent servers with `rag.search` and `agent.answer`

## Layout

- `infra/`: shared infrastructure scenarios for local Docker and microk8s
- `python/`: Python implementations + tests
- `nodejs/`: Node.js implementations + tests
- `java/`: Java implementations + tests
- `csharp/`: C# implementations + tests

Each scenario folder has its own `README.md` and test suite.

## Client Packaging

All language client projects are now packaged with:

- `docker/Dockerfile`
- `docker/run.sh`
- `k8s/namespace.yaml`
- `k8s/workload.yaml`
- `k8s/kustomization.yaml`
- `k8s/run.sh`

For Kafka clients, `docker/entrypoint.sh` is also included to switch between producer and consumer mode.

## Run Locally

Generic helper:

```bash
./scripts/run-client-local.sh <python|nodejs|java|csharp> <project> [producer|consumer]
```

Examples:

```bash
./scripts/run-client-local.sh python postgres-rest
./scripts/run-client-local.sh nodejs opensearch-ha-rest
./scripts/run-client-local.sh java kafka-single producer
./scripts/run-client-local.sh csharp kafka-ha consumer
```

## Run On MicroK8s

Generic helper:

```bash
./scripts/deploy-client-microk8s.sh <python|nodejs|java|csharp> <project> [apply|delete]
```

Examples:

```bash
./scripts/deploy-client-microk8s.sh python postgres-rest apply
./scripts/deploy-client-microk8s.sh nodejs redis-single-rest apply
./scripts/deploy-client-microk8s.sh java kafka-ha apply
./scripts/deploy-client-microk8s.sh csharp ollama-mcp-server apply
```

List all packaged client projects:

```bash
./scripts/list-client-projects.sh
```
