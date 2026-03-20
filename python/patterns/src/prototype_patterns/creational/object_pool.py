"""Object Pool pattern example."""

from __future__ import annotations


class Worker:
    def __init__(self, worker_id: int) -> None:
        self.worker_id = worker_id
        self.busy = False

    def reset(self) -> None:
        self.busy = False


class WorkerPool:
    def __init__(self, size: int) -> None:
        self._available = [Worker(index) for index in range(size)]
        self._in_use: set[int] = set()

    def acquire(self) -> Worker:
        if not self._available:
            raise RuntimeError("pool exhausted")
        worker = self._available.pop()
        worker.busy = True
        self._in_use.add(worker.worker_id)
        return worker

    def release(self, worker: Worker) -> None:
        if worker.worker_id not in self._in_use:
            raise RuntimeError("worker was not checked out")
        self._in_use.remove(worker.worker_id)
        worker.reset()
        self._available.append(worker)


def demo() -> bool:
    pool = WorkerPool(2)
    first = pool.acquire()
    second = pool.acquire()
    pool.release(first)
    again = pool.acquire()
    return first.worker_id == again.worker_id and second.busy
