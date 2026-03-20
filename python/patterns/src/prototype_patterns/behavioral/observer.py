"""Observer pattern example."""

from __future__ import annotations

from typing import Callable


class Subject:
    def __init__(self) -> None:
        self._observers: list[Callable[[int], None]] = []
        self._state = 0

    def subscribe(self, observer: Callable[[int], None]) -> None:
        self._observers.append(observer)

    def set_state(self, value: int) -> None:
        self._state = value
        for observer in self._observers:
            observer(self._state)


def demo() -> list[int]:
    events: list[int] = []
    subject = Subject()
    subject.subscribe(events.append)
    subject.set_state(7)
    return events
