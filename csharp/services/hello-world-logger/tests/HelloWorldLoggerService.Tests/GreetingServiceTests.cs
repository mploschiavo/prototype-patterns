using Microsoft.Extensions.Logging;

namespace HelloWorldLoggerService.Tests;

public sealed class GreetingServiceTests
{
    [Fact]
    public void BuildMessage_ReturnsHelloWorldWithLogger()
    {
        var logger = new CaptureLogger();

        var message = GreetingService.BuildMessage(logger);

        Assert.Equal("hello world with logger", message);
        Assert.Contains(logger.Messages, entry => entry.Contains("Handling hello-world-logger request"));
    }

    private sealed class CaptureLogger : ILogger
    {
        public List<string> Messages { get; } = [];

        public IDisposable? BeginScope<TState>(TState state) where TState : notnull => null;

        public bool IsEnabled(LogLevel logLevel) => true;

        public void Log<TState>(
            LogLevel logLevel,
            EventId eventId,
            TState state,
            Exception? exception,
            Func<TState, Exception?, string> formatter)
        {
            Messages.Add(formatter(state, exception));
        }
    }
}
