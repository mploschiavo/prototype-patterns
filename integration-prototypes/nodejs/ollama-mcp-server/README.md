# Node.js Ollama MCP Server (Single Node)

MCP-style JSON-RPC server exposing `rag.search` and `agent.answer` tools over `POST /mcp`.

## Infra

Use: `integration-prototypes/infra/ollama-single/docker-compose.yml` or `integration-prototypes/infra/ollama-single/k8s`

## Run

```bash
npm install
OLLAMA_URL='http://localhost:11434' OLLAMA_MODEL='tinyllama' node app.js
```

## Test

```bash
npm test
```
