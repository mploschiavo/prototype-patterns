const { Kafka } = require("kafkajs");

function buildMessage(id, text) {
  return { id, text };
}

async function sendMessage(
  { topic = "prototype-topic-ha", brokers = "localhost:9092,localhost:9094,localhost:9096", message },
  kafkaFactory = (config) => new Kafka(config),
) {
  const kafka = kafkaFactory({
    clientId: "node-kafka-ha-producer",
    brokers: brokers.split(",").map((entry) => entry.trim()),
  });

  const producer = kafka.producer();
  await producer.connect();
  await producer.send({ topic, messages: [{ value: JSON.stringify(message) }] });
  await producer.disconnect();
}

async function main() {
  const payload = buildMessage("1", "hello from node kafka ha producer");
  await sendMessage({
    topic: process.env.KAFKA_TOPIC || "prototype-topic-ha",
    brokers: process.env.KAFKA_BOOTSTRAP_SERVERS || "localhost:9092,localhost:9094,localhost:9096",
    message: payload,
  });
  // eslint-disable-next-line no-console
  console.log("message sent", payload);
}

module.exports = { buildMessage, sendMessage };

if (require.main === module) {
  main().catch((error) => {
    // eslint-disable-next-line no-console
    console.error(error);
    process.exit(1);
  });
}
