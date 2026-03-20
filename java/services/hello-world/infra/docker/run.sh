#!/usr/bin/env bash
set -euo pipefail

docker build -t prototype/java-hello-world:latest ../../
docker run --rm -p 8080:8080 prototype/java-hello-world:latest
