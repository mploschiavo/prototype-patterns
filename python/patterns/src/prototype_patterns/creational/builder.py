"""Builder pattern example."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class House:
    rooms: list[str] = field(default_factory=list)
    has_garage: bool = False
    has_garden: bool = False


class HouseBuilder:
    def __init__(self) -> None:
        self._house = House()

    def add_room(self, room: str) -> HouseBuilder:
        self._house.rooms.append(room)
        return self

    def with_garage(self) -> HouseBuilder:
        self._house.has_garage = True
        return self

    def with_garden(self) -> HouseBuilder:
        self._house.has_garden = True
        return self

    def build(self) -> House:
        built = self._house
        self._house = House()
        return built


def demo() -> House:
    return HouseBuilder().add_room("Kitchen").add_room("Office").with_garage().build()
