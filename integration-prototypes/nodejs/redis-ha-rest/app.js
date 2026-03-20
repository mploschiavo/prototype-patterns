const http = require("node:http");
const { URL } = require("node:url");
const { createCluster } = require("redis");

const redisClusterNodes = process.env.REDIS_CLUSTER_NODES || "localhost:6379,localhost:6380,localhost:6381";

function parseRootNodes(nodes) {
  return nodes.split(",").map((entry) => ({ url: `redis://${entry.trim()}` }));
}

async function fetchValue(key = "demo:key", nodes = redisClusterNodes, clusterFactory = null) {
  const cluster = clusterFactory ? clusterFactory() : createCluster({ rootNodes: parseRootNodes(nodes) });
  if (!clusterFactory) {
    await cluster.connect();
  }

  try {
    const raw = await cluster.get(key);
    if (raw === null) {
      return null;
    }

    try {
      return JSON.parse(raw);
    } catch {
      return raw;
    }
  } finally {
    if (!clusterFactory) {
      await cluster.disconnect();
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
    console.log(`redis-ha-rest listening on :${port}`);
  });
}

module.exports = { parseRootNodes, fetchValue, createServer };

if (require.main === module) {
  main().catch((error) => {
    // eslint-disable-next-line no-console
    console.error(error);
    process.exit(1);
  });
}
