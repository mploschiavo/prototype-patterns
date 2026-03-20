FROM eclipse-temurin:21-jdk AS build
WORKDIR /app
COPY src ./src
RUN mkdir -p out && find src/main/java -name "*.java" > sources.txt && javac --release 21 -d out @sources.txt

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/out ./out
ENV PORT=8080
EXPOSE 8080
CMD ["java", "-cp", "out", "org.prototype.services.helloworldlogger.HelloWorldLoggerServer"]
