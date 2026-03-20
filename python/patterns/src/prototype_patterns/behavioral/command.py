"""Command pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        raise NotImplementedError


class Light:
    def on(self) -> str:
        return "light:on"


class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> str:
        return self._light.on()


class RemoteButton:
    def __init__(self, command: Command) -> None:
        self._command = command

    def press(self) -> str:
        return self._command.execute()


def demo() -> str:
    return RemoteButton(LightOnCommand(Light())).press()
