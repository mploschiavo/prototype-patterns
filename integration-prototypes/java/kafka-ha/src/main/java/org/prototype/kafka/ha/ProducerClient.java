package org.prototype.kafka.ha;

import java.util.Properties;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

public final class ProducerClient {
    private ProducerClient() {
    }

    public static String buildMessage(String id, String text) {
        return "{\"id\":\"" + id + "\",\"text\":\"" + text + "\"}";
    }

    public static void sendMessage(String bootstrapServers, String topic, String message) {
        Properties properties = new Properties();
        properties.put("bootstrap.servers", bootstrapServers);
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        try (KafkaProducer<String, String> producer = new KafkaProducer<>(properties)) {
            producer.send(new ProducerRecord<>(topic, message));
            producer.flush();
        }
    }

    public static void main(String[] args) {
        String bootstrap = System.getenv().getOrDefault("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092,localhost:9094,localhost:9096");
        String topic = System.getenv().getOrDefault("KAFKA_TOPIC", "prototype-topic-ha");
        String payload = buildMessage("1", "hello from java kafka ha producer");
        sendMessage(bootstrap, topic, payload);
        System.out.println("sent: " + payload);
    }
}
