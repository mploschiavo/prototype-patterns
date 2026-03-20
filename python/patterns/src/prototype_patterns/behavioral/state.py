"""State pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class OrderContext:
    def __init__(self) -> None:
        self._state: OrderState = PendingState()

    def advance(self) -> str:
        return self._state.advance(self)

    def set_state(self, state: "OrderState") -> None:
        self._state = state


class OrderState(ABC):
    @abstractmethod
    def advance(self, context: OrderContext) -> str:
        raise NotImplementedError


class PendingState(OrderState):
    def advance(self, context: OrderContext) -> str:
        context.set_state(PaidState())
        return "pending->paid"


class PaidState(OrderState):
    def advance(self, context: OrderContext) -> str:
        context.set_state(ShippedState())
        return "paid->shipped"


class ShippedState(OrderState):
    def advance(self, context: OrderContext) -> str:
        return "shipped->shipped"


def demo() -> tuple[str, str, str]:
    order = OrderContext()
    return (order.advance(), order.advance(), order.advance())
