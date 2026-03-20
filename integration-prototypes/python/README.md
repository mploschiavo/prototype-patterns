# Python Integration Prototypes

Python implementations of all integration scenarios in this repository.

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
- Python 3
- For Kubernetes mode: MicroK8s and `microk8s kubectl`

## List Available Client Projects

```bash
../scripts/list-client-projects.sh | grep '^python/'
```

## Local Scenario Examples

### Example: Postgres REST

```bash
# from integration-prototypes/python
../infra/scripts/deploy-local.sh postgres
../scripts/run-client-local.sh python postgres-rest
curl -s "http://localhost:8080/item?id=1"
```

### Example: Kafka Producer + Consumer

```bash
# from integration-prototypes/python
../infra/scripts/deploy-local.sh kafka-single
../scripts/run-client-local.sh python kafka-single producer
../scripts/run-client-local.sh python kafka-single consumer
```

### Example: Ollama MCP

```bash
# from integration-prototypes/python
../infra/scripts/deploy-local.sh ollama-single
../scripts/run-client-local.sh python ollama-mcp-server
```

## MicroK8s Scenario Example

```bash
# from integration-prototypes/python
../infra/scripts/deploy-microk8s.sh redis-single apply
../scripts/deploy-client-microk8s.sh python redis-single-rest apply
microk8s kubectl port-forward -n integration-clients service/python-redis-single-rest 8080:8080
curl -s "http://localhost:8080/value?key=demo:key"
```

Cleanup:

```bash
../scripts/deploy-client-microk8s.sh python redis-single-rest delete
../infra/scripts/deploy-microk8s.sh redis-single delete
```

## Tests

Packaging tests from repo root:

```bash
python3 -m unittest -v integration-prototypes/tests/test_client_packaging.py
```

Per-scenario tests are documented in each project README.
