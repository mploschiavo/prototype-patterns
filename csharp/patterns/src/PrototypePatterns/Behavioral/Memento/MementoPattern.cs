namespace PrototypePatterns.Behavioral.Memento;

public sealed record Memento(string Text);

public sealed class TextEditor
{
    private string _text = string.Empty;

    public void Type(string value) => _text = value;

    public Memento Save() => new(_text);

    public void Restore(Memento memento) => _text = memento.Text;

    public string Text => _text;
}

public static class MementoPattern
{
    public static string Demo()
    {
        var editor = new TextEditor();
        editor.Type("draft");
        var checkpoint = editor.Save();
        editor.Type("final");
        editor.Restore(checkpoint);
        return editor.Text;
    }
}
