using KafkaHaClients;

namespace KafkaHaClients.Tests;

public sealed class KafkaHaTests
{
    [Fact]
    public void BuildMessage_FormatsExpectedJson()
    {
        Assert.Equal("{\"id\":\"1\",\"text\":\"hello\"}", ProducerClient.BuildMessage("1", "hello"));
    }
}
