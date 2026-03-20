# Integration Prototypes (Kafka / Postgres / Redis / OpenSearch)

This workspace provides academic, language-by-language prototypes for integration patterns:

- Kafka producer/consumer clients:
  - single-node Kafka
  - three-node Kafka cluster
- REST + Postgres:
  - fetch one record from seeded table
- REST + Redis:
  - fetch one value from single-node Redis
  - fetch one value from three-node Redis cluster
- REST + OpenSearch:
  - fetch one value from single-node OpenSearch
  - fetch one value from three-node OpenSearch cluster

## Layout

- `infra/`: shared docker-compose infrastructure scenarios
- `python/`: Python implementations + tests
- `nodejs/`: Node.js implementations + tests
- `java/`: Java implementations + tests
- `csharp/`: C# implementations + tests

Each scenario folder has its own `README.md` and test suite.
