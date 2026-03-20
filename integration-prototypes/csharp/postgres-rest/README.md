# C# REST + Postgres

## Infra

Use: `integration-prototypes/infra/postgres/docker-compose.yml`

## Run

```bash
POSTGRES_CONNECTION_STRING='Host=localhost;Port=5432;Username=prototype_user;Password=prototype_pass;Database=prototype_db' dotnet run --project src/PostgresRestService/PostgresRestService.csproj
# open http://localhost:8080/item?id=1
```

## Test

```bash
dotnet test tests/PostgresRestService.Tests/PostgresRestService.Tests.csproj
```
