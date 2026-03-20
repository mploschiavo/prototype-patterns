using Confluent.Kafka;

namespace KafkaHaClients;

public static class ProducerClient
{
    public static string BuildMessage(string id, string text) => $"{{\"id\":\"{id}\",\"text\":\"{text}\"}}";

    public static async Task SendMessageAsync(string bootstrapServers, string topic, string message)
    {
        var config = new ProducerConfig { BootstrapServers = bootstrapServers };
        using var producer = new ProducerBuilder<Null, string>(config).Build();
        await producer.ProduceAsync(topic, new Message<Null, string> { Value = message });
        producer.Flush(TimeSpan.FromSeconds(5));
    }
}
