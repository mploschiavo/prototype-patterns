# Java REST + Redis (Single Node)

## Infra

Use: `integration-prototypes/infra/redis-single/docker-compose.yml`

## Run

```bash
mvn -q -DskipTests package
REDIS_URL='redis://localhost:6379' mvn -q exec:java -Dexec.mainClass=org.prototype.redis.single.RedisSingleRestServer
# open http://localhost:8080/value?key=demo:key
```

## Test

```bash
mvn test
```
