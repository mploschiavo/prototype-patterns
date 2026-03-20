"""Mediator pattern example."""

from __future__ import annotations


class ChatMediator:
    def __init__(self) -> None:
        self._participants: list[Participant] = []

    def register(self, participant: "Participant") -> None:
        self._participants.append(participant)

    def broadcast(self, sender: "Participant", message: str) -> None:
        for participant in self._participants:
            if participant is not sender:
                participant.receive(message)


class Participant:
    def __init__(self, name: str, mediator: ChatMediator) -> None:
        self.name = name
        self.inbox: list[str] = []
        self._mediator = mediator
        mediator.register(self)

    def send(self, message: str) -> None:
        self._mediator.broadcast(self, f"{self.name}:{message}")

    def receive(self, message: str) -> None:
        self.inbox.append(message)


def demo() -> list[str]:
    mediator = ChatMediator()
    alex = Participant("alex", mediator)
    river = Participant("river", mediator)
    alex.send("ready")
    return river.inbox
