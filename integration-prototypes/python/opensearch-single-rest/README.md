# Python REST + OpenSearch (Single Node)

REST service returning JSON value from one OpenSearch document.

## Infra

Use: `integration-prototypes/infra/opensearch-single/docker-compose.yml`

## Run

```bash
export OPENSEARCH_URL='http://localhost:9200'
python3 app.py
# open http://localhost:8080/value?index=prototype_docs&id=1
```

## Test

```bash
python3 -m unittest -v test_opensearch_single_rest.py
```
