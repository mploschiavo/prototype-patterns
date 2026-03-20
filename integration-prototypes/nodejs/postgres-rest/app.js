const http = require("node:http");
const { URL } = require("node:url");
const { Pool } = require("pg");

const connectionString = process.env.PG_CONNECTION_STRING || "postgresql://prototype_user:prototype_pass@localhost:5432/prototype_db";
const pool = new Pool({ connectionString });

async function fetchItem(id, queryFn = null) {
  const runner = queryFn || ((text, params) => pool.query(text, params));
  const result = await runner("SELECT id, name, description FROM demo_items WHERE id = $1", [id]);
  if (result.rows.length === 0) {
    return null;
  }
  return result.rows[0];
}

function createServer(fetcher = fetchItem) {
  return http.createServer(async (req, res) => {
    const url = new URL(req.url, "http://localhost");
    if (url.pathname !== "/item") {
      res.writeHead(404, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "not found" }));
      return;
    }

    const id = Number(url.searchParams.get("id") || "1");
    const item = await fetcher(id);

    if (!item) {
      res.writeHead(404, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "item not found" }));
      return;
    }

    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(item));
  });
}

async function main() {
  const port = Number(process.env.PORT || 8080);
  const server = createServer();
  server.listen(port, () => {
    // eslint-disable-next-line no-console
    console.log(`postgres-rest listening on :${port}`);
  });
}

module.exports = { fetchItem, createServer };

if (require.main === module) {
  main().catch((error) => {
    // eslint-disable-next-line no-console
    console.error(error);
    process.exit(1);
  });
}
