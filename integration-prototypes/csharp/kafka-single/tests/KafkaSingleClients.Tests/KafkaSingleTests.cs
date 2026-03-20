using KafkaSingleClients;

namespace KafkaSingleClients.Tests;

public sealed class KafkaSingleTests
{
    [Fact]
    public void BuildMessage_FormatsExpectedJson()
    {
        Assert.Equal("{\"id\":\"1\",\"text\":\"hello\"}", ProducerClient.BuildMessage("1", "hello"));
    }
}
