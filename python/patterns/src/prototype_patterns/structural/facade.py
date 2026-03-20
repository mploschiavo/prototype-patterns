"""Facade pattern example."""

from __future__ import annotations


class Lights:
    def dim(self) -> str:
        return "lights dimmed"


class Projector:
    def on(self) -> str:
        return "projector on"


class SoundSystem:
    def surround(self) -> str:
        return "surround enabled"


class HomeTheaterFacade:
    def __init__(self, lights: Lights, projector: Projector, sound: SoundSystem) -> None:
        self._lights = lights
        self._projector = projector
        self._sound = sound

    def watch_movie(self) -> str:
        actions = [self._lights.dim(), self._projector.on(), self._sound.surround()]
        return " | ".join(actions)


def demo() -> str:
    facade = HomeTheaterFacade(Lights(), Projector(), SoundSystem())
    return facade.watch_movie()
