"""Flyweight pattern example."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GlyphStyle:
    family: str
    size: int
    bold: bool


class GlyphStyleFactory:
    def __init__(self) -> None:
        self._cache: dict[tuple[str, int, bool], GlyphStyle] = {}

    def get_style(self, family: str, size: int, bold: bool) -> GlyphStyle:
        key = (family, size, bold)
        if key not in self._cache:
            self._cache[key] = GlyphStyle(family, size, bold)
        return self._cache[key]


def demo() -> bool:
    factory = GlyphStyleFactory()
    first = factory.get_style("Fira Code", 12, False)
    second = factory.get_style("Fira Code", 12, False)
    return first is second
