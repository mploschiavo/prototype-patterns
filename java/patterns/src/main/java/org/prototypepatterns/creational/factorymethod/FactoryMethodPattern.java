package org.prototypepatterns.creational.factorymethod;

import java.util.List;

public final class FactoryMethodPattern {
    private FactoryMethodPattern() {
    }

    interface Button {
        String render();
    }

    static final class HtmlButton implements Button {
        @Override
        public String render() {
            return "<button>Submit</button>";
        }
    }

    static final class DesktopButton implements Button {
        @Override
        public String render() {
            return "[DesktopButton: Submit]";
        }
    }

    abstract static class Dialog {
        abstract Button createButton();

        String renderDialog() {
            return createButton().render();
        }
    }

    static final class WebDialog extends Dialog {
        @Override
        Button createButton() {
            return new HtmlButton();
        }
    }

    static final class DesktopDialog extends Dialog {
        @Override
        Button createButton() {
            return new DesktopButton();
        }
    }

    public static List<String> demo() {
        return List.of(new WebDialog().renderDialog(), new DesktopDialog().renderDialog());
    }
}
