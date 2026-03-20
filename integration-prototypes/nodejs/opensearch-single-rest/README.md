# Node.js REST + OpenSearch (Single Node)

## Infra

Use: `integration-prototypes/infra/opensearch-single/docker-compose.yml`

## Run

```bash
npm install
OPENSEARCH_URL='http://localhost:9200' node app.js
# open http://localhost:8080/value?index=prototype_docs&id=1
```

## Test

```bash
npm test
```
