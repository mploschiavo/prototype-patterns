FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /workspace
COPY pom.xml ./
COPY src ./src
RUN mvn -q -DskipTests package dependency:copy-dependencies
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /workspace/target/classes ./classes
COPY --from=build /workspace/target/dependency ./dependency
ENV PORT=8080
EXPOSE 8080
CMD ["java", "-cp", "/app/classes:/app/dependency/*", "org.prototype.opensearch.single.OpenSearchSingleRestServer"]
