const test = require("node:test");
const assert = require("node:assert/strict");

const { fetchValue } = require("./app");

test("fetchValue parses json payload", async () => {
  const value = await fetchValue("demo:key", () => ({
    async get() {
      return '{"id":1,"value":"hello redis single"}';
    },
  }));

  assert.deepEqual(value, { id: 1, value: "hello redis single" });
});

test("fetchValue returns null when key missing", async () => {
  const value = await fetchValue("missing:key", () => ({
    async get() {
      return null;
    },
  }));

  assert.equal(value, null);
});
