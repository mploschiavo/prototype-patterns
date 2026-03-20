const test = require("node:test");
const assert = require("node:assert/strict");

const { parseRootNodes, fetchValue } = require("./app");

test("parseRootNodes", () => {
  assert.deepEqual(parseRootNodes("localhost:6379,localhost:6380"), [
    { url: "redis://localhost:6379" },
    { url: "redis://localhost:6380" },
  ]);
});

test("fetchValue parses json payload", async () => {
  const value = await fetchValue("demo:key", undefined, () => ({
    async get() {
      return '{"id":1,"value":"hello redis ha"}';
    },
  }));

  assert.deepEqual(value, { id: 1, value: "hello redis ha" });
});
