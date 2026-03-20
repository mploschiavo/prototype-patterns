# Python Ollama MCP Server (Single Node)

MCP-style JSON-RPC server exposing `rag.search` and `agent.answer` tools over `POST /mcp`.

## Infra

Use: `integration-prototypes/infra/ollama-single/docker-compose.yml` or `integration-prototypes/infra/ollama-single/k8s`

## Run

```bash
export OLLAMA_URL='http://localhost:11434'
export OLLAMA_MODEL='tinyllama'
python3 app.py
```

## Test

```bash
python3 -m unittest -v test_ollama_mcp_server.py
```
