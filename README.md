# Prototype Patterns (Multi-Language)

This repository is an academic prototype workspace that includes:

- 24 design pattern examples for each language:
  - C#
  - Java
  - Python
  - Node.js
- Language-specific REST services in two variants:
  - `hello world`
  - `hello world with logger`
- Infra deployment scaffolding aligned to `pelican38`-style scenarios:
  - `infra/docker`
  - `infra/compose`
  - `infra/k8s`

## Repository Layout

- `csharp/`
  - `patterns/`
  - `services/hello-world/`
  - `services/hello-world-logger/`
- `java/`
  - `patterns/`
  - `services/hello-world/`
  - `services/hello-world-logger/`
- `python/`
  - `patterns/`
  - `services/hello-world/`
  - `services/hello-world-logger/`
- `nodejs/`
  - `patterns/`
  - `services/hello-world/`
  - `services/hello-world-logger/`
- `integration-prototypes/`
  - `infra/` (Kafka/Postgres/Redis/OpenSearch container scenarios)
  - `python/` (Kafka clients + Postgres/Redis/OpenSearch REST prototypes)
  - `nodejs/` (Kafka clients + Postgres/Redis/OpenSearch REST prototypes)
  - `java/` (Kafka clients + Postgres/Redis/OpenSearch REST prototypes)
  - `csharp/` (Kafka clients + Postgres/Redis/OpenSearch REST prototypes)

Each project has its own README with run/test/deploy commands.

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

## Test Commands

Run everything automatically:

```bash
./run-all-tests.sh
```

Python:

```bash
cd python/patterns
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_patterns_unittest.py' -v

cd ../services/hello-world
python3 -m unittest discover -s tests -v

cd ../hello-world-logger
python3 -m unittest discover -s tests -v
```

Node.js:

```bash
cd nodejs/patterns && npm test
cd ../services/hello-world && npm test
cd ../hello-world-logger && npm test
```

Java:

```bash
cd java/patterns && ./scripts/test.sh
cd ../services/hello-world && ./scripts/test.sh
cd ../hello-world-logger && ./scripts/test.sh
```

C#:

```bash
cd csharp/patterns && dotnet test PrototypePatterns.sln
cd ../services/hello-world && dotnet test HelloWorldService.sln
cd ../hello-world-logger && dotnet test HelloWorldLoggerService.sln
```

## Licensing

This repository is dual-licensed for public use under either:

- MIT License (`LICENSE-MIT`)
- Apache License 2.0 (`LICENSE-APACHE`)

You may choose either license for your use.
