# Java REST + Redis (HA Cluster)

## Infra

Use: `integration-prototypes/infra/redis-ha/docker-compose.yml`

## Run

```bash
mvn -q -DskipTests package
REDIS_CLUSTER_NODES='localhost:6379,localhost:6380,localhost:6381' mvn -q exec:java -Dexec.mainClass=org.prototype.redis.ha.RedisHaRestServer
# open http://localhost:8080/value?key=demo:key
```

## Test

```bash
mvn test
```
