# C# REST + OpenSearch (HA Cluster)

## Infra

Use: `integration-prototypes/infra/opensearch-ha/docker-compose.yml`

## Run

```bash
OPENSEARCH_NODES='http://localhost:9200,http://localhost:9201,http://localhost:9202' dotnet run --project src/OpenSearchHaRestService/OpenSearchHaRestService.csproj
# open http://localhost:8080/value?index=prototype_docs&id=1
```

## Test

```bash
dotnet test tests/OpenSearchHaRestService.Tests/OpenSearchHaRestService.Tests.csproj
```
