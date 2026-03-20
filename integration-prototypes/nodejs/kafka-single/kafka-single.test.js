const test = require("node:test");
const assert = require("node:assert/strict");

const { buildMessage, sendMessage } = require("./producer");
const { consumeOnce } = require("./consumer");

test("buildMessage", () => {
  assert.deepEqual(buildMessage("1", "hello"), { id: "1", text: "hello" });
});

test("sendMessage uses producer lifecycle", async () => {
  const calls = [];
  const kafkaFactory = () => ({
    producer() {
      return {
        async connect() {
          calls.push("connect");
        },
        async send(payload) {
          calls.push({ send: payload });
        },
        async disconnect() {
          calls.push("disconnect");
        },
      };
    },
  });

  await sendMessage({ topic: "topic", brokers: "localhost:9092", message: { id: "1" } }, kafkaFactory);
  assert.equal(calls[0], "connect");
  assert.equal(calls[2], "disconnect");
});

test("consumeOnce reads one message", async () => {
  const kafkaFactory = () => ({
    consumer() {
      return {
        async connect() {},
        async subscribe() {},
        run({ eachMessage }) {
          void eachMessage({ message: { value: Buffer.from('{"id":"1","text":"hello"}', "utf8") } });
        },
        async disconnect() {},
      };
    },
  });

  const result = await consumeOnce({ timeoutMs: 50 }, kafkaFactory);
  assert.deepEqual(result, { id: "1", text: "hello" });
});
