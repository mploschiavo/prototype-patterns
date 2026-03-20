# Python REST + OpenSearch (HA Cluster)

REST service returning JSON value from one OpenSearch document using multi-node failover.

## Infra

Use: `integration-prototypes/infra/opensearch-ha/docker-compose.yml`

## Run

```bash
export OPENSEARCH_NODES='http://localhost:9200,http://localhost:9201,http://localhost:9202'
python3 app.py
# open http://localhost:8080/value?index=prototype_docs&id=1
```

## Test

```bash
python3 -m unittest -v test_opensearch_ha_rest.py
```
