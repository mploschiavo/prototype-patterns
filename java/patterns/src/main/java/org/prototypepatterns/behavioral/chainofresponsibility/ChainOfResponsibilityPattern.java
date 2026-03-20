package org.prototypepatterns.behavioral.chainofresponsibility;

import java.util.List;

public final class ChainOfResponsibilityPattern {
    private ChainOfResponsibilityPattern() {
    }

    abstract static class Handler {
        private final Handler next;

        Handler(Handler next) {
            this.next = next;
        }

        abstract String handle(int level);

        String nextOrDefault(int level) {
            if (next == null) {
                return "unhandled:" + level;
            }
            return next.handle(level);
        }
    }

    static final class TeamLeadHandler extends Handler {
        TeamLeadHandler(Handler next) {
            super(next);
        }

        @Override
        String handle(int level) {
            if (level <= 1) {
                return "team-lead";
            }
            return nextOrDefault(level);
        }
    }

    static final class ManagerHandler extends Handler {
        ManagerHandler(Handler next) {
            super(next);
        }

        @Override
        String handle(int level) {
            if (level <= 2) {
                return "manager";
            }
            return nextOrDefault(level);
        }
    }

    static final class DirectorHandler extends Handler {
        DirectorHandler(Handler next) {
            super(next);
        }

        @Override
        String handle(int level) {
            if (level <= 3) {
                return "director";
            }
            return nextOrDefault(level);
        }
    }

    public static List<String> demo() {
        Handler chain = new TeamLeadHandler(new ManagerHandler(new DirectorHandler(null)));
        return List.of(chain.handle(1), chain.handle(2), chain.handle(4));
    }
}
