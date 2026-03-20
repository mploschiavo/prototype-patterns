# Python Hello World Logger Service

`http.server` service returning `hello world with logger` on `GET /` and writing a log event.

## Test

```bash
python3 -m unittest discover -s tests -v
```

## Run Locally

```bash
python3 src/app.py
```

## Deploy Scenarios

- Docker: `./infra/docker/run.sh`
- Docker Compose: `docker compose -f infra/compose/docker-compose.yml up --build`
- Kubernetes: `kubectl apply -k infra/k8s`
