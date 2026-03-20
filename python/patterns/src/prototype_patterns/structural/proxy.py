"""Proxy pattern example."""

from __future__ import annotations


class RealImage:
    load_count = 0

    def __init__(self, path: str) -> None:
        self.path = path
        RealImage.load_count += 1

    def display(self) -> str:
        return f"display:{self.path}"


class ImageProxy:
    def __init__(self, path: str) -> None:
        self._path = path
        self._real_image: RealImage | None = None

    def display(self) -> str:
        if self._real_image is None:
            self._real_image = RealImage(self._path)
        return self._real_image.display()


def demo() -> bool:
    RealImage.load_count = 0
    proxy = ImageProxy("chart.png")
    first = proxy.display()
    second = proxy.display()
    return first == second and RealImage.load_count == 1
