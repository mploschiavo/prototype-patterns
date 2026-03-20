# Java REST + OpenSearch (Single Node)

## Infra

Use: `integration-prototypes/infra/opensearch-single/docker-compose.yml`

## Run

```bash
mvn -q -DskipTests package
OPENSEARCH_URL='http://localhost:9200' mvn -q exec:java -Dexec.mainClass=org.prototype.opensearch.single.OpenSearchSingleRestServer
# open http://localhost:8080/value?index=prototype_docs&id=1
```

## Test

```bash
mvn test
```
