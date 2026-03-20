namespace PrototypePatterns.Behavioral.ChainOfResponsibility;

public abstract class Handler(Handler? next)
{
    private Handler? Next { get; } = next;

    public abstract string Handle(int level);

    protected string NextOrDefault(int level) => Next is null ? $"unhandled:{level}" : Next.Handle(level);
}

public sealed class TeamLeadHandler(Handler? next) : Handler(next)
{
    public override string Handle(int level) => level <= 1 ? "team-lead" : NextOrDefault(level);
}

public sealed class ManagerHandler(Handler? next) : Handler(next)
{
    public override string Handle(int level) => level <= 2 ? "manager" : NextOrDefault(level);
}

public sealed class DirectorHandler(Handler? next) : Handler(next)
{
    public override string Handle(int level) => level <= 3 ? "director" : NextOrDefault(level);
}

public static class ChainOfResponsibilityPattern
{
    public static IReadOnlyList<string> Demo()
    {
        Handler chain = new TeamLeadHandler(new ManagerHandler(new DirectorHandler(null)));
        return [chain.Handle(1), chain.Handle(2), chain.Handle(4)];
    }
}
