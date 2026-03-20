# Node.js REST + Redis (Single Node)

## Infra

Use: `integration-prototypes/infra/redis-single/docker-compose.yml`

## Run

```bash
npm install
REDIS_URL='redis://localhost:6379' node app.js
# open http://localhost:8080/value?key=demo:key
```

## Test

```bash
npm test
```
