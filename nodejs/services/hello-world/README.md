# Node.js Hello World Service

Node HTTP service returning `hello world` on `GET /`.

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
