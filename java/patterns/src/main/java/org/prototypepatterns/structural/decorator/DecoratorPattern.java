package org.prototypepatterns.structural.decorator;

public final class DecoratorPattern {
    private DecoratorPattern() {
    }

    interface Notifier {
        String send(String message);
    }

    static final class EmailNotifier implements Notifier {
        @Override
        public String send(String message) {
            return "email:" + message;
        }
    }

    static final class SmsDecorator implements Notifier {
        private final Notifier wrapped;

        SmsDecorator(Notifier wrapped) {
            this.wrapped = wrapped;
        }

        @Override
        public String send(String message) {
            return wrapped.send(message) + "|sms:" + message;
        }
    }

    static final class SlackDecorator implements Notifier {
        private final Notifier wrapped;

        SlackDecorator(Notifier wrapped) {
            this.wrapped = wrapped;
        }

        @Override
        public String send(String message) {
            return wrapped.send(message) + "|slack:" + message;
        }
    }

    public static String demo() {
        Notifier notifier = new SlackDecorator(new SmsDecorator(new EmailNotifier()));
        return notifier.send("build complete");
    }
}
