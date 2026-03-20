using PostgresRestService;

namespace PostgresRestService.Tests;

public sealed class PostgresTests
{
    [Fact]
    public void DemoItem_StoresExpectedValues()
    {
        var item = new DemoItem(1, "alpha", "seed row alpha");
        Assert.Equal(1, item.Id);
        Assert.Equal("alpha", item.Name);
    }
}
