package org.prototype.redis.single;

import redis.clients.jedis.Jedis;

public final class RedisSingleRepository {
    private RedisSingleRepository() {
    }

    public static String fetchValue(String redisUrl, String key) {
        try (Jedis jedis = new Jedis(redisUrl)) {
            return jedis.get(key);
        }
    }
}
