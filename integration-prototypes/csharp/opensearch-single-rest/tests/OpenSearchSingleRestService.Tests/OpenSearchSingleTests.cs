using OpenSearchSingleRestService;

namespace OpenSearchSingleRestService.Tests;

public sealed class OpenSearchSingleTests
{
    [Fact]
    public void ParseMessage_ReturnsValue_WhenFound()
    {
        var value = OpenSearchSingleRepository.ParseMessage("{\"found\":true,\"_source\":{\"message\":\"hello opensearch single\"}}");
        Assert.Equal("hello opensearch single", value);
    }

    [Fact]
    public void ParseMessage_ReturnsNull_WhenNotFound()
    {
        var value = OpenSearchSingleRepository.ParseMessage("{\"found\":false}");
        Assert.Null(value);
    }
}
