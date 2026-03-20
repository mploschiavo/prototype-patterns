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

namespace PrototypePatterns.Tests;

public sealed class PatternTests
{
    [Fact]
    public void Singleton() => Assert.True(SingletonPattern.Demo());

    [Fact]
    public void FactoryMethod() => Assert.Equal(["<button>Submit</button>", "[DesktopButton: Submit]"], FactoryMethodPattern.Demo());

    [Fact]
    public void AbstractFactory() => Assert.Equal(["dark-button", "dark-checkbox"], AbstractFactoryPattern.Demo());

    [Fact]
    public void Builder()
    {
        var house = BuilderPattern.Demo();
        Assert.Equal(["Kitchen", "Office"], house.Rooms);
        Assert.True(house.HasGarage);
    }

    [Fact]
    public void Prototype() => Assert.True(PrototypePattern.Demo());

    [Fact]
    public void ObjectPool() => Assert.True(ObjectPoolPattern.Demo());

    [Fact]
    public void LazyInitialization() => Assert.True(LazyInitializationPattern.Demo());

    [Fact]
    public void Adapter() => Assert.Equal(25.0, AdapterPattern.Demo());

    [Fact]
    public void Decorator() => Assert.Equal("email:build complete|sms:build complete|slack:build complete", DecoratorPattern.Demo());

    [Fact]
    public void Composite() => Assert.Equal(30, CompositePattern.Demo());

    [Fact]
    public void Facade() => Assert.Contains("projector on", FacadePattern.Demo());

    [Fact]
    public void Proxy() => Assert.True(ProxyPattern.Demo());

    [Fact]
    public void Bridge() => Assert.Equal(["vector-circle:5", "raster-circle:5"], BridgePattern.Demo());

    [Fact]
    public void Flyweight() => Assert.True(FlyweightPattern.Demo());

    [Fact]
    public void CompositeEntity() => Assert.Equal(["Sam", "Austin"], CompositeEntityPattern.Demo());

    [Fact]
    public void Observer() => Assert.Equal([7], ObserverPattern.Demo());

    [Fact]
    public void Strategy() => Assert.Equal([[1, 2, 3], [3, 2, 1]], StrategyPattern.Demo());

    [Fact]
    public void Command() => Assert.Equal("light:on", CommandPattern.Demo());

    [Fact]
    public void State() => Assert.Equal(["pending->paid", "paid->shipped", "shipped->shipped"], StatePattern.Demo());

    [Fact]
    public void TemplateMethod() => Assert.Equal(["read:csv", "transform:normalize", "write:warehouse"], TemplateMethodPattern.Demo());

    [Fact]
    public void ChainOfResponsibility() => Assert.Equal(["team-lead", "manager", "unhandled:4"], ChainOfResponsibilityPattern.Demo());

    [Fact]
    public void Iterator() => Assert.Equal(["intro", "verse", "outro"], IteratorPattern.Demo());

    [Fact]
    public void Mediator() => Assert.Equal(["alex:ready"], MediatorPattern.Demo());

    [Fact]
    public void Memento() => Assert.Equal("draft", MementoPattern.Demo());
}
