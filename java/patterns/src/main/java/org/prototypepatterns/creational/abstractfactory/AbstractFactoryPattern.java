package org.prototypepatterns.creational.abstractfactory;

import java.util.List;

public final class AbstractFactoryPattern {
    private AbstractFactoryPattern() {
    }

    interface Button {
        String paint();
    }

    interface Checkbox {
        String paint();
    }

    interface ThemeFactory {
        Button createButton();

        Checkbox createCheckbox();
    }

    static final class DarkButton implements Button {
        @Override
        public String paint() {
            return "dark-button";
        }
    }

    static final class DarkCheckbox implements Checkbox {
        @Override
        public String paint() {
            return "dark-checkbox";
        }
    }

    static final class DarkThemeFactory implements ThemeFactory {
        @Override
        public Button createButton() {
            return new DarkButton();
        }

        @Override
        public Checkbox createCheckbox() {
            return new DarkCheckbox();
        }
    }

    public static List<String> demo() {
        ThemeFactory factory = new DarkThemeFactory();
        return List.of(factory.createButton().paint(), factory.createCheckbox().paint());
    }
}
