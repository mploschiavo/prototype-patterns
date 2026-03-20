namespace PrototypePatterns.Behavioral.Observer;

public sealed class Subject
{
    private event Action<int>? Changed;

    public void Subscribe(Action<int> observer)
    {
        Changed += observer;
    }

    public void SetState(int value)
    {
        Changed?.Invoke(value);
    }
}

public static class ObserverPattern
{
    public static IReadOnlyList<int> Demo()
    {
        var events = new List<int>();
        var subject = new Subject();
        subject.Subscribe(events.Add);
        subject.SetState(7);
        return events;
    }
}
