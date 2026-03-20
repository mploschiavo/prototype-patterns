class PendingState {
  advance(context) {
    context.state = new PaidState();
    return "pending->paid";
  }
}

class PaidState {
  advance(context) {
    context.state = new ShippedState();
    return "paid->shipped";
  }
}

class ShippedState {
  advance() {
    return "shipped->shipped";
  }
}

class OrderContext {
  constructor() {
    this.state = new PendingState();
  }

  advance() {
    return this.state.advance(this);
  }
}

function demo() {
  const order = new OrderContext();
  return [order.advance(), order.advance(), order.advance()];
}

module.exports = { OrderContext, demo };
