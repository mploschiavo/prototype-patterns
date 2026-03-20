# C# REST + Redis (Single Node)

## Infra

Use: `integration-prototypes/infra/redis-single/docker-compose.yml`

## Run

```bash
REDIS_CONNECTION='localhost:6379' dotnet run --project src/RedisSingleRestService/RedisSingleRestService.csproj
# open http://localhost:8080/value?key=demo:key
```

## Test

```bash
dotnet test tests/RedisSingleRestService.Tests/RedisSingleRestService.Tests.csproj
```
