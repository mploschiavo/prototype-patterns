package org.prototypepatterns.behavioral.mediator;

import java.util.ArrayList;
import java.util.List;

public final class MediatorPattern {
    private MediatorPattern() {
    }

    public static final class ChatMediator {
        private final List<Participant> participants = new ArrayList<>();

        public void register(Participant participant) {
            participants.add(participant);
        }

        public void broadcast(Participant sender, String message) {
            for (Participant participant : participants) {
                if (participant != sender) {
                    participant.receive(message);
                }
            }
        }
    }

    public static final class Participant {
        private final String name;
        private final ChatMediator mediator;
        private final List<String> inbox = new ArrayList<>();

        public Participant(String name, ChatMediator mediator) {
            this.name = name;
            this.mediator = mediator;
            mediator.register(this);
        }

        public void send(String message) {
            mediator.broadcast(this, name + ":" + message);
        }

        public void receive(String message) {
            inbox.add(message);
        }

        public List<String> inbox() {
            return inbox;
        }
    }

    public static List<String> demo() {
        ChatMediator mediator = new ChatMediator();
        Participant alex = new Participant("alex", mediator);
        Participant river = new Participant("river", mediator);
        alex.send("ready");
        return river.inbox();
    }
}
