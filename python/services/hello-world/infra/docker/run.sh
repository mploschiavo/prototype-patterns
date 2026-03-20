#!/usr/bin/env bash
set -euo pipefail

docker build -t prototype/python-hello-world:latest ../../
docker run --rm -p 8080:8080 prototype/python-hello-world:latest
