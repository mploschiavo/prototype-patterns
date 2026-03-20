# Python Workspace

Python prototypes and services for pattern exercises and lightweight REST demos.

## Contents

- `patterns`: 24 design pattern prototypes
- `services/hello-world`: REST service returning `hello world`
- `services/hello-world-logger`: REST service returning `hello world with logger`

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
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_patterns_unittest.py' -v
```

### Run Services

```bash
cd services/hello-world
python3 src/app.py

cd ../hello-world-logger
python3 src/app.py
```

### Run Service Tests

```bash
cd services/hello-world
python3 -m unittest discover -s tests -v

cd ../hello-world-logger
python3 -m unittest discover -s tests -v
```

## Container/Kubernetes Scenarios

Each service includes:

- `infra/docker/run.sh`
- `infra/compose/docker-compose.yml`
- `infra/k8s/`

## Related Integration Scenarios

For Kafka/Postgres/Redis/OpenSearch/Ollama scenario runs, see:

- `integration-prototypes/python/README.md`
