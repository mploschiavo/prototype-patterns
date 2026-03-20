#!/usr/bin/env sh
set -eu
mode="${KAFKA_CLIENT_MODE:-producer}"
if [ "$mode" = "consumer" ]; then
  exec dotnet "$CSHARP_DLL" consume
fi
exec dotnet "$CSHARP_DLL"
