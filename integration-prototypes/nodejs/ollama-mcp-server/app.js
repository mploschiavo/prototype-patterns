const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");

const ollamaUrl = process.env.OLLAMA_URL || "http://localhost:11434";
const ollamaModel = process.env.OLLAMA_MODEL || "tinyllama";
const ragDocsPath = process.env.RAG_DOCS_PATH || path.join(__dirname, "rag-documents.json");

function loadDocuments(path = ragDocsPath) {
  return JSON.parse(fs.readFileSync(path, "utf8"));
}

function ragSearch(query, docs, limit = 3) {
  const terms = query
    .split(/\s+/)
    .map((value) => value.trim().toLowerCase())
    .filter((value) => value.length > 0);

  const score = (doc) => terms.reduce((count, term) => count + (doc.text.toLowerCase().includes(term) ? 1 : 0), 0);

  return docs
    .slice()
    .sort((left, right) => score(right) - score(left))
    .filter((doc) => score(doc) > 0)
    .slice(0, limit);
}

async function callOllama(question, context, requestFn = null) {
  const contextBlock = context.length > 0 ? context.map((entry) => `- ${entry.text}`).join("\n") : "- No context found";
  const prompt = `Use context to answer.\nContext:\n${contextBlock}\n\nQuestion: ${question}`;

  if (requestFn) {
    return requestFn(question, context);
  }

  const response = await fetch(`${ollamaUrl}/api/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ model: ollamaModel, prompt, stream: false }),
  });

  if (!response.ok) {
    throw new Error(`ollama request failed: ${response.status}`);
  }

  const payload = await response.json();
  return payload.response || "";
}

async function handleRpc(request, docs, ollamaFn = null) {
  const method = request.method;
  const id = request.id;
  const params = request.params || {};

  if (method === "initialize") {
    return { jsonrpc: "2.0", id, result: { serverName: "nodejs-ollama-mcp", version: "0.1.0" } };
  }

  if (method === "tools/list") {
    return {
      jsonrpc: "2.0",
      id,
      result: {
        tools: [
          { name: "rag.search", description: "Search seeded RAG documents" },
          { name: "agent.answer", description: "Answer a question using RAG + Ollama" },
        ],
      },
    };
  }

  if (method === "tools/call") {
    const name = params.name;
    const args = params.arguments || {};

    if (name === "rag.search") {
      const hits = ragSearch(args.query || "", docs);
      return { jsonrpc: "2.0", id, result: { content: [{ type: "json", json: hits }] } };
    }

    if (name === "agent.answer") {
      const question = args.question || "";
      const hits = ragSearch(question, docs);
      const answer = ollamaFn ? await ollamaFn(question, hits) : await callOllama(question, hits);
      return {
        jsonrpc: "2.0",
        id,
        result: {
          content: [{ type: "text", text: answer }],
          context: hits,
        },
      };
    }
  }

  return { jsonrpc: "2.0", id, error: { code: -32601, message: "Method not found" } };
}

function createServer(documents = loadDocuments()) {
  return http.createServer(async (req, res) => {
    if (req.method !== "POST" || req.url !== "/mcp") {
      res.writeHead(404, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "not found" }));
      return;
    }

    let rawBody = "";
    req.on("data", (chunk) => {
      rawBody += chunk.toString("utf8");
    });

    req.on("end", async () => {
      const request = JSON.parse(rawBody || "{}");
      const response = await handleRpc(request, documents);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify(response));
    });
  });
}

async function main() {
  const port = Number(process.env.PORT || 8090);
  const server = createServer();
  server.listen(port, () => {
    // eslint-disable-next-line no-console
    console.log(`nodejs-ollama-mcp listening on :${port}`);
  });
}

module.exports = { loadDocuments, ragSearch, callOllama, handleRpc, createServer };

if (require.main === module) {
  main().catch((error) => {
    // eslint-disable-next-line no-console
    console.error(error);
    process.exit(1);
  });
}
