from __future__ import annotations

import logging
import os
import time
from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


REQUEST_COUNT = Counter("demo_requests_total", "Total HTTP requests", ["endpoint", "status"])
REQUEST_LATENCY = Histogram("demo_request_duration_seconds", "Request latency", ["endpoint"])


def configure_logging() -> None:
    log_dir = os.getenv("APP_LOG_DIR", "/var/log/demo-app")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "app.log")

    logger = logging.getLogger("demo-app")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    stream = logging.StreamHandler()
    file_handler = logging.FileHandler(log_path)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    stream.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream)
    logger.addHandler(file_handler)


def configure_tracing() -> None:
    endpoint = os.getenv("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "http://localhost:4318/v1/traces")
    provider = TracerProvider(resource=Resource.create({"service.name": "demo-app"}))
    exporter = OTLPSpanExporter(endpoint=endpoint)
    processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)


def create_app() -> Flask:
    configure_logging()
    configure_tracing()
    logger = logging.getLogger("demo-app")
    tracer = trace.get_tracer("demo-app")

    app = Flask(__name__)

    @app.get("/")
    def root():
        start = time.perf_counter()
        with tracer.start_as_current_span("root_handler"):
            logger.info("handling root endpoint")
            response = {"message": "hello observability"}
        duration = time.perf_counter() - start
        REQUEST_COUNT.labels(endpoint="/", status="200").inc()
        REQUEST_LATENCY.labels(endpoint="/").observe(duration)
        return jsonify(response)

    @app.get("/slow")
    def slow():
        start = time.perf_counter()
        with tracer.start_as_current_span("slow_handler"):
            time.sleep(0.6)
            logger.info("handling slow endpoint")
        duration = time.perf_counter() - start
        REQUEST_COUNT.labels(endpoint="/slow", status="200").inc()
        REQUEST_LATENCY.labels(endpoint="/slow").observe(duration)
        return jsonify({"message": "slow path", "duration_seconds": round(duration, 3)})

    @app.get("/error")
    def error():
        start = time.perf_counter()
        with tracer.start_as_current_span("error_handler"):
            logger.error("intentional error path triggered")
        duration = time.perf_counter() - start
        REQUEST_COUNT.labels(endpoint="/error", status="500").inc()
        REQUEST_LATENCY.labels(endpoint="/error").observe(duration)
        return jsonify({"error": "intentional failure"}), 500

    @app.get("/metrics")
    def metrics():
        return generate_latest(), 200, {"Content-Type": "text/plain; version=0.0.4; charset=utf-8"}

    return app


def main() -> None:
    app = create_app()
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
