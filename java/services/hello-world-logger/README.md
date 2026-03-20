# Java Hello World Logger Service

JDK `HttpServer` service returning `hello world with logger` on `GET /` and writing a log event.

## Test

```bash
./scripts/test.sh
```

## Run Locally

```bash
mkdir -p build/classes
find src/main/java -name "*.java" > build/sources.txt
javac --release 21 -d build/classes @build/sources.txt
java -cp build/classes org.prototype.services.helloworldlogger.HelloWorldLoggerServer
```

## Deploy Scenarios

- Docker: `./infra/docker/run.sh`
- Docker Compose: `docker compose -f infra/compose/docker-compose.yml up --build`
- Kubernetes: `kubectl apply -k infra/k8s`
