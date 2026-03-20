package org.prototypepatterns.behavioral.memento;

public final class MementoPattern {
    private MementoPattern() {
    }

    public record Memento(String text) {
    }

    public static final class TextEditor {
        private String text = "";

        public void type(String value) {
            text = value;
        }

        public Memento save() {
            return new Memento(text);
        }

        public void restore(Memento memento) {
            text = memento.text();
        }

        public String text() {
            return text;
        }
    }

    public static String demo() {
        TextEditor editor = new TextEditor();
        editor.type("draft");
        Memento checkpoint = editor.save();
        editor.type("final");
        editor.restore(checkpoint);
        return editor.text();
    }
}
