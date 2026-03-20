#!/usr/bin/env bash
set -euo pipefail

docker build -t prototype/nodejs-hello-world-logger:latest ../../
docker run --rm -p 8080:8080 prototype/nodejs-hello-world-logger:latest
