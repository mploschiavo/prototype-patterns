"""Composite pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def size(self) -> int:
        raise NotImplementedError


class File(Node):
    def __init__(self, bytes_size: int) -> None:
        self._bytes_size = bytes_size

    def size(self) -> int:
        return self._bytes_size


class Folder(Node):
    def __init__(self) -> None:
        self._children: list[Node] = []

    def add(self, child: Node) -> None:
        self._children.append(child)

    def size(self) -> int:
        return sum(child.size() for child in self._children)


def demo() -> int:
    root = Folder()
    root.add(File(10))
    nested = Folder()
    nested.add(File(5))
    nested.add(File(15))
    root.add(nested)
    return root.size()
