const http = require("node:http");
const { URL } = require("node:url");
const { createClient } = require("redis");

const redisUrl = process.env.REDIS_URL || "redis://localhost:6379";

async function fetchValue(key = "demo:key", clientFactory = null) {
  const client = clientFactory ? clientFactory() : createClient({ url: redisUrl });
  if (!clientFactory) {
    await client.connect();
  }

  try {
    const raw = await client.get(key);
    if (raw === null) {
      return null;
    }

    try {
      return JSON.parse(raw);
    } catch {
      return raw;
    }
  } finally {
    if (!clientFactory) {
      await client.disconnect();
    }
  }
}

function createServer(fetcher = fetchValue) {
  return http.createServer(async (req, res) => {
    const url = new URL(req.url, "http://localhost");
    if (url.pathname !== "/value") {
      res.writeHead(404, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "not found" }));
      return;
    }

    const key = url.searchParams.get("key") || "demo:key";
    const value = await fetcher(key);

    if (value === null) {
      res.writeHead(404, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "key not found" }));
      return;
    }

    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ key, value }));
  });
}

async function main() {
  const port = Number(process.env.PORT || 8080);
  const server = createServer();
  server.listen(port, () => {
    // eslint-disable-next-line no-console
    console.log(`redis-single-rest listening on :${port}`);
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
