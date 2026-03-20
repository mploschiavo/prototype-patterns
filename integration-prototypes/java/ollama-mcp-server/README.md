# Java Ollama MCP Server (Single Node)

MCP-style JSON-RPC server exposing `rag.search` and `agent.answer` tools over `POST /mcp`.

## Infra

Use: `integration-prototypes/infra/ollama-single/docker-compose.yml` or `integration-prototypes/infra/ollama-single/k8s`

## Run

```bash
mvn -q -DskipTests package
OLLAMA_URL='http://localhost:11434' OLLAMA_MODEL='tinyllama' mvn -q exec:java -Dexec.mainClass=org.prototype.ollama.mcp.OllamaMcpServer
```

## Test

```bash
mvn test
```
