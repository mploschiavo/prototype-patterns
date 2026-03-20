namespace PrototypePatterns.Creational.FactoryMethod;

public interface IButton
{
    string Render();
}

public sealed class HtmlButton : IButton
{
    public string Render() => "<button>Submit</button>";
}

public sealed class DesktopButton : IButton
{
    public string Render() => "[DesktopButton: Submit]";
}

public abstract class Dialog
{
    protected abstract IButton CreateButton();

    public string RenderDialog() => CreateButton().Render();
}

public sealed class WebDialog : Dialog
{
    protected override IButton CreateButton() => new HtmlButton();
}

public sealed class DesktopDialog : Dialog
{
    protected override IButton CreateButton() => new DesktopButton();
}

public static class FactoryMethodPattern
{
    public static IReadOnlyList<string> Demo() => [new WebDialog().RenderDialog(), new DesktopDialog().RenderDialog()];
}
