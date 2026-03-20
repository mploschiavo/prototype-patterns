# Java Kafka Producer/Consumer (HA Cluster)

## Infra

Use: `integration-prototypes/infra/kafka-ha/docker-compose.yml`

## Run

```bash
mvn -q -DskipTests package
KAFKA_BOOTSTRAP_SERVERS=localhost:9092,localhost:9094,localhost:9096 KAFKA_TOPIC=prototype-topic-ha mvn -q exec:java -Dexec.mainClass=org.prototype.kafka.ha.ProducerClient
KAFKA_BOOTSTRAP_SERVERS=localhost:9092,localhost:9094,localhost:9096 KAFKA_TOPIC=prototype-topic-ha mvn -q exec:java -Dexec.mainClass=org.prototype.kafka.ha.ConsumerClient
```

## Test

```bash
mvn test
```
