package org.prototype.redis.ha;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public final class RedisHaTests {
    @Test
    void parseNodesCount() {
        assertEquals(3, RedisHaRepository.parseNodes("localhost:6379,localhost:6380,localhost:6381").size());
    }
}
