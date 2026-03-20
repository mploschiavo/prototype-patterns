#!/usr/bin/env bash
set -euo pipefail

docker build -t prototype/java-hello-world-logger:latest ../../
docker run --rm -p 8080:8080 prototype/java-hello-world-logger:latest
