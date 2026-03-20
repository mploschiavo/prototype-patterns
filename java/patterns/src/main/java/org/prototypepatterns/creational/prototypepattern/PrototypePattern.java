package org.prototypepatterns.creational.prototypepattern;

import java.util.ArrayList;
import java.util.List;

public final class PrototypePattern {
    private PrototypePattern() {
    }

    public static final class Document {
        public final String title;
        public final List<String> tags;

        public Document(String title, List<String> tags) {
            this.title = title;
            this.tags = tags;
        }

        public Document cloneDocument() {
            return new Document(title, new ArrayList<>(tags));
        }
    }

    public static boolean demo() {
        Document original = new Document("Pattern Notes", new ArrayList<>(List.of("draft")));
        Document copy = original.cloneDocument();
        copy.tags.add("review");
        return original.tags.size() == 1 && copy.tags.size() == 2;
    }
}
