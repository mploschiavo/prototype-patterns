package org.prototypepatterns.creational.singleton;

import java.util.HashMap;
import java.util.Map;

public final class SingletonPattern {
    private SingletonPattern() {
    }

    public static final class Configuration {
        private static final Configuration INSTANCE = new Configuration();
        private final Map<String, String> settings = new HashMap<>();

        private Configuration() {
        }

        public static Configuration instance() {
            return INSTANCE;
        }

        public void set(String key, String value) {
            settings.put(key, value);
        }

        public String get(String key) {
            return settings.get(key);
        }
    }

    public static boolean demo() {
        Configuration first = Configuration.instance();
        Configuration second = Configuration.instance();
        first.set("mode", "prototype");
        return first == second && "prototype".equals(second.get("mode"));
    }
}
