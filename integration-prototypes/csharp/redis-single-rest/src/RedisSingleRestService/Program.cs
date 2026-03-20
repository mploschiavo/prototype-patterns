using RedisSingleRestService;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<RedisSingleRepository>();

var app = builder.Build();

app.MapGet("/value", async (string key, RedisSingleRepository repository) =>
{
    var value = await repository.FetchValueAsync(key);
    return value is null ? Results.NotFound(new { error = "key not found" }) : Results.Json(new { key, value });
});

app.Run();

public partial class Program;
