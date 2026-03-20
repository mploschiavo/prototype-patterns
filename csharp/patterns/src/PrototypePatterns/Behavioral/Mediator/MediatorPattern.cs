namespace PrototypePatterns.Behavioral.Mediator;

public sealed class ChatMediator
{
    private readonly List<Participant> _participants = [];

    public void Register(Participant participant) => _participants.Add(participant);

    public void Broadcast(Participant sender, string message)
    {
        foreach (var participant in _participants.Where(participant => participant != sender))
        {
            participant.Receive(message);
        }
    }
}

public sealed class Participant
{
    private readonly ChatMediator _mediator;

    public Participant(string name, ChatMediator mediator)
    {
        Name = name;
        _mediator = mediator;
        _mediator.Register(this);
    }

    public string Name { get; }

    public List<string> Inbox { get; } = [];

    public void Send(string message) => _mediator.Broadcast(this, $"{Name}:{message}");

    public void Receive(string message) => Inbox.Add(message);
}

public static class MediatorPattern
{
    public static IReadOnlyList<string> Demo()
    {
        var mediator = new ChatMediator();
        var alex = new Participant("alex", mediator);
        var river = new Participant("river", mediator);
        alex.Send("ready");
        return river.Inbox;
    }
}
