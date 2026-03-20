namespace PrototypePatterns.Creational.AbstractFactory;

public interface IThemeButton
{
    string Paint();
}

public interface IThemeCheckbox
{
    string Paint();
}

public interface IThemeFactory
{
    IThemeButton CreateButton();
    IThemeCheckbox CreateCheckbox();
}

public sealed class DarkButton : IThemeButton
{
    public string Paint() => "dark-button";
}

public sealed class DarkCheckbox : IThemeCheckbox
{
    public string Paint() => "dark-checkbox";
}

public sealed class DarkThemeFactory : IThemeFactory
{
    public IThemeButton CreateButton() => new DarkButton();

    public IThemeCheckbox CreateCheckbox() => new DarkCheckbox();
}

public static class AbstractFactoryPattern
{
    public static IReadOnlyList<string> Demo()
    {
        IThemeFactory factory = new DarkThemeFactory();
        return [factory.CreateButton().Paint(), factory.CreateCheckbox().Paint()];
    }
}
