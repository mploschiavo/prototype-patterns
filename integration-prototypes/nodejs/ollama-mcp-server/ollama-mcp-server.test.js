const test = require("node:test");
const assert = require("node:assert/strict");

const { loadDocuments, ragSearch, handleRpc } = require("./app");

test("ragSearch returns relevant docs", () => {
  const docs = loadDocuments();
  const hits = ragSearch("Redis", docs);
  assert.ok(hits.length >= 1);
});

test("tools/list returns expected tools", async () => {
  const docs = loadDocuments();
  const response = await handleRpc({ jsonrpc: "2.0", id: 1, method: "tools/list" }, docs);
  const names = response.result.tools.map((tool) => tool.name);
  assert.deepEqual(names.sort(), ["agent.answer", "rag.search"]);
});

test("agent.answer uses provided responder", async () => {
  const docs = loadDocuments();
  const response = await handleRpc(
    {
      jsonrpc: "2.0",
      id: 2,
      method: "tools/call",
      params: { name: "agent.answer", arguments: { question: "What exists?" } },
    },
    docs,
    async () => "mock answer",
  );

  assert.equal(response.result.content[0].text, "mock answer");
});
