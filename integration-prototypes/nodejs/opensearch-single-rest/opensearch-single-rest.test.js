const test = require("node:test");
const assert = require("node:assert/strict");

const { fetchValue } = require("./app");

test("fetchValue reads message from source", async () => {
  const value = await fetchValue("prototype_docs", "1", undefined, async () => ({
    status: 200,
    ok: true,
    async json() {
      return { found: true, _source: { message: "hello opensearch single" } };
    },
  }));

  assert.equal(value, "hello opensearch single");
});

test("fetchValue returns null when not found", async () => {
  const value = await fetchValue("prototype_docs", "404", undefined, async () => ({
    status: 200,
    ok: true,
    async json() {
      return { found: false };
    },
  }));

  assert.equal(value, null);
});
