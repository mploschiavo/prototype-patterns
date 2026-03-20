"""Composite Entity pattern example."""

from __future__ import annotations


class OrderHeader:
    def __init__(self) -> None:
        self.customer_name = ""


class ShippingInfo:
    def __init__(self) -> None:
        self.city = ""


class CoarseGrainedOrder:
    def __init__(self) -> None:
        self.header = OrderHeader()
        self.shipping = ShippingInfo()

    def set_data(self, customer_name: str, city: str) -> None:
        self.header.customer_name = customer_name
        self.shipping.city = city

    def get_data(self) -> tuple[str, str]:
        return (self.header.customer_name, self.shipping.city)


class CompositeOrderEntity:
    def __init__(self) -> None:
        self._order = CoarseGrainedOrder()

    def set_order(self, customer_name: str, city: str) -> None:
        self._order.set_data(customer_name, city)

    def read_order(self) -> tuple[str, str]:
        return self._order.get_data()


def demo() -> tuple[str, str]:
    entity = CompositeOrderEntity()
    entity.set_order("Sam", "Austin")
    return entity.read_order()
