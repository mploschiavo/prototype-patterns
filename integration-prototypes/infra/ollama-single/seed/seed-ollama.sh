#!/bin/sh
set -e

until ollama list >/dev/null 2>&1; do
  sleep 2
done

ollama pull tinyllama

echo "seeded model tinyllama"
