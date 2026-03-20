namespace KafkaSingleClients;

public static class Program
{
    public static async Task Main(string[] args)
    {
        var bootstrap = Environment.GetEnvironmentVariable("KAFKA_BOOTSTRAP_SERVERS") ?? "localhost:9092";
        var topic = Environment.GetEnvironmentVariable("KAFKA_TOPIC") ?? "prototype-topic";

        if (args.FirstOrDefault() == "consume")
        {
            var message = ConsumerClient.ConsumeOnce(bootstrap, topic, "csharp-kafka-single-consumer", TimeSpan.FromSeconds(5));
            Console.WriteLine($"received: {message}");
            return;
        }

        var payload = ProducerClient.BuildMessage("1", "hello from csharp kafka single producer");
        await ProducerClient.SendMessageAsync(bootstrap, topic, payload);
        Console.WriteLine($"sent: {payload}");
    }
}
