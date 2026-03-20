namespace KafkaHaClients;

public static class Program
{
    public static async Task Main(string[] args)
    {
        var bootstrap = Environment.GetEnvironmentVariable("KAFKA_BOOTSTRAP_SERVERS") ?? "localhost:9092,localhost:9094,localhost:9096";
        var topic = Environment.GetEnvironmentVariable("KAFKA_TOPIC") ?? "prototype-topic-ha";

        if (args.FirstOrDefault() == "consume")
        {
            var message = ConsumerClient.ConsumeOnce(bootstrap, topic, "csharp-kafka-ha-consumer", TimeSpan.FromSeconds(5));
            Console.WriteLine($"received: {message}");
            return;
        }

        var payload = ProducerClient.BuildMessage("1", "hello from csharp kafka ha producer");
        await ProducerClient.SendMessageAsync(bootstrap, topic, payload);
        Console.WriteLine($"sent: {payload}");
    }
}
