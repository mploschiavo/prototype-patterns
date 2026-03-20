package org.prototype.kafka.ha;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public final class KafkaHaTests {
    @Test
    void buildMessageFormatsJson() {
        assertEquals("{\"id\":\"1\",\"text\":\"hello\"}", ProducerClient.buildMessage("1", "hello"));
    }
}
