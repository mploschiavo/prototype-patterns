# Prototype Patterns (Multi-Language)

This repository is an academic prototype workspace for design patterns, language-specific services, integration infrastructure, and observability demos.

## What Is Included

- 24 design pattern examples in each language:
  - C#
  - Java
  - Python
  - Node.js
- Language-specific REST services in two variants:
  - `hello world`
  - `hello world with logger`
- Integration prototypes for Kafka, Postgres, Redis, OpenSearch, and Ollama
- Infra scaffolding for local Docker and MicroK8s
- Cloud setup examples (AWS, Azure, GCP)
- Observability demo stack (Grafana + Prometheus + Loki + Tempo + OTel Collector)

## Repository Layout

- `csharp/`
- `java/`
- `python/`
- `nodejs/`
- `integration-prototypes/`
- `examples/cloud-k8s-setup/`
- `observability-demo/hello-world-stack/`

Each folder contains its own README with language or scenario-specific details.

## Prerequisites

Recommended baseline tools:

- `git`
- `docker` + `docker compose`
- `python3`
- `node` + `npm`
- `java` (JDK 21) and optionally `mvn` for integration Java projects
- `dotnet` (for C# projects)

For Kubernetes scenarios:

- `kubectl` or `microk8s kubectl`
- MicroK8s with DNS and storage enabled (recommended for local cluster demos)

## Quick Start By Goal

### 1) Explore One Pattern At A Time

Use the root dispatcher script:

```bash
./scripts/run-pattern.sh python --list
./scripts/run-pattern.sh python --pattern singleton
./scripts/run-pattern.sh nodejs --pattern "chain of responsibility"
./scripts/run-pattern.sh java --all
./scripts/run-pattern.sh csharp --pattern adapter
```

### 2) Run Hello World Services (Any Language)

Example flow (Python):

```bash
cd python/services/hello-world
python3 src/app.py
# open http://localhost:8080/
```

Containerized options are available in each service folder:

- `infra/docker/run.sh`
- `infra/compose/docker-compose.yml`
- `infra/k8s/`

### 3) Run Integration Scenarios (Kafka/Postgres/Redis/OpenSearch/Ollama)

See the detailed runbook in `integration-prototypes/README.md`.

Fast path:

```bash
cd integration-prototypes

# Start infra scenario locally
./infra/scripts/deploy-local.sh postgres

# Run a language client against that infra
./scripts/run-client-local.sh python postgres-rest
```

### 4) Run Observability Demo

```bash
cd observability-demo/hello-world-stack
./docker/run.sh
```

Then use:

- Demo app: `http://localhost:8088`
- Grafana: `http://localhost:3000`

## Run Tests

Run all repository test suites:

```bash
./run-all-tests.sh
```

## Pattern Coverage (Per Language)

1. Singleton
2. Factory Method
3. Abstract Factory
4. Builder
5. Prototype
6. Object Pool
7. Lazy Initialization
8. Adapter
9. Decorator
10. Composite
11. Facade
12. Proxy
13. Bridge
14. Flyweight
15. Composite Entity
16. Observer
17. Strategy
18. Command
19. State
20. Template Method
21. Chain of Responsibility
22. Iterator
23. Mediator
24. Memento

## Licensing

This repository is dual-licensed for public use under either:

- MIT License (`LICENSE-MIT`)
- Apache License 2.0 (`LICENSE-APACHE`)

You may choose either license for your use.
