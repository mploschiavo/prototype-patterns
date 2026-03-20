# Java REST + Postgres

## Infra

Use: `integration-prototypes/infra/postgres/docker-compose.yml`

## Run

```bash
mvn -q -DskipTests package
POSTGRES_JDBC_URL='jdbc:postgresql://localhost:5432/prototype_db' POSTGRES_USER=prototype_user POSTGRES_PASSWORD=prototype_pass mvn -q exec:java -Dexec.mainClass=org.prototype.postgres.PostgresRestServer
# open http://localhost:8080/item?id=1
```

## Test

```bash
mvn test
```
