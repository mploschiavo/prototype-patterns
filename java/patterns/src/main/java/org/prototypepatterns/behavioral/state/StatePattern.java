package org.prototypepatterns.behavioral.state;

import java.util.List;

public final class StatePattern {
    private StatePattern() {
    }

    interface OrderState {
        String advance(OrderContext context);
    }

    static final class PendingState implements OrderState {
        @Override
        public String advance(OrderContext context) {
            context.setState(new PaidState());
            return "pending->paid";
        }
    }

    static final class PaidState implements OrderState {
        @Override
        public String advance(OrderContext context) {
            context.setState(new ShippedState());
            return "paid->shipped";
        }
    }

    static final class ShippedState implements OrderState {
        @Override
        public String advance(OrderContext context) {
            return "shipped->shipped";
        }
    }

    static final class OrderContext {
        private OrderState state = new PendingState();

        void setState(OrderState state) {
            this.state = state;
        }

        String advance() {
            return state.advance(this);
        }
    }

    public static List<String> demo() {
        OrderContext context = new OrderContext();
        return List.of(context.advance(), context.advance(), context.advance());
    }
}
