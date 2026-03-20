"""Iterator pattern example."""

from __future__ import annotations


class PlaylistIterator:
    def __init__(self, songs: list[str]) -> None:
        self._songs = songs
        self._index = 0

    def __iter__(self) -> "PlaylistIterator":
        return self

    def __next__(self) -> str:
        if self._index >= len(self._songs):
            raise StopIteration
        song = self._songs[self._index]
        self._index += 1
        return song


class Playlist:
    def __init__(self, songs: list[str]) -> None:
        self._songs = songs

    def __iter__(self) -> PlaylistIterator:
        return PlaylistIterator(self._songs)


def demo() -> list[str]:
    return list(Playlist(["intro", "verse", "outro"]))
