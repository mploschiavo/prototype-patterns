namespace PrototypePatterns.Structural.Decorator;

public interface INotifier
{
    string Send(string message);
}

public sealed class EmailNotifier : INotifier
{
    public string Send(string message) => $"email:{message}";
}

public sealed class SmsDecorator(INotifier wrapped) : INotifier
{
    public string Send(string message) => $"{wrapped.Send(message)}|sms:{message}";
}

public sealed class SlackDecorator(INotifier wrapped) : INotifier
{
    public string Send(string message) => $"{wrapped.Send(message)}|slack:{message}";
}

public static class DecoratorPattern
{
    public static string Demo() => new SlackDecorator(new SmsDecorator(new EmailNotifier())).Send("build complete");
}
