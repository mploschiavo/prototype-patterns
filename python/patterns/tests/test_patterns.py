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


def test_singleton() -> None:
    assert singleton.demo()


def test_factory_method() -> None:
    assert factory_method.demo() == ("<button>Submit</button>", "[DesktopButton: Submit]")


def test_abstract_factory() -> None:
    assert abstract_factory.demo() == ("dark-button", "dark-checkbox")


def test_builder() -> None:
    house = builder.demo()
    assert house.rooms == ["Kitchen", "Office"]
    assert house.has_garage is True


def test_prototype() -> None:
    assert prototype.demo()


def test_object_pool() -> None:
    assert object_pool.demo()


def test_lazy_initialization() -> None:
    assert lazy_initialization.demo()


def test_adapter() -> None:
    assert adapter.demo() == 25.0


def test_decorator() -> None:
    assert decorator.demo() == "email:build complete|sms:build complete|slack:build complete"


def test_composite() -> None:
    assert composite.demo() == 30


def test_facade() -> None:
    assert "projector on" in facade.demo()


def test_proxy() -> None:
    assert proxy.demo()


def test_bridge() -> None:
    assert bridge.demo() == ("vector-circle:5", "raster-circle:5")


def test_flyweight() -> None:
    assert flyweight.demo()


def test_composite_entity() -> None:
    assert composite_entity.demo() == ("Sam", "Austin")


def test_observer() -> None:
    assert observer.demo() == [7]


def test_strategy() -> None:
    assert strategy.demo() == ([1, 2, 3], [3, 2, 1])


def test_command() -> None:
    assert command.demo() == "light:on"


def test_state() -> None:
    assert state.demo() == ("pending->paid", "paid->shipped", "shipped->shipped")


def test_template_method() -> None:
    assert template_method.demo() == ["read:csv", "transform:normalize", "write:warehouse"]


def test_chain_of_responsibility() -> None:
    assert chain_of_responsibility.demo() == ("team-lead", "manager", "unhandled:4")


def test_iterator() -> None:
    assert iterator.demo() == ["intro", "verse", "outro"]


def test_mediator() -> None:
    assert mediator.demo() == ["alex:ready"]


def test_memento() -> None:
    assert memento.demo() == "draft"
