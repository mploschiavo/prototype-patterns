# C# Ollama MCP Server (Single Node)

MCP-style JSON-RPC server exposing `rag.search` and `agent.answer` tools over `POST /mcp`.

## Infra

Use: `integration-prototypes/infra/ollama-single/docker-compose.yml` or `integration-prototypes/infra/ollama-single/k8s`

## Run

```bash
OLLAMA_URL='http://localhost:11434' OLLAMA_MODEL='tinyllama' dotnet run --project src/OllamaMcpServer/OllamaMcpServer.csproj
```

## Test

```bash
dotnet test tests/OllamaMcpServer.Tests/OllamaMcpServer.Tests.csproj
```
