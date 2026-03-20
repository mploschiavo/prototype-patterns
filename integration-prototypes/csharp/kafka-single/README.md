# C# Kafka Producer/Consumer (Single Node)

## Infra

Use: `integration-prototypes/infra/kafka-single/docker-compose.yml`

## Run

```bash
dotnet run --project src/KafkaSingleClients/KafkaSingleClients.csproj
# consume one message
dotnet run --project src/KafkaSingleClients/KafkaSingleClients.csproj -- consume
```

## Test

```bash
dotnet test tests/KafkaSingleClients.Tests/KafkaSingleClients.Tests.csproj
```
