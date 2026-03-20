package org.prototypepatterns.creational.objectpool;

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

public final class ObjectPoolPattern {
    private ObjectPoolPattern() {
    }

    public static final class Worker {
        public final int workerId;
        public boolean busy;

        public Worker(int workerId) {
            this.workerId = workerId;
        }

        public void reset() {
            busy = false;
        }
    }

    public static final class WorkerPool {
        private final Queue<Worker> available = new ArrayDeque<>();
        private final Set<Integer> inUse = new HashSet<>();

        public WorkerPool(int size) {
            for (int i = 0; i < size; i++) {
                available.add(new Worker(i));
            }
        }

        public Worker acquire() {
            Worker worker = available.poll();
            if (worker == null) {
                throw new IllegalStateException("pool exhausted");
            }
            worker.busy = true;
            inUse.add(worker.workerId);
            return worker;
        }

        public void release(Worker worker) {
            if (!inUse.remove(worker.workerId)) {
                throw new IllegalStateException("worker was not checked out");
            }
            worker.reset();
            available.add(worker);
        }
    }

    public static boolean demo() {
        WorkerPool pool = new WorkerPool(2);
        Worker first = pool.acquire();
        pool.acquire();
        pool.release(first);
        Worker again = pool.acquire();
        return first.workerId == again.workerId;
    }
}
