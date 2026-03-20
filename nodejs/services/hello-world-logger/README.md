# Node.js Hello World Logger Service

Node HTTP service returning `hello world with logger` on `GET /` and writing a log event.

## Test

```bash
npm test
```

## Run Locally

```bash
npm start
```

## Deploy Scenarios

- Docker: `./infra/docker/run.sh`
- Docker Compose: `docker compose -f infra/compose/docker-compose.yml up --build`
- Kubernetes: `kubectl apply -k infra/k8s`
