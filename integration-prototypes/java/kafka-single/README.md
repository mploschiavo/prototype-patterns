# Java Kafka Producer/Consumer (Single Node)

## Infra

Use: `integration-prototypes/infra/kafka-single/docker-compose.yml`

## Run

```bash
mvn -q -DskipTests package
KAFKA_BOOTSTRAP_SERVERS=localhost:9092 KAFKA_TOPIC=prototype-topic mvn -q exec:java -Dexec.mainClass=org.prototype.kafka.single.ProducerClient
KAFKA_BOOTSTRAP_SERVERS=localhost:9092 KAFKA_TOPIC=prototype-topic mvn -q exec:java -Dexec.mainClass=org.prototype.kafka.single.ConsumerClient
```

## Test

```bash
mvn test
```
