# Python Kafka Producer/Consumer (Single Node)

Producer and consumer clients targeting the single-node Kafka deployment.

## Infra

Use: `integration-prototypes/infra/kafka-single/docker-compose.yml`

## Run

```bash
export KAFKA_BOOTSTRAP_SERVERS=localhost:9092
export KAFKA_TOPIC=prototype-topic
python3 producer.py
python3 consumer.py
```

## Test

```bash
python3 -m unittest -v test_kafka_single.py
```
