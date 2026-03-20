"""Python MCP-style server backed by Ollama with simple RAG."""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any, Callable


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "tinyllama")
RAG_DOCS_PATH = Path(os.getenv("RAG_DOCS_PATH", str(Path(__file__).with_name("rag-documents.json"))))


def load_documents(path: Path = RAG_DOCS_PATH) -> list[dict[str, str]]:
    return json.loads(path.read_text(encoding="utf-8"))


def rag_search(query: str, docs: list[dict[str, str]], limit: int = 3) -> list[dict[str, str]]:
    terms = [term.strip().lower() for term in query.split() if term.strip()]

    def score(doc: dict[str, str]) -> int:
        text = doc["text"].lower()
        return sum(1 for term in terms if term in text)

    ranked = sorted(docs, key=score, reverse=True)
    return [doc for doc in ranked if score(doc) > 0][:limit]


def call_ollama(
    question: str,
    context: list[dict[str, str]],
    post_fn: Callable[..., Any] | None = None,
    base_url: str = OLLAMA_URL,
    model: str = OLLAMA_MODEL,
) -> str:
    context_block = "\n".join(f"- {item['text']}" for item in context) if context else "- No context found"
    prompt = f"Use context to answer.\nContext:\n{context_block}\n\nQuestion: {question}"

    if post_fn is None:
        import requests

        response = requests.post(
            f"{base_url}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=30,
        )
        response.raise_for_status()
        payload = response.json()
    else:
        payload = post_fn(question, context)

    return payload.get("response", "")


def handle_rpc(
    request: dict[str, Any],
    docs: list[dict[str, str]],
    ollama_fn: Callable[[str, list[dict[str, str]]], str] | None = None,
) -> dict[str, Any]:
    request_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "initialize":
        return {"jsonrpc": "2.0", "id": request_id, "result": {"serverName": "python-ollama-mcp", "version": "0.1.0"}}

    if method == "tools/list":
        tools = [
            {"name": "rag.search", "description": "Search seeded RAG documents"},
            {"name": "agent.answer", "description": "Answer a question using RAG + Ollama"},
        ]
        return {"jsonrpc": "2.0", "id": request_id, "result": {"tools": tools}}

    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "rag.search":
            query = args.get("query", "")
            hits = rag_search(query, docs)
            return {"jsonrpc": "2.0", "id": request_id, "result": {"content": [{"type": "json", "json": hits}]}}

        if name == "agent.answer":
            question = args.get("question", "")
            hits = rag_search(question, docs)
            responder = ollama_fn or (lambda q, c: call_ollama(q, c))
            answer = responder(question, hits)
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [{"type": "text", "text": answer}],
                    "context": hits,
                },
            }

    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": "Method not found"}}


class McpHandler(BaseHTTPRequestHandler):
    docs = load_documents()

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/mcp":
            self._send(404, {"error": "not found"})
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(content_length).decode("utf-8"))
        response = handle_rpc(payload, self.docs)
        self._send(200, response)

    def _send(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args: object) -> None:
        _ = (fmt, args)


def create_server(port: int) -> HTTPServer:
    return HTTPServer(("0.0.0.0", port), McpHandler)


def main() -> None:
    port = int(os.getenv("PORT", "8090"))
    server = create_server(port)
    print(f"python-ollama-mcp listening on :{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
