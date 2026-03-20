# Hello World Observability Stack (Local + MicroK8s)

This folder demonstrates a full open-source observability flow with a small app and correlated telemetry.

## Stack Components

- Grafana (dashboards and correlation)
- Prometheus (metrics)
- Loki (logs)
- Tempo (traces)
- OpenTelemetry Collector (trace + log routing)
- Demo app with normal, slow, and error paths

## Health Model

- Docker Compose services define container `healthcheck` probes.
- MicroK8s deployments include `startupProbe`, `readinessProbe`, and `livenessProbe`.

## Prerequisites

- Docker + Docker Compose
- Python 3 (for app tests)
- For Kubernetes mode: MicroK8s with local registry enabled

## Local Run (Docker Compose)

From `observability-demo/hello-world-stack`:

```bash
./docker/run.sh
```

Endpoints:

- Demo app: `http://localhost:8088`
- Grafana: `http://localhost:3000` (`admin` / `admin`)
- Prometheus: `http://localhost:9090`
- Loki API: `http://localhost:3100`
- Tempo API: `http://localhost:3200`

### Generate Demo Traffic

```bash
curl -s http://localhost:8088/
curl -s http://localhost:8088/slow
curl -i http://localhost:8088/error
```

### Validate Telemetry Quickly

```bash
curl -s http://localhost:8088/metrics | head
curl -s http://localhost:9090/-/ready
curl -s http://localhost:3100/ready
curl -s http://localhost:3200/ready
```

## MicroK8s Run

From `observability-demo/hello-world-stack`:

1. Build and push demo app image to MicroK8s local registry:

```bash
./k8s/build-and-push-microk8s.sh
```

2. Deploy stack:

```bash
microk8s kubectl apply -k k8s
```

3. Check rollout:

```bash
microk8s kubectl get pods -n observability-demo
```

4. Access key UIs:

- Grafana NodePort: `http://<node-ip>:30030`
- Prometheus NodePort: `http://<node-ip>:30090`
- Demo app NodePort: `http://<node-ip>:30088`

Optional local access via port-forward:

```bash
microk8s kubectl port-forward -n observability-demo service/grafana 3000:3000
microk8s kubectl port-forward -n observability-demo service/prometheus 9090:9090
microk8s kubectl port-forward -n observability-demo service/demo-app 8088:8080
```

## Demo Flow (Suggested Walkthrough)

1. Send traffic to `/`, `/slow`, and `/error`.
2. In Grafana, open Prometheus metrics and check request counters/latency.
3. Pivot to Loki logs for the same period.
4. Open Tempo traces for slow/error requests.
5. Show end-to-end correlation from metrics -> logs -> traces.

## Cleanup

Local:

```bash
docker compose -f compose/docker-compose.yml down -v
```

MicroK8s:

```bash
microk8s kubectl delete -k k8s --ignore-not-found
```

## App Test

```bash
python3 -m unittest -v app/test_app.py
```
