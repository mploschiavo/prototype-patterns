namespace HelloWorldService.Tests;

public sealed class GreetingServiceTests
{
    [Fact]
    public void BuildMessage_ReturnsHelloWorld()
    {
        Assert.Equal("hello world", GreetingService.BuildMessage());
    }
}
