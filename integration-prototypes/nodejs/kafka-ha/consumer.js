const { Kafka } = require("kafkajs");

async function consumeOnce(
  {
    topic = "prototype-topic-ha",
    brokers = "localhost:9092,localhost:9094,localhost:9096",
    groupId = "node-kafka-ha-consumer",
    timeoutMs = 5000,
  },
  kafkaFactory = (config) => new Kafka(config),
) {
  const kafka = kafkaFactory({
    clientId: "node-kafka-ha-consumer-client",
    brokers: brokers.split(",").map((entry) => entry.trim()),
  });

  const consumer = kafka.consumer({ groupId });
  let received = null;

  await consumer.connect();
  await consumer.subscribe({ topic, fromBeginning: true });

  await new Promise((resolve) => {
    const timeout = setTimeout(resolve, timeoutMs);

    consumer.run({
      eachMessage: async ({ message }) => {
        if (received === null) {
          received = JSON.parse(message.value.toString("utf8"));
          clearTimeout(timeout);
          resolve();
        }
      },
    });
  });

  await consumer.disconnect();
  return received;
}

async function main() {
  const message = await consumeOnce({
    topic: process.env.KAFKA_TOPIC || "prototype-topic-ha",
    brokers: process.env.KAFKA_BOOTSTRAP_SERVERS || "localhost:9092,localhost:9094,localhost:9096",
  });
  // eslint-disable-next-line no-console
  console.log("message received", message);
}

module.exports = { consumeOnce };

if (require.main === module) {
  main().catch((error) => {
    // eslint-disable-next-line no-console
    console.error(error);
    process.exit(1);
  });
}
