using Confluent.Kafka;

namespace KafkaHaClients;

public static class ConsumerClient
{
    public static string? ConsumeOnce(string bootstrapServers, string topic, string groupId, TimeSpan timeout)
    {
        var config = new ConsumerConfig
        {
            BootstrapServers = bootstrapServers,
            GroupId = groupId,
            AutoOffsetReset = AutoOffsetReset.Earliest
        };

        using var consumer = new ConsumerBuilder<Ignore, string>(config).Build();
        consumer.Subscribe(topic);
        var result = consumer.Consume(timeout);
        return result?.Message.Value;
    }
}
