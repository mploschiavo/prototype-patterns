from __future__ import annotations

import unittest

from prototype_patterns.creational import (
    abstract_factory,
    builder,
    factory_method,
    lazy_initialization,
    object_pool,
    prototype,
    singleton,
)
from prototype_patterns.structural import (
    adapter,
    bridge,
    composite,
    composite_entity,
    decorator,
    facade,
    flyweight,
    proxy,
)
from prototype_patterns.behavioral import (
    chain_of_responsibility,
    command,
    iterator,
    mediator,
    memento,
    observer,
    state,
    strategy,
    template_method,
)


class PatternTests(unittest.TestCase):
    def test_singleton(self) -> None:
        self.assertTrue(singleton.demo())

    def test_factory_method(self) -> None:
        self.assertEqual(factory_method.demo(), ("<button>Submit</button>", "[DesktopButton: Submit]"))

    def test_abstract_factory(self) -> None:
        self.assertEqual(abstract_factory.demo(), ("dark-button", "dark-checkbox"))

    def test_builder(self) -> None:
        house = builder.demo()
        self.assertEqual(house.rooms, ["Kitchen", "Office"])
        self.assertTrue(house.has_garage)

    def test_prototype(self) -> None:
        self.assertTrue(prototype.demo())

    def test_object_pool(self) -> None:
        self.assertTrue(object_pool.demo())

    def test_lazy_initialization(self) -> None:
        self.assertTrue(lazy_initialization.demo())

    def test_adapter(self) -> None:
        self.assertEqual(adapter.demo(), 25.0)

    def test_decorator(self) -> None:
        self.assertEqual(decorator.demo(), "email:build complete|sms:build complete|slack:build complete")

    def test_composite(self) -> None:
        self.assertEqual(composite.demo(), 30)

    def test_facade(self) -> None:
        self.assertIn("projector on", facade.demo())

    def test_proxy(self) -> None:
        self.assertTrue(proxy.demo())

    def test_bridge(self) -> None:
        self.assertEqual(bridge.demo(), ("vector-circle:5", "raster-circle:5"))

    def test_flyweight(self) -> None:
        self.assertTrue(flyweight.demo())

    def test_composite_entity(self) -> None:
        self.assertEqual(composite_entity.demo(), ("Sam", "Austin"))

    def test_observer(self) -> None:
        self.assertEqual(observer.demo(), [7])

    def test_strategy(self) -> None:
        self.assertEqual(strategy.demo(), ([1, 2, 3], [3, 2, 1]))

    def test_command(self) -> None:
        self.assertEqual(command.demo(), "light:on")

    def test_state(self) -> None:
        self.assertEqual(state.demo(), ("pending->paid", "paid->shipped", "shipped->shipped"))

    def test_template_method(self) -> None:
        self.assertEqual(template_method.demo(), ["read:csv", "transform:normalize", "write:warehouse"])

    def test_chain_of_responsibility(self) -> None:
        self.assertEqual(chain_of_responsibility.demo(), ("team-lead", "manager", "unhandled:4"))

    def test_iterator(self) -> None:
        self.assertEqual(iterator.demo(), ["intro", "verse", "outro"])

    def test_mediator(self) -> None:
        self.assertEqual(mediator.demo(), ["alex:ready"])

    def test_memento(self) -> None:
        self.assertEqual(memento.demo(), "draft")


if __name__ == "__main__":
    unittest.main()
