# C# Workspace

C# prototypes and services for pattern exercises and ASP.NET demos.

## Contents

- `patterns`: 24 design pattern prototypes with xUnit tests
- `services/hello-world`: ASP.NET service returning `hello world`
- `services/hello-world-logger`: ASP.NET service returning `hello world with logger`

## Quick Commands

### Run One Pattern

```bash
cd patterns
./scripts/run-pattern.sh --list
./scripts/run-pattern.sh --pattern singleton
```

### Run Pattern Tests

```bash
cd patterns
dotnet test PrototypePatterns.sln
```

### Run Services

```bash
cd services/hello-world
dotnet run --project src/HelloWorldService/HelloWorldService.csproj

cd ../hello-world-logger
dotnet run --project src/HelloWorldLoggerService/HelloWorldLoggerService.csproj
```

### Run Service Tests

```bash
cd services/hello-world
dotnet test HelloWorldService.sln

cd ../hello-world-logger
dotnet test HelloWorldLoggerService.sln
```

## Container/Kubernetes Scenarios

Each service includes:

- `infra/docker/run.sh`
- `infra/compose/docker-compose.yml`
- `infra/k8s/`

## Related Integration Scenarios

For Kafka/Postgres/Redis/OpenSearch/Ollama scenario runs, see:

- `integration-prototypes/csharp/README.md`
