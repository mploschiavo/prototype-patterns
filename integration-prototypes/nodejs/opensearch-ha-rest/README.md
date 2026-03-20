# Node.js REST + OpenSearch (HA Cluster)

## Infra

Use: `integration-prototypes/infra/opensearch-ha/docker-compose.yml`

## Run

```bash
npm install
OPENSEARCH_NODES='http://localhost:9200,http://localhost:9201,http://localhost:9202' node app.js
# open http://localhost:8080/value?index=prototype_docs&id=1
```

## Test

```bash
npm test
```
