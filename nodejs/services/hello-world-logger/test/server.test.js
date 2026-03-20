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

test("getMessage returns hello world with logger and logs", () => {
  const messages = [];
  const logger = {
    info(entry) {
      messages.push(entry);
    },
  };

  assert.equal(getMessage(logger), "hello world with logger");
  assert.equal(messages.length, 1);
  assert.match(messages[0], /Handling hello-world-logger request/);
});

test("server responds with hello world with logger", async () => {
  const logger = { info() {} };
  const server = createServer(logger);
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));

  try {
    const port = server.address().port;
    const response = await httpGet(`http://127.0.0.1:${port}/`);
    assert.equal(response.status, 200);
    assert.equal(response.body, "hello world with logger");
  } finally {
    await new Promise((resolve) => server.close(resolve));
  }
});
