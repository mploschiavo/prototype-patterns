using System.Text.RegularExpressions;
using PrototypePatterns.Behavioral.ChainOfResponsibility;
using PrototypePatterns.Behavioral.Command;
using PrototypePatterns.Behavioral.Iterator;
using PrototypePatterns.Behavioral.Mediator;
using PrototypePatterns.Behavioral.Memento;
using PrototypePatterns.Behavioral.Observer;
using PrototypePatterns.Behavioral.State;
using PrototypePatterns.Behavioral.Strategy;
using PrototypePatterns.Behavioral.TemplateMethod;
using PrototypePatterns.Creational.AbstractFactory;
using PrototypePatterns.Creational.Builder;
using PrototypePatterns.Creational.FactoryMethod;
using PrototypePatterns.Creational.LazyInitialization;
using PrototypePatterns.Creational.ObjectPool;
using PrototypePatterns.Creational.Prototype;
using PrototypePatterns.Creational.Singleton;
using PrototypePatterns.Structural.Adapter;
using PrototypePatterns.Structural.Bridge;
using PrototypePatterns.Structural.Composite;
using PrototypePatterns.Structural.CompositeEntity;
using PrototypePatterns.Structural.Decorator;
using PrototypePatterns.Structural.Facade;
using PrototypePatterns.Structural.Flyweight;
using PrototypePatterns.Structural.Proxy;

namespace PrototypePatterns;

public sealed record PatternEntry(string Id, string Category, Func<object?> Demo);

public static class PatternRegistry
{
    private static readonly IReadOnlyList<PatternEntry> Patterns =
    [
        new("singleton", "creational", () => SingletonPattern.Demo()),
        new("factory-method", "creational", () => FactoryMethodPattern.Demo()),
        new("abstract-factory", "creational", () => AbstractFactoryPattern.Demo()),
        new("builder", "creational", () => BuilderPattern.Demo()),
        new("prototype", "creational", () => PrototypePattern.Demo()),
        new("object-pool", "creational", () => ObjectPoolPattern.Demo()),
        new("lazy-initialization", "creational", () => LazyInitializationPattern.Demo()),
        new("adapter", "structural", () => AdapterPattern.Demo()),
        new("decorator", "structural", () => DecoratorPattern.Demo()),
        new("composite", "structural", () => CompositePattern.Demo()),
        new("facade", "structural", () => FacadePattern.Demo()),
        new("proxy", "structural", () => ProxyPattern.Demo()),
        new("bridge", "structural", () => BridgePattern.Demo()),
        new("flyweight", "structural", () => FlyweightPattern.Demo()),
        new("composite-entity", "structural", () => CompositeEntityPattern.Demo()),
        new("observer", "behavioral", () => ObserverPattern.Demo()),
        new("strategy", "behavioral", () => StrategyPattern.Demo()),
        new("command", "behavioral", () => CommandPattern.Demo()),
        new("state", "behavioral", () => StatePattern.Demo()),
        new("template-method", "behavioral", () => TemplateMethodPattern.Demo()),
        new("chain-of-responsibility", "behavioral", () => ChainOfResponsibilityPattern.Demo()),
        new("iterator", "behavioral", () => IteratorPattern.Demo()),
        new("mediator", "behavioral", () => MediatorPattern.Demo()),
        new("memento", "behavioral", () => MementoPattern.Demo())
    ];

    private static readonly IReadOnlyDictionary<string, PatternEntry> PatternById =
        Patterns.ToDictionary(pattern => pattern.Id, pattern => pattern);

    public static string NormalizePatternId(string patternId)
    {
        var normalized = patternId.Trim().ToLowerInvariant().Replace('_', ' ');
        return Regex.Replace(normalized, @"\s+", "-");
    }

    public static IReadOnlyList<PatternEntry> List() => Patterns;

    public static object? RunPattern(string patternId)
    {
        var normalized = NormalizePatternId(patternId);
        if (!PatternById.TryGetValue(normalized, out var pattern))
        {
            throw new ArgumentException($"Unknown pattern: {patternId}", nameof(patternId));
        }

        return pattern.Demo();
    }

    public static IReadOnlyDictionary<string, object?> RunAllPatterns()
    {
        var results = new Dictionary<string, object?>();
        foreach (var pattern in Patterns)
        {
            results[pattern.Id] = pattern.Demo();
        }

        return results;
    }
}
