# Integration Prototypes (Kafka / Postgres / Redis / OpenSearch / Ollama)

This workspace provides language-by-language integration examples with the same scenario set in Python, Node.js, Java, and C#.

## Scenarios Covered

- Kafka clients:
  - `kafka-single` (one-node Kafka)
  - `kafka-ha` (three-node Kafka)
- Postgres REST:
  - `postgres-rest`
- Redis REST:
  - `redis-single-rest`
  - `redis-ha-rest`
- OpenSearch REST:
  - `opensearch-single-rest`
  - `opensearch-ha-rest`
- Ollama MCP + RAG:
  - `ollama-mcp-server`

## Folder Layout

- `infra/`: shared infrastructure scenarios (local Docker + MicroK8s)
- `python/`: Python clients/services per scenario
- `nodejs/`: Node.js clients/services per scenario
- `java/`: Java clients/services per scenario
- `csharp/`: C# clients/services per scenario
- `scripts/`: helper entrypoints for local and MicroK8s runs

## Prerequisites

- Docker + Docker Compose
- Python 3 (for test runner and helper tests)
- Language runtime(s) you want to run directly (`node`, `java`, `dotnet`, `python3`)
- For Kubernetes mode: MicroK8s (or kubectl-compatible cluster)

## Client Packaging Model

Each language project includes:

- `.dockerignore`
- `docker/Dockerfile`
- `docker/run.sh`
- `k8s/namespace.yaml`
- `k8s/workload.yaml`
- `k8s/kustomization.yaml`
- `k8s/run.sh`

Kafka projects also include `docker/entrypoint.sh` to switch producer/consumer mode.

## Helper Scripts

From `integration-prototypes/`:

```bash
./scripts/list-client-projects.sh
./scripts/run-client-local.sh <python|nodejs|java|csharp> <project> [producer|consumer]
./scripts/deploy-client-microk8s.sh <python|nodejs|java|csharp> <project> [apply|delete]
```

## Local End-to-End Examples

### Example A: Postgres + Python REST

```bash
cd integration-prototypes

# 1) Start infra
./infra/scripts/deploy-local.sh postgres

# 2) Run client (containerized)
./scripts/run-client-local.sh python postgres-rest

# 3) Verify
curl -s "http://localhost:8080/item?id=1"
```

### Example B: Kafka Single + Node.js Producer/Consumer

```bash
cd integration-prototypes

# 1) Start Kafka infra
./infra/scripts/deploy-local.sh kafka-single

# 2) Produce one batch
./scripts/run-client-local.sh nodejs kafka-single producer

# 3) Consume
./scripts/run-client-local.sh nodejs kafka-single consumer
```

### Example C: Redis HA + Java REST

```bash
cd integration-prototypes

./infra/scripts/deploy-local.sh redis-ha
./scripts/run-client-local.sh java redis-ha-rest
curl -s "http://localhost:8080/value?key=demo:key"
```

### Example D: OpenSearch Single + C# REST

```bash
cd integration-prototypes

./infra/scripts/deploy-local.sh opensearch-single
./scripts/run-client-local.sh csharp opensearch-single-rest
curl -s "http://localhost:8080/document?id=1"
```

### Example E: Ollama MCP + Python

```bash
cd integration-prototypes

./infra/scripts/deploy-local.sh ollama-single
./scripts/run-client-local.sh python ollama-mcp-server
```

## MicroK8s End-to-End Example

```bash
cd integration-prototypes

# 1) Deploy infra scenario
./infra/scripts/deploy-microk8s.sh redis-single apply

# 2) Deploy language client
./scripts/deploy-client-microk8s.sh python redis-single-rest apply

# 3) Access client
microk8s kubectl port-forward -n integration-clients service/python-redis-single-rest 8080:8080
curl -s "http://localhost:8080/value?key=demo:key"

# 4) Cleanup
./scripts/deploy-client-microk8s.sh python redis-single-rest delete
./infra/scripts/deploy-microk8s.sh redis-single delete
```

## Running Tests

```bash
python3 -m unittest -v tests/test_client_packaging.py
```

For per-language tests, see each scenario README under language folders.

## Cleanup Commands (Local)

```bash
./infra/scripts/deploy-local.sh kafka-single down
./infra/scripts/deploy-local.sh kafka-ha down
./infra/scripts/deploy-local.sh postgres down
./infra/scripts/deploy-local.sh redis-single down
./infra/scripts/deploy-local.sh redis-ha down
./infra/scripts/deploy-local.sh opensearch-single down
./infra/scripts/deploy-local.sh opensearch-ha down
./infra/scripts/deploy-local.sh ollama-single down
```
