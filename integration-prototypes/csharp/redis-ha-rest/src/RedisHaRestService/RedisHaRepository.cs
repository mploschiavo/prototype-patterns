using StackExchange.Redis;

namespace RedisHaRestService;

public sealed class RedisHaRepository
{
    private readonly string _endpoints = Environment.GetEnvironmentVariable("REDIS_CLUSTER_ENDPOINTS")
        ?? "localhost:6379,localhost:6380,localhost:6381";

    public static IReadOnlyList<string> ParseEndpoints(string endpoints)
    {
        return endpoints.Split(',').Select(endpoint => endpoint.Trim()).Where(endpoint => endpoint.Length > 0).ToArray();
    }

    public async Task<string?> FetchValueAsync(string key)
    {
        var options = new ConfigurationOptions
        {
            AbortOnConnectFail = false,
            AllowAdmin = true
        };

        foreach (var endpoint in ParseEndpoints(_endpoints))
        {
            options.EndPoints.Add(endpoint);
        }

        await using var connection = await ConnectionMultiplexer.ConnectAsync(options);
        var db = connection.GetDatabase();
        var value = await db.StringGetAsync(key);
        return value.IsNull ? null : value.ToString();
    }
}
