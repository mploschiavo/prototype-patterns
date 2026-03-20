"""Lazy Initialization pattern example."""

from __future__ import annotations


class LazyDataset:
    def __init__(self) -> None:
        self._records: list[str] | None = None
        self.load_count = 0

    @property
    def records(self) -> list[str]:
        if self._records is None:
            self.load_count += 1
            self._records = ["row-1", "row-2", "row-3"]
        return self._records


def demo() -> bool:
    dataset = LazyDataset()
    first = dataset.records
    second = dataset.records
    return first == second and dataset.load_count == 1
