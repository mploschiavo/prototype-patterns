# Hello World Observability Stack (Local + MicroK8s)

Stack components:

- Grafana (dashboards)
- Prometheus (metrics)
- Loki (logs)
- Tempo (traces)
- OpenTelemetry Collector (telemetry routing)
- Demo app with intentional normal/slow/error paths

## Local Run (Docker Compose)

```bash
./docker/run.sh
```

Endpoints:

- Demo app: `http://localhost:8088`
- Grafana: `http://localhost:3000` (admin/admin)
- Prometheus: `http://localhost:9090`
- Loki API: `http://localhost:3100`
- Tempo API: `http://localhost:3200`

## MicroK8s Run

1. Build and push app image to MicroK8s local registry:

```bash
./k8s/build-and-push-microk8s.sh
```

2. Deploy stack:

```bash
microk8s kubectl apply -k k8s
```

3. Access key UIs:

- Grafana NodePort: `http://<node-ip>:30030`
- Prometheus NodePort: `http://<node-ip>:30090`
- Demo app NodePort: `http://<node-ip>:30088`

## Demo Flow

1. Hit `/`, `/slow`, and `/error` on the demo app.
2. View metrics in Prometheus and Grafana.
3. Inspect logs in Loki datasource.
4. Inspect traces in Tempo datasource.
5. Correlate a slow/error request across all three telemetry pillars.

## App Test

```bash
python3 -m unittest -v app/test_app.py
```
