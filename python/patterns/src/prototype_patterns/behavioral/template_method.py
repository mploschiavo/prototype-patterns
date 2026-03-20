"""Template Method pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class DataPipeline(ABC):
    def run(self) -> list[str]:
        steps = [self.read(), self.transform(), self.write()]
        return steps

    @abstractmethod
    def read(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def transform(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def write(self) -> str:
        raise NotImplementedError


class CsvPipeline(DataPipeline):
    def read(self) -> str:
        return "read:csv"

    def transform(self) -> str:
        return "transform:normalize"

    def write(self) -> str:
        return "write:warehouse"


def demo() -> list[str]:
    return CsvPipeline().run()
