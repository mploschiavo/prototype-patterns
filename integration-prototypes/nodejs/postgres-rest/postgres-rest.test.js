const test = require("node:test");
const assert = require("node:assert/strict");

const { fetchItem } = require("./app");

test("fetchItem returns row", async () => {
  const item = await fetchItem(1, async () => ({ rows: [{ id: 1, name: "alpha", description: "seed row alpha" }] }));
  assert.deepEqual(item, { id: 1, name: "alpha", description: "seed row alpha" });
});

test("fetchItem returns null when no rows", async () => {
  const item = await fetchItem(999, async () => ({ rows: [] }));
  assert.equal(item, null);
});
