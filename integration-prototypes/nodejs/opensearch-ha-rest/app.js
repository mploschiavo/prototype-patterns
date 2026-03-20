const http = require("node:http");
const { URL } = require("node:url");

const opensearchNodes = process.env.OPENSEARCH_NODES || "http://localhost:9200,http://localhost:9201,http://localhost:9202";

function parseNodes(nodes) {
  return nodes
    .split(",")
    .map((node) => node.trim())
    .filter((node) => node.length > 0);
}

async function fetchValue(index = "prototype_docs", id = "1", nodes = opensearchNodes, getFn = null) {
  const requester = getFn || (async (url) => fetch(url));

  for (const node of parseNodes(nodes)) {
    try {
      const response = await requester(`${node}/${index}/_doc/${id}`);
      if (response.status === 404) {
        return null;
      }

      if (!response.ok) {
        continue;
      }

      const payload = await response.json();
      if (payload.found === false) {
        return null;
      }

      return payload._source?.message ?? null;
    } catch {
      // try next node
    }
  }

  throw new Error("all OpenSearch nodes unreachable");
}

function createServer(fetcher = fetchValue) {
  return http.createServer(async (req, res) => {
    const url = new URL(req.url, "http://localhost");
    if (url.pathname !== "/value") {
      res.writeHead(404, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "not found" }));
      return;
    }

    const index = url.searchParams.get("index") || "prototype_docs";
    const id = url.searchParams.get("id") || "1";

    try {
      const value = await fetcher(index, id);
      if (value === null) {
        res.writeHead(404, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "document not found" }));
        return;
      }

      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ index, id, value }));
    } catch (error) {
      res.writeHead(503, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: error.message }));
    }
  });
}

async function main() {
  const port = Number(process.env.PORT || 8080);
  const server = createServer();
  server.listen(port, () => {
    // eslint-disable-next-line no-console
    console.log(`opensearch-ha-rest listening on :${port}`);
  });
}

module.exports = { parseNodes, fetchValue, createServer };

if (require.main === module) {
  main().catch((error) => {
    // eslint-disable-next-line no-console
    console.error(error);
    process.exit(1);
  });
}
