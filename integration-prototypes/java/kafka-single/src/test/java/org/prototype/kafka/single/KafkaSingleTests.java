package org.prototype.kafka.single;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public final class KafkaSingleTests {
    @Test
    void buildMessageFormatsJson() {
        assertEquals("{\"id\":\"1\",\"text\":\"hello\"}", ProducerClient.buildMessage("1", "hello"));
    }
}
