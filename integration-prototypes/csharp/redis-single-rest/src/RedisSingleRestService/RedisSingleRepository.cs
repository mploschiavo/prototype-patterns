using StackExchange.Redis;

namespace RedisSingleRestService;

public sealed class RedisSingleRepository
{
    private readonly string _connection = Environment.GetEnvironmentVariable("REDIS_CONNECTION") ?? "localhost:6379";

    public async Task<string?> FetchValueAsync(string key)
    {
        await using var connection = await ConnectionMultiplexer.ConnectAsync(_connection);
        var db = connection.GetDatabase();
        var value = await db.StringGetAsync(key);
        return value.IsNull ? null : value.ToString();
    }
}
