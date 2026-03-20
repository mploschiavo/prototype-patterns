namespace PrototypePatterns.Behavioral.Command;

public interface ICommand
{
    string Execute();
}

public sealed class Light
{
    public string On() => "light:on";
}

public sealed class LightOnCommand(Light light) : ICommand
{
    public string Execute() => light.On();
}

public sealed class RemoteButton(ICommand command)
{
    public string Press() => command.Execute();
}

public static class CommandPattern
{
    public static string Demo() => new RemoteButton(new LightOnCommand(new Light())).Press();
}
