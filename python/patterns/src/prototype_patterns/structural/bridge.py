"""Bridge pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: int) -> str:
        raise NotImplementedError


class VectorRenderer(Renderer):
    def render_circle(self, radius: int) -> str:
        return f"vector-circle:{radius}"


class RasterRenderer(Renderer):
    def render_circle(self, radius: int) -> str:
        return f"raster-circle:{radius}"


class Circle:
    def __init__(self, radius: int, renderer: Renderer) -> None:
        self._radius = radius
        self._renderer = renderer

    def draw(self) -> str:
        return self._renderer.render_circle(self._radius)


def demo() -> tuple[str, str]:
    return (Circle(5, VectorRenderer()).draw(), Circle(5, RasterRenderer()).draw())
