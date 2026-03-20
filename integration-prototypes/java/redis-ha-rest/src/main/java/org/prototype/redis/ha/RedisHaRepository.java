package org.prototype.redis.ha;

import java.util.HashSet;
import java.util.Set;
import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;

public final class RedisHaRepository {
    private RedisHaRepository() {
    }

    public static Set<HostAndPort> parseNodes(String nodes) {
        Set<HostAndPort> parsed = new HashSet<>();
        for (String node : nodes.split(",")) {
            String[] parts = node.trim().split(":", 2);
            parsed.add(new HostAndPort(parts[0], Integer.parseInt(parts[1])));
        }
        return parsed;
    }

    public static String fetchValue(String nodes, String key) {
        try (JedisCluster cluster = new JedisCluster(parseNodes(nodes))) {
            return cluster.get(key);
        }
    }
}
