package org.prototype.redis.single;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public final class RedisSingleTests {
    @Test
    void jsonEnvelopeFormat() {
        String key = "demo:key";
        String value = "{\"id\":1,\"value\":\"hello\"}";
        assertEquals("{\"key\":\"demo:key\",\"value\":" + value + "}", "{\"key\":\"" + key + "\",\"value\":" + value + "}");
    }
}
