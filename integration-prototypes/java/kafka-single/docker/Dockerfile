FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /workspace
COPY pom.xml ./
COPY src ./src
RUN mvn -q -DskipTests package dependency:copy-dependencies
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /workspace/target/classes ./classes
COPY --from=build /workspace/target/dependency ./dependency
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENV KAFKA_CLIENT_MODE=producer
ENV JAVA_PRODUCER_CLASS=org.prototype.kafka.single.ProducerClient
ENV JAVA_CONSUMER_CLASS=org.prototype.kafka.single.ConsumerClient
ENTRYPOINT ["/entrypoint.sh"]
