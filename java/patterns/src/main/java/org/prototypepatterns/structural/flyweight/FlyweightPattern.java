package org.prototypepatterns.structural.flyweight;

import java.util.HashMap;
import java.util.Map;

public final class FlyweightPattern {
    private FlyweightPattern() {
    }

    public record GlyphStyle(String family, int size, boolean bold) {
    }

    public static final class GlyphStyleFactory {
        private final Map<String, GlyphStyle> cache = new HashMap<>();

        public GlyphStyle getStyle(String family, int size, boolean bold) {
            String key = family + ":" + size + ":" + bold;
            return cache.computeIfAbsent(key, ignored -> new GlyphStyle(family, size, bold));
        }
    }

    public static boolean demo() {
        GlyphStyleFactory factory = new GlyphStyleFactory();
        GlyphStyle first = factory.getStyle("Fira Code", 12, false);
        GlyphStyle second = factory.getStyle("Fira Code", 12, false);
        return first == second;
    }
}
