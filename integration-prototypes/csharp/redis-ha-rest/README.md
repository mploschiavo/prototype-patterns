# C# REST + Redis (HA Cluster)

## Infra

Use: `integration-prototypes/infra/redis-ha/docker-compose.yml`

## Run

```bash
REDIS_CLUSTER_ENDPOINTS='localhost:6379,localhost:6380,localhost:6381' dotnet run --project src/RedisHaRestService/RedisHaRestService.csproj
# open http://localhost:8080/value?key=demo:key
```

## Test

```bash
dotnet test tests/RedisHaRestService.Tests/RedisHaRestService.Tests.csproj
```
