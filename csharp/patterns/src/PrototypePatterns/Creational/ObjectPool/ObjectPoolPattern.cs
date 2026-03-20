namespace PrototypePatterns.Creational.ObjectPool;

public sealed class Worker(int workerId)
{
    public int WorkerId { get; } = workerId;
    public bool Busy { get; set; }

    public void Reset() => Busy = false;
}

public sealed class WorkerPool
{
    private readonly Queue<Worker> _available = new();
    private readonly HashSet<int> _inUse = [];

    public WorkerPool(int size)
    {
        for (var index = 0; index < size; index++)
        {
            _available.Enqueue(new Worker(index));
        }
    }

    public Worker Acquire()
    {
        if (_available.Count == 0)
        {
            throw new InvalidOperationException("pool exhausted");
        }

        var worker = _available.Dequeue();
        worker.Busy = true;
        _inUse.Add(worker.WorkerId);
        return worker;
    }

    public void Release(Worker worker)
    {
        if (!_inUse.Remove(worker.WorkerId))
        {
            throw new InvalidOperationException("worker was not checked out");
        }

        worker.Reset();
        _available.Enqueue(worker);
    }
}

public static class ObjectPoolPattern
{
    public static bool Demo()
    {
        var pool = new WorkerPool(2);
        var first = pool.Acquire();
        pool.Acquire();
        pool.Release(first);
        var again = pool.Acquire();
        return first.WorkerId == again.WorkerId;
    }
}
