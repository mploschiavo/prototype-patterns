# C# REST + OpenSearch (Single Node)

## Infra

Use: `integration-prototypes/infra/opensearch-single/docker-compose.yml`

## Run

```bash
OPENSEARCH_URL='http://localhost:9200' dotnet run --project src/OpenSearchSingleRestService/OpenSearchSingleRestService.csproj
# open http://localhost:8080/value?index=prototype_docs&id=1
```

## Test

```bash
dotnet test tests/OpenSearchSingleRestService.Tests/OpenSearchSingleRestService.Tests.csproj
```
