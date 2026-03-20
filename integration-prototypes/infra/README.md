# Integration Infrastructure Prototypes

Shared infrastructure scenarios used by language-specific integration clients.

## Deployment Modes

- Local Docker Compose
- MicroK8s (`kustomize` manifests)

## Health Model

- Docker Compose services include `healthcheck` definitions.
- Seed/init containers use healthy dependencies where supported.
- MicroK8s workloads include `startupProbe`, `readinessProbe`, and `livenessProbe` for `Deployment`/`StatefulSet` resources.

## Prerequisites

- Docker + Docker Compose
- kubectl or MicroK8s (`microk8s kubectl`)
- `curl` for verification examples

## Scenario List

- `kafka-single`
- `kafka-ha`
- `postgres`
- `redis-single`
- `redis-ha`
- `opensearch-single`
- `opensearch-ha`
- `ollama-single`

## Local Docker Usage

Generic helper:

```bash
./scripts/deploy-local.sh <scenario> [up|down]
```

Examples:

```bash
./scripts/deploy-local.sh kafka-single up
./scripts/deploy-local.sh postgres up
./scripts/deploy-local.sh redis-ha up
./scripts/deploy-local.sh opensearch-single up
./scripts/deploy-local.sh ollama-single up
```

Teardown:

```bash
./scripts/deploy-local.sh kafka-single down
./scripts/deploy-local.sh kafka-ha down
./scripts/deploy-local.sh postgres down
./scripts/deploy-local.sh redis-single down
./scripts/deploy-local.sh redis-ha down
./scripts/deploy-local.sh opensearch-single down
./scripts/deploy-local.sh opensearch-ha down
./scripts/deploy-local.sh ollama-single down
```

## MicroK8s Usage

Generic helper:

```bash
./scripts/deploy-microk8s.sh <scenario> [apply|delete]
```

Examples:

```bash
./scripts/deploy-microk8s.sh kafka-single apply
./scripts/deploy-microk8s.sh postgres apply
./scripts/deploy-microk8s.sh redis-ha apply
./scripts/deploy-microk8s.sh opensearch-ha apply
./scripts/deploy-microk8s.sh ollama-single apply
```

Delete examples:

```bash
./scripts/deploy-microk8s.sh postgres delete
./scripts/deploy-microk8s.sh redis-single delete
```

## Default Local Endpoints

- Kafka single: `localhost:9092`
- Kafka HA: `localhost:9092,localhost:9094,localhost:9096`
- Postgres: `postgresql://prototype_user:prototype_pass@localhost:5432/prototype_db`
- Redis single: `redis://localhost:6379`
- Redis HA nodes: `localhost:6379`, `localhost:6380`, `localhost:6381`
- OpenSearch single: `http://localhost:9200`
- OpenSearch HA: `http://localhost:9200`, `http://localhost:9201`, `http://localhost:9202`
- OpenSearch Dashboards single: `http://localhost:5601`
- OpenSearch Dashboards HA: `http://localhost:5602`
- Ollama: `http://localhost:11434`

## Verification Examples

### Check Docker health states

```bash
docker compose -f postgres/docker-compose.yml ps
docker compose -f redis-single/docker-compose.yml ps
docker compose -f opensearch-single/docker-compose.yml ps
```

### Verify services are reachable

```bash
curl -s http://localhost:9200/_cluster/health
curl -s http://localhost:5601/api/status
curl -s http://localhost:11434/api/tags
```

### Check MicroK8s probes/status

```bash
microk8s kubectl get pods -A
microk8s kubectl describe pod -n integration-postgres -l app=postgres
microk8s kubectl describe pod -n integration-opensearch-single -l app=opensearch-single
```

## Scenario Quick Map

- `kafka-single`: single broker for quick producer/consumer exercises
- `kafka-ha`: three brokers for HA/cluster behavior
- `postgres`: seeded `demo_items` table for REST query examples
- `redis-single`: seeded `demo:key` value for simple key fetch
- `redis-ha`: Redis cluster setup with seeded key
- `opensearch-single`: seeded `prototype_docs` index with doc id `1`
- `opensearch-ha`: clustered OpenSearch + seeded index
- `ollama-single`: seeded `tinyllama` model + mounted RAG docs
