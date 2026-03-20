var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => GreetingService.BuildMessage());

app.Run();

public static class GreetingService
{
    public static string BuildMessage() => "hello world";
}

public partial class Program
{
}
