# C# Kafka Producer/Consumer (HA Cluster)

## Infra

Use: `integration-prototypes/infra/kafka-ha/docker-compose.yml`

## Run

```bash
dotnet run --project src/KafkaHaClients/KafkaHaClients.csproj
# consume one message
dotnet run --project src/KafkaHaClients/KafkaHaClients.csproj -- consume
```

## Test

```bash
dotnet test tests/KafkaHaClients.Tests/KafkaHaClients.Tests.csproj
```
