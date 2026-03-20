# Node.js Kafka Producer/Consumer (HA Cluster)

## Infra

Use: `integration-prototypes/infra/kafka-ha/docker-compose.yml`

## Run

```bash
npm install
KAFKA_BOOTSTRAP_SERVERS=localhost:9092,localhost:9094,localhost:9096 KAFKA_TOPIC=prototype-topic-ha node producer.js
KAFKA_BOOTSTRAP_SERVERS=localhost:9092,localhost:9094,localhost:9096 KAFKA_TOPIC=prototype-topic-ha node consumer.js
```

## Test

```bash
npm test
```
