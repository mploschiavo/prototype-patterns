# Node.js Kafka Producer/Consumer (Single Node)

## Infra

Use: `integration-prototypes/infra/kafka-single/docker-compose.yml`

## Run

```bash
npm install
KAFKA_BOOTSTRAP_SERVERS=localhost:9092 KAFKA_TOPIC=prototype-topic node producer.js
KAFKA_BOOTSTRAP_SERVERS=localhost:9092 KAFKA_TOPIC=prototype-topic node consumer.js
```

## Test

```bash
npm test
```
