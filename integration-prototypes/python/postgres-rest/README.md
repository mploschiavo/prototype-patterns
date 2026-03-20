# Python REST + Postgres

REST service returning JSON from Postgres table `demo_items`.

## Infra

Use: `integration-prototypes/infra/postgres/docker-compose.yml`

## Run

```bash
export POSTGRES_DSN='postgresql://prototype_user:prototype_pass@localhost:5432/prototype_db'
python3 app.py
# open http://localhost:8080/item?id=1
```

## Test

```bash
python3 -m unittest -v test_postgres_rest.py
```
