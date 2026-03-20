# C# Hello World Service

ASP.NET minimal API returning `hello world` on `GET /`.

## Test

```bash
dotnet test HelloWorldService.sln
```

## Run Locally

```bash
dotnet run --project src/HelloWorldService/HelloWorldService.csproj
```

## Deploy Scenarios

- Docker: `./infra/docker/run.sh`
- Docker Compose: `docker compose -f infra/compose/docker-compose.yml up --build`
- Kubernetes: `kubectl apply -k infra/k8s`
