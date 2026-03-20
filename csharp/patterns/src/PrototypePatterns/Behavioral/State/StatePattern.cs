namespace PrototypePatterns.Behavioral.State;

public interface IOrderState
{
    string Advance(OrderContext context);
}

public sealed class PendingState : IOrderState
{
    public string Advance(OrderContext context)
    {
        context.SetState(new PaidState());
        return "pending->paid";
    }
}

public sealed class PaidState : IOrderState
{
    public string Advance(OrderContext context)
    {
        context.SetState(new ShippedState());
        return "paid->shipped";
    }
}

public sealed class ShippedState : IOrderState
{
    public string Advance(OrderContext context) => "shipped->shipped";
}

public sealed class OrderContext
{
    private IOrderState _state = new PendingState();

    public void SetState(IOrderState state) => _state = state;

    public string Advance() => _state.Advance(this);
}

public static class StatePattern
{
    public static IReadOnlyList<string> Demo()
    {
        var order = new OrderContext();
        return [order.Advance(), order.Advance(), order.Advance()];
    }
}
