"""Strategy pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        raise NotImplementedError


class AscendingSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        return sorted(data)


class DescendingSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        return sorted(data, reverse=True)


class SortContext:
    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def run(self, data: list[int]) -> list[int]:
        return self._strategy.sort(data)


def demo() -> tuple[list[int], list[int]]:
    context = SortContext(AscendingSort())
    ascending = context.run([3, 1, 2])
    context.set_strategy(DescendingSort())
    descending = context.run([3, 1, 2])
    return (ascending, descending)
