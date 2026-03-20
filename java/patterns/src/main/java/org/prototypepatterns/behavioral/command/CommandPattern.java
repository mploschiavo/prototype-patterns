package org.prototypepatterns.behavioral.command;

public final class CommandPattern {
    private CommandPattern() {
    }

    interface Command {
        String execute();
    }

    static final class Light {
        String on() {
            return "light:on";
        }
    }

    static final class LightOnCommand implements Command {
        private final Light light;

        LightOnCommand(Light light) {
            this.light = light;
        }

        @Override
        public String execute() {
            return light.on();
        }
    }

    static final class RemoteButton {
        private final Command command;

        RemoteButton(Command command) {
            this.command = command;
        }

        String press() {
            return command.execute();
        }
    }

    public static String demo() {
        return new RemoteButton(new LightOnCommand(new Light())).press();
    }
}
