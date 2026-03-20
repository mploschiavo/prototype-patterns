# C# Hello World Logger Service

ASP.NET minimal API returning `hello world with logger` on `GET /` and writing a log event.

## Test

```bash
dotnet test HelloWorldLoggerService.sln
```

## Run Locally

```bash
dotnet run --project src/HelloWorldLoggerService/HelloWorldLoggerService.csproj
```

## Deploy Scenarios

- Docker: `./infra/docker/run.sh`
- Docker Compose: `docker compose -f infra/compose/docker-compose.yml up --build`
- Kubernetes: `kubectl apply -k infra/k8s`
