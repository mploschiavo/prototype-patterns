# Node.js Integration Prototypes

Node.js implementations of all integration scenarios in this repository.

## Projects

- `kafka-single`
- `kafka-ha`
- `postgres-rest`
- `redis-single-rest`
- `redis-ha-rest`
- `opensearch-single-rest`
- `opensearch-ha-rest`
- `ollama-mcp-server`

Each project includes `docker/` and `k8s/` packaging.

## Prerequisites

- Docker + Docker Compose
- Node.js + npm
- For Kubernetes mode: MicroK8s and `microk8s kubectl`

## List Available Client Projects

```bash
../scripts/list-client-projects.sh | grep '^nodejs/'
```

## Local Scenario Examples

### Example: Postgres REST

```bash
# from integration-prototypes/nodejs
../infra/scripts/deploy-local.sh postgres
../scripts/run-client-local.sh nodejs postgres-rest
curl -s "http://localhost:8080/item?id=1"
```

### Example: Kafka Producer + Consumer

```bash
# from integration-prototypes/nodejs
../infra/scripts/deploy-local.sh kafka-single
../scripts/run-client-local.sh nodejs kafka-single producer
../scripts/run-client-local.sh nodejs kafka-single consumer
```

### Example: Ollama MCP

```bash
# from integration-prototypes/nodejs
../infra/scripts/deploy-local.sh ollama-single
../scripts/run-client-local.sh nodejs ollama-mcp-server
```

## MicroK8s Scenario Example

```bash
# from integration-prototypes/nodejs
../infra/scripts/deploy-microk8s.sh redis-single apply
../scripts/deploy-client-microk8s.sh nodejs redis-single-rest apply
microk8s kubectl port-forward -n integration-clients service/nodejs-redis-single-rest 8080:8080
curl -s "http://localhost:8080/value?key=demo:key"
```

Cleanup:

```bash
../scripts/deploy-client-microk8s.sh nodejs redis-single-rest delete
../infra/scripts/deploy-microk8s.sh redis-single delete
```

## Tests

Packaging tests from repo root:

```bash
python3 -m unittest -v integration-prototypes/tests/test_client_packaging.py
```

Per-scenario tests are documented in each project README.
