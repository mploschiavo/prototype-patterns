# Python Kafka Producer/Consumer (HA Cluster)

Producer and consumer clients targeting the three-node Kafka cluster.

## Infra

Use: `integration-prototypes/infra/kafka-ha/docker-compose.yml`

## Run

```bash
export KAFKA_BOOTSTRAP_SERVERS=localhost:9092,localhost:9094,localhost:9096
export KAFKA_TOPIC=prototype-topic-ha
python3 producer.py
python3 consumer.py
```

## Test

```bash
python3 -m unittest -v test_kafka_ha.py
```
