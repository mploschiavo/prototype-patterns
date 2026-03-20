# Integration Infrastructure Prototypes

This folder provides infrastructure scenarios used by the language-specific prototypes.

Deployment modes:

- Local Docker Compose
- MicroK8s (kustomize manifests)

## Scenarios

- `kafka-single`: Single-node Kafka (KRaft)
- `kafka-ha`: Three-node Kafka cluster (KRaft)
- `postgres`: PostgreSQL with seeded demo table
- `redis-single`: Single-node Redis with seeded key
- `redis-ha`: Three-node Redis Cluster with seeded key
- `opensearch-single`: Single-node OpenSearch with seeded document
- `opensearch-ha`: Three-node OpenSearch cluster with seeded document
- `ollama-single`: Single-node Ollama with seeded model and RAG documents

## Quick Start (Local)

Generic script:

```bash
./scripts/deploy-local.sh <scenario>
```

Examples:

Kafka single:

```bash
cd kafka-single
docker compose up -d
```

Kafka HA:

```bash
cd kafka-ha
docker compose up -d
```

Postgres:

```bash
cd postgres
docker compose up -d
```

Redis single:

```bash
cd redis-single
docker compose up -d
```

Redis HA:

```bash
cd redis-ha
docker compose up -d
```

OpenSearch single:

```bash
cd opensearch-single
docker compose up -d
```

OpenSearch HA:

```bash
cd opensearch-ha
docker compose up -d
```

Ollama single:

```bash
cd ollama-single
docker compose up -d
```

## Quick Start (MicroK8s)

Generic script:

```bash
./scripts/deploy-microk8s.sh <scenario> apply
```

Examples:

```bash
./scripts/deploy-microk8s.sh kafka-single apply
./scripts/deploy-microk8s.sh postgres apply
./scripts/deploy-microk8s.sh opensearch-ha apply
./scripts/deploy-microk8s.sh ollama-single apply
```

## Default Connection Endpoints

- Kafka single bootstrap: `localhost:9092`
- Kafka HA bootstrap: `localhost:9092,localhost:9094,localhost:9096`
- Postgres: `postgresql://prototype_user:prototype_pass@localhost:5432/prototype_db`
- Redis single: `redis://localhost:6379`
- Redis HA startup nodes: `localhost:6379`, `localhost:6380`, `localhost:6381`
- OpenSearch single: `http://localhost:9200`
- OpenSearch HA nodes: `http://localhost:9200`, `http://localhost:9201`, `http://localhost:9202`
- Ollama single: `http://localhost:11434`
