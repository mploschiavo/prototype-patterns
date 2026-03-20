# Java Workspace

Java prototypes and services for pattern exercises and REST-style demos.

## Contents

- `patterns`: 24 design pattern prototypes with a zero-dependency test runner
- `services/hello-world`: JDK HTTP service returning `hello world`
- `services/hello-world-logger`: JDK HTTP service returning `hello world with logger`

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
./scripts/test.sh
```

### Run Services

```bash
cd services/hello-world
mkdir -p build/classes
find src/main/java -name "*.java" > build/sources.txt
javac --release 21 -d build/classes @build/sources.txt
java -cp build/classes org.prototype.services.helloworld.HelloWorldServer

cd ../hello-world-logger
mkdir -p build/classes
find src/main/java -name "*.java" > build/sources.txt
javac --release 21 -d build/classes @build/sources.txt
java -cp build/classes org.prototype.services.helloworldlogger.HelloWorldLoggerServer
```

### Run Service Tests

```bash
cd services/hello-world
./scripts/test.sh

cd ../hello-world-logger
./scripts/test.sh
```

## Container/Kubernetes Scenarios

Each service includes:

- `infra/docker/run.sh`
- `infra/compose/docker-compose.yml`
- `infra/k8s/`

## Related Integration Scenarios

For Kafka/Postgres/Redis/OpenSearch/Ollama scenario runs, see:

- `integration-prototypes/java/README.md`
