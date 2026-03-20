"""Chain of Responsibility pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handler: "Handler | None" = None) -> None:
        self._next = next_handler

    @abstractmethod
    def handle(self, level: int) -> str:
        raise NotImplementedError

    def _next_or_default(self, level: int) -> str:
        if self._next is None:
            return f"unhandled:{level}"
        return self._next.handle(level)


class TeamLeadHandler(Handler):
    def handle(self, level: int) -> str:
        if level <= 1:
            return "team-lead"
        return self._next_or_default(level)


class ManagerHandler(Handler):
    def handle(self, level: int) -> str:
        if level <= 2:
            return "manager"
        return self._next_or_default(level)


class DirectorHandler(Handler):
    def handle(self, level: int) -> str:
        if level <= 3:
            return "director"
        return self._next_or_default(level)


def demo() -> tuple[str, str, str]:
    chain = TeamLeadHandler(ManagerHandler(DirectorHandler()))
    return (chain.handle(1), chain.handle(2), chain.handle(4))
