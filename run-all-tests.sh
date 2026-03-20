#!/usr/bin/env bash
set -uo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

passed=0
failed=0
skipped=0

run_suite() {
  local name="$1"
  local workdir="$2"
  local command="$3"

  echo
  echo "==> $name"
  (cd "$ROOT_DIR/$workdir" && bash -lc "$command")
  local rc=$?

  if [[ $rc -eq 0 ]]; then
    echo "PASS: $name"
    passed=$((passed + 1))
  else
    echo "FAIL: $name (exit code $rc)"
    failed=$((failed + 1))
  fi
}

skip_suite() {
  local name="$1"
  local reason="$2"
  echo
  echo "==> $name"
  echo "SKIP: $reason"
  skipped=$((skipped + 1))
}

has_cmd() {
  command -v "$1" >/dev/null 2>&1
}

echo "Running repository test suites..."
echo "Root: $ROOT_DIR"

# Python
if has_cmd python3; then
  run_suite "Python Patterns" "python/patterns" "PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_patterns_unittest.py' -v"
  run_suite "Python Hello World Service" "python/services/hello-world" "python3 -m unittest discover -s tests -v"
  run_suite "Python Hello World Logger Service" "python/services/hello-world-logger" "python3 -m unittest discover -s tests -v"
  run_suite "Python Integration Kafka Single" "integration-prototypes/python/kafka-single" "python3 -m unittest -v test_kafka_single.py"
  run_suite "Python Integration Kafka HA" "integration-prototypes/python/kafka-ha" "python3 -m unittest -v test_kafka_ha.py"
  run_suite "Python Integration Postgres REST" "integration-prototypes/python/postgres-rest" "python3 -m unittest -v test_postgres_rest.py"
  run_suite "Python Integration Redis Single REST" "integration-prototypes/python/redis-single-rest" "python3 -m unittest -v test_redis_single_rest.py"
  run_suite "Python Integration Redis HA REST" "integration-prototypes/python/redis-ha-rest" "python3 -m unittest -v test_redis_ha_rest.py"
  run_suite "Python Integration OpenSearch Single REST" "integration-prototypes/python/opensearch-single-rest" "python3 -m unittest -v test_opensearch_single_rest.py"
  run_suite "Python Integration OpenSearch HA REST" "integration-prototypes/python/opensearch-ha-rest" "python3 -m unittest -v test_opensearch_ha_rest.py"
  run_suite "Python Integration Ollama MCP Server" "integration-prototypes/python/ollama-mcp-server" "python3 -m unittest -v test_ollama_mcp_server.py"
  run_suite "Integration Client Packaging" "integration-prototypes" "python3 -m unittest -v tests/test_client_packaging.py"
  run_suite "Python Cloud K8s Setup Scripts" "examples/cloud-k8s-setup" "PYTHONPATH=. python3 -m unittest -v tests/test_cloud_setup.py"
else
  skip_suite "Python Patterns" "python3 not installed"
  skip_suite "Python Hello World Service" "python3 not installed"
  skip_suite "Python Hello World Logger Service" "python3 not installed"
  skip_suite "Python Integration Kafka Single" "python3 not installed"
  skip_suite "Python Integration Kafka HA" "python3 not installed"
  skip_suite "Python Integration Postgres REST" "python3 not installed"
  skip_suite "Python Integration Redis Single REST" "python3 not installed"
  skip_suite "Python Integration Redis HA REST" "python3 not installed"
  skip_suite "Python Integration OpenSearch Single REST" "python3 not installed"
  skip_suite "Python Integration OpenSearch HA REST" "python3 not installed"
  skip_suite "Python Integration Ollama MCP Server" "python3 not installed"
  skip_suite "Integration Client Packaging" "python3 not installed"
  skip_suite "Python Cloud K8s Setup Scripts" "python3 not installed"
fi

# Node.js
if has_cmd node && has_cmd npm; then
  run_suite "Node.js Patterns" "nodejs/patterns" "npm test --silent"
  run_suite "Node.js Hello World Service" "nodejs/services/hello-world" "npm test --silent"
  run_suite "Node.js Hello World Logger Service" "nodejs/services/hello-world-logger" "npm test --silent"
  run_suite "Node.js Integration Kafka Single" "integration-prototypes/nodejs/kafka-single" "npm install --silent && npm test --silent"
  run_suite "Node.js Integration Kafka HA" "integration-prototypes/nodejs/kafka-ha" "npm install --silent && npm test --silent"
  run_suite "Node.js Integration Postgres REST" "integration-prototypes/nodejs/postgres-rest" "npm install --silent && npm test --silent"
  run_suite "Node.js Integration Redis Single REST" "integration-prototypes/nodejs/redis-single-rest" "npm install --silent && npm test --silent"
  run_suite "Node.js Integration Redis HA REST" "integration-prototypes/nodejs/redis-ha-rest" "npm install --silent && npm test --silent"
  run_suite "Node.js Integration OpenSearch Single REST" "integration-prototypes/nodejs/opensearch-single-rest" "npm install --silent && npm test --silent"
  run_suite "Node.js Integration OpenSearch HA REST" "integration-prototypes/nodejs/opensearch-ha-rest" "npm install --silent && npm test --silent"
  run_suite "Node.js Integration Ollama MCP Server" "integration-prototypes/nodejs/ollama-mcp-server" "npm install --silent && npm test --silent"
else
  skip_suite "Node.js Patterns" "node and/or npm not installed"
  skip_suite "Node.js Hello World Service" "node and/or npm not installed"
  skip_suite "Node.js Hello World Logger Service" "node and/or npm not installed"
  skip_suite "Node.js Integration Kafka Single" "node and/or npm not installed"
  skip_suite "Node.js Integration Kafka HA" "node and/or npm not installed"
  skip_suite "Node.js Integration Postgres REST" "node and/or npm not installed"
  skip_suite "Node.js Integration Redis Single REST" "node and/or npm not installed"
  skip_suite "Node.js Integration Redis HA REST" "node and/or npm not installed"
  skip_suite "Node.js Integration OpenSearch Single REST" "node and/or npm not installed"
  skip_suite "Node.js Integration OpenSearch HA REST" "node and/or npm not installed"
  skip_suite "Node.js Integration Ollama MCP Server" "node and/or npm not installed"
fi

# Java
if has_cmd java && has_cmd javac; then
  run_suite "Java Patterns" "java/patterns" "./scripts/test.sh"
  run_suite "Java Hello World Service" "java/services/hello-world" "./scripts/test.sh"
  run_suite "Java Hello World Logger Service" "java/services/hello-world-logger" "./scripts/test.sh"
  if has_cmd mvn; then
    run_suite "Java Integration Kafka Single" "integration-prototypes/java/kafka-single" "mvn -q test"
    run_suite "Java Integration Kafka HA" "integration-prototypes/java/kafka-ha" "mvn -q test"
    run_suite "Java Integration Postgres REST" "integration-prototypes/java/postgres-rest" "mvn -q test"
    run_suite "Java Integration Redis Single REST" "integration-prototypes/java/redis-single-rest" "mvn -q test"
    run_suite "Java Integration Redis HA REST" "integration-prototypes/java/redis-ha-rest" "mvn -q test"
    run_suite "Java Integration OpenSearch Single REST" "integration-prototypes/java/opensearch-single-rest" "mvn -q test"
    run_suite "Java Integration OpenSearch HA REST" "integration-prototypes/java/opensearch-ha-rest" "mvn -q test"
    run_suite "Java Integration Ollama MCP Server" "integration-prototypes/java/ollama-mcp-server" "mvn -q test"
  else
    skip_suite "Java Integration Kafka Single" "maven not installed"
    skip_suite "Java Integration Kafka HA" "maven not installed"
    skip_suite "Java Integration Postgres REST" "maven not installed"
    skip_suite "Java Integration Redis Single REST" "maven not installed"
    skip_suite "Java Integration Redis HA REST" "maven not installed"
    skip_suite "Java Integration OpenSearch Single REST" "maven not installed"
    skip_suite "Java Integration OpenSearch HA REST" "maven not installed"
    skip_suite "Java Integration Ollama MCP Server" "maven not installed"
  fi
else
  skip_suite "Java Patterns" "java and/or javac not installed"
  skip_suite "Java Hello World Service" "java and/or javac not installed"
  skip_suite "Java Hello World Logger Service" "java and/or javac not installed"
  skip_suite "Java Integration Kafka Single" "java and/or javac not installed"
  skip_suite "Java Integration Kafka HA" "java and/or javac not installed"
  skip_suite "Java Integration Postgres REST" "java and/or javac not installed"
  skip_suite "Java Integration Redis Single REST" "java and/or javac not installed"
  skip_suite "Java Integration Redis HA REST" "java and/or javac not installed"
  skip_suite "Java Integration OpenSearch Single REST" "java and/or javac not installed"
  skip_suite "Java Integration OpenSearch HA REST" "java and/or javac not installed"
  skip_suite "Java Integration Ollama MCP Server" "java and/or javac not installed"
fi

# C#
if has_cmd dotnet; then
  run_suite "C# Patterns" "csharp/patterns" "dotnet test PrototypePatterns.sln"
  run_suite "C# Hello World Service" "csharp/services/hello-world" "dotnet test HelloWorldService.sln"
  run_suite "C# Hello World Logger Service" "csharp/services/hello-world-logger" "dotnet test HelloWorldLoggerService.sln"
  run_suite "C# Integration Kafka Single" "integration-prototypes/csharp/kafka-single" "dotnet test tests/KafkaSingleClients.Tests/KafkaSingleClients.Tests.csproj"
  run_suite "C# Integration Kafka HA" "integration-prototypes/csharp/kafka-ha" "dotnet test tests/KafkaHaClients.Tests/KafkaHaClients.Tests.csproj"
  run_suite "C# Integration Postgres REST" "integration-prototypes/csharp/postgres-rest" "dotnet test tests/PostgresRestService.Tests/PostgresRestService.Tests.csproj"
  run_suite "C# Integration Redis Single REST" "integration-prototypes/csharp/redis-single-rest" "dotnet test tests/RedisSingleRestService.Tests/RedisSingleRestService.Tests.csproj"
  run_suite "C# Integration Redis HA REST" "integration-prototypes/csharp/redis-ha-rest" "dotnet test tests/RedisHaRestService.Tests/RedisHaRestService.Tests.csproj"
  run_suite "C# Integration OpenSearch Single REST" "integration-prototypes/csharp/opensearch-single-rest" "dotnet test tests/OpenSearchSingleRestService.Tests/OpenSearchSingleRestService.Tests.csproj"
  run_suite "C# Integration OpenSearch HA REST" "integration-prototypes/csharp/opensearch-ha-rest" "dotnet test tests/OpenSearchHaRestService.Tests/OpenSearchHaRestService.Tests.csproj"
  run_suite "C# Integration Ollama MCP Server" "integration-prototypes/csharp/ollama-mcp-server" "dotnet test tests/OllamaMcpServer.Tests/OllamaMcpServer.Tests.csproj"
else
  skip_suite "C# Patterns" "dotnet not installed"
  skip_suite "C# Hello World Service" "dotnet not installed"
  skip_suite "C# Hello World Logger Service" "dotnet not installed"
  skip_suite "C# Integration Kafka Single" "dotnet not installed"
  skip_suite "C# Integration Kafka HA" "dotnet not installed"
  skip_suite "C# Integration Postgres REST" "dotnet not installed"
  skip_suite "C# Integration Redis Single REST" "dotnet not installed"
  skip_suite "C# Integration Redis HA REST" "dotnet not installed"
  skip_suite "C# Integration OpenSearch Single REST" "dotnet not installed"
  skip_suite "C# Integration OpenSearch HA REST" "dotnet not installed"
  skip_suite "C# Integration Ollama MCP Server" "dotnet not installed"
fi

echo
echo "=============================="
echo "Summary:"
echo "  Passed:  $passed"
echo "  Failed:  $failed"
echo "  Skipped: $skipped"
echo "=============================="

if [[ $failed -gt 0 ]]; then
  exit 1
fi

exit 0
