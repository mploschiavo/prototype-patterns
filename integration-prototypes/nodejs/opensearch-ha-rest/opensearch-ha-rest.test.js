const test = require("node:test");
const assert = require("node:assert/strict");

const { parseNodes, fetchValue } = require("./app");

test("parseNodes extracts all urls", () => {
  assert.deepEqual(parseNodes("http://localhost:9200,http://localhost:9201"), [
    "http://localhost:9200",
    "http://localhost:9201",
  ]);
});

test("fetchValue fails over to second node", async () => {
  const calls = [];

  const value = await fetchValue(
    "prototype_docs",
    "1",
    "http://localhost:9200,http://localhost:9201",
    async (url) => {
      calls.push(url);
      if (url.startsWith("http://localhost:9200")) {
        throw new Error("node down");
      }

      return {
        status: 200,
        ok: true,
        async json() {
          return { found: true, _source: { message: "hello opensearch ha" } };
        },
      };
    },
  );

  assert.equal(value, "hello opensearch ha");
  assert.equal(calls.length, 2);
});
