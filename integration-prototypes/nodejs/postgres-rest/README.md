# Node.js REST + Postgres

## Infra

Use: `integration-prototypes/infra/postgres/docker-compose.yml`

## Run

```bash
npm install
PG_CONNECTION_STRING='postgresql://prototype_user:prototype_pass@localhost:5432/prototype_db' node app.js
# open http://localhost:8080/item?id=1
```

## Test

```bash
npm test
```
