# Python REST + Redis (Single Node)

REST service returning JSON value from Redis key.

## Infra

Use: `integration-prototypes/infra/redis-single/docker-compose.yml`

## Run

```bash
export REDIS_URL='redis://localhost:6379'
python3 app.py
# open http://localhost:8080/value?key=demo:key
```

## Test

```bash
python3 -m unittest -v test_redis_single_rest.py
```
