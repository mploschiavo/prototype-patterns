# Python REST + Redis (HA Cluster)

REST service returning JSON value from Redis cluster key.

## Infra

Use: `integration-prototypes/infra/redis-ha/docker-compose.yml`

## Run

```bash
export REDIS_CLUSTER_NODES='localhost:6379,localhost:6380,localhost:6381'
python3 app.py
# open http://localhost:8080/value?key=demo:key
```

## Test

```bash
python3 -m unittest -v test_redis_ha_rest.py
```
