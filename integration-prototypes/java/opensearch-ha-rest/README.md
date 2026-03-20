# Java REST + OpenSearch (HA Cluster)

## Infra

Use: `integration-prototypes/infra/opensearch-ha/docker-compose.yml`

## Run

```bash
mvn -q -DskipTests package
OPENSEARCH_NODES='http://localhost:9200,http://localhost:9201,http://localhost:9202' mvn -q exec:java -Dexec.mainClass=org.prototype.opensearch.ha.OpenSearchHaRestServer
# open http://localhost:8080/value?index=prototype_docs&id=1
```

## Test

```bash
mvn test
```
