# Node.js Workspace

Node.js prototypes and services for pattern exercises and HTTP demos.

## Contents

- `patterns`: 24 design pattern prototypes with `node --test`
- `services/hello-world`: HTTP service returning `hello world`
- `services/hello-world-logger`: HTTP service returning `hello world with logger`

## Quick Commands

### Run One Pattern

```bash
cd patterns
./scripts/run-pattern.sh --list
./scripts/run-pattern.sh --pattern singleton
```

### Run Pattern Tests

```bash
cd patterns
npm test
```

### Run Services

```bash
cd services/hello-world
npm start

cd ../hello-world-logger
npm start
```

### Run Service Tests

```bash
cd services/hello-world
npm test

cd ../hello-world-logger
npm test
```

## Container/Kubernetes Scenarios

Each service includes:

- `infra/docker/run.sh`
- `infra/compose/docker-compose.yml`
- `infra/k8s/`

## Related Integration Scenarios

For Kafka/Postgres/Redis/OpenSearch/Ollama scenario runs, see:

- `integration-prototypes/nodejs/README.md`
