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
else
  skip_suite "Python Patterns" "python3 not installed"
  skip_suite "Python Hello World Service" "python3 not installed"
  skip_suite "Python Hello World Logger Service" "python3 not installed"
fi

# Node.js
if has_cmd node && has_cmd npm; then
  run_suite "Node.js Patterns" "nodejs/patterns" "npm test --silent"
  run_suite "Node.js Hello World Service" "nodejs/services/hello-world" "npm test --silent"
  run_suite "Node.js Hello World Logger Service" "nodejs/services/hello-world-logger" "npm test --silent"
else
  skip_suite "Node.js Patterns" "node and/or npm not installed"
  skip_suite "Node.js Hello World Service" "node and/or npm not installed"
  skip_suite "Node.js Hello World Logger Service" "node and/or npm not installed"
fi

# Java
if has_cmd java && has_cmd javac; then
  run_suite "Java Patterns" "java/patterns" "./scripts/test.sh"
  run_suite "Java Hello World Service" "java/services/hello-world" "./scripts/test.sh"
  run_suite "Java Hello World Logger Service" "java/services/hello-world-logger" "./scripts/test.sh"
else
  skip_suite "Java Patterns" "java and/or javac not installed"
  skip_suite "Java Hello World Service" "java and/or javac not installed"
  skip_suite "Java Hello World Logger Service" "java and/or javac not installed"
fi

# C#
if has_cmd dotnet; then
  run_suite "C# Patterns" "csharp/patterns" "dotnet test PrototypePatterns.sln"
  run_suite "C# Hello World Service" "csharp/services/hello-world" "dotnet test HelloWorldService.sln"
  run_suite "C# Hello World Logger Service" "csharp/services/hello-world-logger" "dotnet test HelloWorldLoggerService.sln"
else
  skip_suite "C# Patterns" "dotnet not installed"
  skip_suite "C# Hello World Service" "dotnet not installed"
  skip_suite "C# Hello World Logger Service" "dotnet not installed"
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
