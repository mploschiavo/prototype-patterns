package org.prototypepatterns.behavioral.observer;

import java.util.ArrayList;
import java.util.List;
import java.util.function.IntConsumer;

public final class ObserverPattern {
    private ObserverPattern() {
    }

    public static final class Subject {
        private final List<IntConsumer> observers = new ArrayList<>();

        public void subscribe(IntConsumer observer) {
            observers.add(observer);
        }

        public void setState(int value) {
            observers.forEach(observer -> observer.accept(value));
        }
    }

    public static List<Integer> demo() {
        List<Integer> events = new ArrayList<>();
        Subject subject = new Subject();
        subject.subscribe(events::add);
        subject.setState(7);
        return events;
    }
}
