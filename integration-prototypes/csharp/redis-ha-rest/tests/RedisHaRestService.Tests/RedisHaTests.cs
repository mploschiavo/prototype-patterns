using RedisHaRestService;

namespace RedisHaRestService.Tests;

public sealed class RedisHaTests
{
    [Fact]
    public void ParseEndpoints_ReturnsAllNodes()
    {
        var parsed = RedisHaRepository.ParseEndpoints("localhost:6379,localhost:6380,localhost:6381");
        Assert.Equal(3, parsed.Count);
    }
}
