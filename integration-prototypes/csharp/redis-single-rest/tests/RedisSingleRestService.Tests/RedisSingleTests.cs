namespace RedisSingleRestService.Tests;

public sealed class RedisSingleTests
{
    [Fact]
    public void KeyValueEnvelopeShape_IsStable()
    {
        var payload = new { key = "demo:key", value = "hello" };
        Assert.Equal("demo:key", payload.key);
        Assert.Equal("hello", payload.value);
    }
}
