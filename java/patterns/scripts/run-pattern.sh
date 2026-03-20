#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$ROOT_DIR/build/runner"
CLASSES_DIR="$BUILD_DIR/classes"

rm -rf "$BUILD_DIR"
mkdir -p "$CLASSES_DIR"

find "$ROOT_DIR/src/main/java" -name "*.java" > "$BUILD_DIR/sources.txt"
javac --release 21 -d "$CLASSES_DIR" @"$BUILD_DIR/sources.txt"
java -cp "$CLASSES_DIR" org.prototypepatterns.PatternCli "$@"
