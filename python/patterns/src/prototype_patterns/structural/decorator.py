"""Decorator pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"email:{message}"


class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier) -> None:
        self._wrapped = wrapped

    def send(self, message: str) -> str:
        return self._wrapped.send(message)


class SmsDecorator(NotifierDecorator):
    def send(self, message: str) -> str:
        return f"{super().send(message)}|sms:{message}"


class SlackDecorator(NotifierDecorator):
    def send(self, message: str) -> str:
        return f"{super().send(message)}|slack:{message}"


def demo() -> str:
    notifier = SlackDecorator(SmsDecorator(EmailNotifier()))
    return notifier.send("build complete")
