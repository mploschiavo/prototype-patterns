#!/bin/sh
set -e

until curl -s http://opensearch-ha-1:9200/_cluster/health >/dev/null; do
  sleep 2
done

curl -s -X PUT "http://opensearch-ha-1:9200/prototype_docs" \
  -H 'Content-Type: application/json' \
  -d '{"settings":{"number_of_shards":1,"number_of_replicas":1}}' >/dev/null || true

curl -s -X PUT "http://opensearch-ha-1:9200/prototype_docs/_doc/1?refresh=true" \
  -H 'Content-Type: application/json' \
  -d '{"message":"hello opensearch ha","source":"seed-ha"}' >/dev/null

echo "opensearch ha seed complete"
