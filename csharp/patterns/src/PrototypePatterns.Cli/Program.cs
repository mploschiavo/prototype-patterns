using System.Text.Json;
using PrototypePatterns;

namespace PrototypePatterns.Cli;

internal static class Program
{
    private static int Main(string[] args)
    {
        if (args.Length == 1 && args[0] == "--list")
        {
            foreach (var pattern in PatternRegistry.List())
            {
                Console.WriteLine($"{pattern.Id}\t{pattern.Category}");
            }

            return 0;
        }

        if (args.Length == 1 && args[0] == "--all")
        {
            foreach (var entry in PatternRegistry.RunAllPatterns())
            {
                Console.WriteLine($"{entry.Key}: {FormatResult(entry.Value)}");
            }

            return 0;
        }

        if (args.Length == 2 && args[0] == "--pattern")
        {
            try
            {
                var result = PatternRegistry.RunPattern(args[1]);
                Console.WriteLine($"{args[1]}: {FormatResult(result)}");
            }
            catch (ArgumentException exception)
            {
                Console.Error.WriteLine(exception.Message);
                return 2;
            }

            return 0;
        }

        Console.Error.WriteLine("Usage:");
        Console.Error.WriteLine("  ./scripts/run-pattern.sh --list");
        Console.Error.WriteLine("  ./scripts/run-pattern.sh --pattern <pattern-id>");
        Console.Error.WriteLine("  ./scripts/run-pattern.sh --all");
        return 1;
    }

    private static string FormatResult(object? result)
    {
        return result switch
        {
            null => "null",
            string text => text,
            _ => JsonSerializer.Serialize(result)
        };
    }
}
