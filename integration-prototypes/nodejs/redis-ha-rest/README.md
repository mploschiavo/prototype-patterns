# Node.js REST + Redis (HA Cluster)

## Infra

Use: `integration-prototypes/infra/redis-ha/docker-compose.yml`

## Run

```bash
npm install
REDIS_CLUSTER_NODES='localhost:6379,localhost:6380,localhost:6381' node app.js
# open http://localhost:8080/value?key=demo:key
```

## Test

```bash
npm test
```
