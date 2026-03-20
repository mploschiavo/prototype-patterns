const http = require("node:http");
const { URL } = require("node:url");

const opensearchUrl = process.env.OPENSEARCH_URL || "http://localhost:9200";

async function fetchValue(index = "prototype_docs", id = "1", baseUrl = opensearchUrl, getFn = null) {
  const requester = getFn || (async (url) => fetch(url));
  const response = await requester(`${baseUrl}/${index}/_doc/${id}`);

  if (response.status === 404) {
    return null;
  }

  if (!response.ok) {
    throw new Error(`opensearch request failed: ${response.status}`);
  }

  const payload = await response.json();
  if (payload.found === false) {
    return null;
  }

  return payload._source?.message ?? null;
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
    console.log(`opensearch-single-rest listening on :${port}`);
  });
}

module.exports = { fetchValue, createServer };

if (require.main === module) {
  main().catch((error) => {
    // eslint-disable-next-line no-console
    console.error(error);
    process.exit(1);
  });
}
