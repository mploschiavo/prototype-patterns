const test = require("node:test");
const assert = require("node:assert/strict");
const http = require("node:http");

const { createServer, getMessage } = require("../src/server");

function httpGet(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, (res) => {
      let body = "";
      res.setEncoding("utf8");
      res.on("data", (chunk) => {
        body += chunk;
      });
      res.on("end", () => resolve({ status: res.statusCode, body }));
    });
    req.on("error", reject);
  });
}

test("getMessage returns hello world", () => {
  assert.equal(getMessage(), "hello world");
});

test("server responds with hello world", async () => {
  const server = createServer();
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));

  try {
    const port = server.address().port;
    const response = await httpGet(`http://127.0.0.1:${port}/`);
    assert.equal(response.status, 200);
    assert.equal(response.body, "hello world");
  } finally {
    await new Promise((resolve) => server.close(resolve));
  }
});
