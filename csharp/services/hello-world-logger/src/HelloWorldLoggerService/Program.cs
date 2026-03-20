using Microsoft.Extensions.Logging;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", (ILoggerFactory loggerFactory) =>
{
    var logger = loggerFactory.CreateLogger("hello-world-logger");
    return GreetingService.BuildMessage(logger);
});

app.Run();

public static class GreetingService
{
    public static string BuildMessage(ILogger? logger = null)
    {
        logger?.LogInformation("Handling hello-world-logger request");
        return "hello world with logger";
    }
}

public partial class Program
{
}
