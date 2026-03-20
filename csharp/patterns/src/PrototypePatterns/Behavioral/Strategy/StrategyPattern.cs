namespace PrototypePatterns.Behavioral.Strategy;

public interface ISortStrategy
{
    IReadOnlyList<int> Sort(IReadOnlyList<int> data);
}

public sealed class AscendingSort : ISortStrategy
{
    public IReadOnlyList<int> Sort(IReadOnlyList<int> data) => [.. data.OrderBy(value => value)];
}

public sealed class DescendingSort : ISortStrategy
{
    public IReadOnlyList<int> Sort(IReadOnlyList<int> data) => [.. data.OrderByDescending(value => value)];
}

public sealed class SortContext(ISortStrategy strategy)
{
    private ISortStrategy _strategy = strategy;

    public void SetStrategy(ISortStrategy strategyValue) => _strategy = strategyValue;

    public IReadOnlyList<int> Run(IReadOnlyList<int> data) => _strategy.Sort(data);
}

public static class StrategyPattern
{
    public static IReadOnlyList<IReadOnlyList<int>> Demo()
    {
        var context = new SortContext(new AscendingSort());
        var ascending = context.Run([3, 1, 2]);
        context.SetStrategy(new DescendingSort());
        var descending = context.Run([3, 1, 2]);
        return [ascending, descending];
    }
}
