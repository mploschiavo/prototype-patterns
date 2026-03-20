"""Singleton pattern example."""

from __future__ import annotations


class Configuration:
    """Ensures only one configuration instance exists."""

    _instance: Configuration | None = None

    def __new__(cls) -> Configuration:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._settings = {}
        return cls._instance

    def set(self, key: str, value: str) -> None:
        self._settings[key] = value

    def get(self, key: str) -> str | None:
        return self._settings.get(key)


def demo() -> bool:
    first = Configuration()
    second = Configuration()
    first.set("mode", "prototype")
    return first is second and second.get("mode") == "prototype"
