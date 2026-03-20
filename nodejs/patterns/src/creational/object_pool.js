class Worker {
  constructor(workerId) {
    this.workerId = workerId;
    this.busy = false;
  }

  reset() {
    this.busy = false;
  }
}

class WorkerPool {
  constructor(size) {
    this.available = Array.from({ length: size }, (_, index) => new Worker(index));
    this.inUse = new Set();
  }

  acquire() {
    if (this.available.length === 0) {
      throw new Error("pool exhausted");
    }
    const worker = this.available.pop();
    worker.busy = true;
    this.inUse.add(worker.workerId);
    return worker;
  }

  release(worker) {
    if (!this.inUse.has(worker.workerId)) {
      throw new Error("worker was not checked out");
    }
    this.inUse.delete(worker.workerId);
    worker.reset();
    this.available.push(worker);
  }
}

function demo() {
  const pool = new WorkerPool(2);
  const first = pool.acquire();
  pool.acquire();
  pool.release(first);
  const again = pool.acquire();
  return first.workerId === again.workerId;
}

module.exports = { WorkerPool, demo };
