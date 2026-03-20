package org.prototypepatterns;

import java.util.List;
import org.prototypepatterns.behavioral.chainofresponsibility.ChainOfResponsibilityPattern;
import org.prototypepatterns.behavioral.command.CommandPattern;
import org.prototypepatterns.behavioral.iterator.IteratorPattern;
import org.prototypepatterns.behavioral.mediator.MediatorPattern;
import org.prototypepatterns.behavioral.memento.MementoPattern;
import org.prototypepatterns.behavioral.observer.ObserverPattern;
import org.prototypepatterns.behavioral.state.StatePattern;
import org.prototypepatterns.behavioral.strategy.StrategyPattern;
import org.prototypepatterns.behavioral.templatemethod.TemplateMethodPattern;
import org.prototypepatterns.creational.abstractfactory.AbstractFactoryPattern;
import org.prototypepatterns.creational.builder.BuilderPattern;
import org.prototypepatterns.creational.factorymethod.FactoryMethodPattern;
import org.prototypepatterns.creational.lazyinitialization.LazyInitializationPattern;
import org.prototypepatterns.creational.objectpool.ObjectPoolPattern;
import org.prototypepatterns.creational.prototypepattern.PrototypePattern;
import org.prototypepatterns.creational.singleton.SingletonPattern;
import org.prototypepatterns.structural.adapter.AdapterPattern;
import org.prototypepatterns.structural.bridge.BridgePattern;
import org.prototypepatterns.structural.composite.CompositePattern;
import org.prototypepatterns.structural.compositeentity.CompositeEntityPattern;
import org.prototypepatterns.structural.decorator.DecoratorPattern;
import org.prototypepatterns.structural.facade.FacadePattern;
import org.prototypepatterns.structural.flyweight.FlyweightPattern;
import org.prototypepatterns.structural.proxy.ProxyPattern;

public final class PatternTests {
    private static int passed = 0;

    private PatternTests() {
    }

    private static void assertTrue(boolean condition, String message) {
        if (!condition) {
            throw new IllegalStateException(message);
        }
        passed++;
    }

    private static void assertEquals(Object expected, Object actual, String message) {
        assertTrue(expected.equals(actual), message + " expected=" + expected + " actual=" + actual);
    }

    private static void assertDouble(double expected, double actual, String message) {
        assertTrue(Math.abs(expected - actual) < 0.0001, message + " expected=" + expected + " actual=" + actual);
    }

    public static void main(String[] args) {
        assertTrue(SingletonPattern.demo(), "singleton");
        assertEquals(List.of("<button>Submit</button>", "[DesktopButton: Submit]"), FactoryMethodPattern.demo(), "factory method");
        assertEquals(List.of("dark-button", "dark-checkbox"), AbstractFactoryPattern.demo(), "abstract factory");
        BuilderPattern.House house = BuilderPattern.demo();
        assertEquals(List.of("Kitchen", "Office"), house.rooms, "builder rooms");
        assertTrue(house.hasGarage, "builder garage");
        assertTrue(PrototypePattern.demo(), "prototype");
        assertTrue(ObjectPoolPattern.demo(), "object pool");
        assertTrue(LazyInitializationPattern.demo(), "lazy initialization");

        assertDouble(25.0, AdapterPattern.demo(), "adapter");
        assertEquals("email:build complete|sms:build complete|slack:build complete", DecoratorPattern.demo(), "decorator");
        assertTrue(CompositePattern.demo() == 30, "composite");
        assertTrue(FacadePattern.demo().contains("projector on"), "facade");
        assertTrue(ProxyPattern.demo(), "proxy");
        assertEquals(List.of("vector-circle:5", "raster-circle:5"), BridgePattern.demo(), "bridge");
        assertTrue(FlyweightPattern.demo(), "flyweight");
        assertEquals(List.of("Sam", "Austin"), CompositeEntityPattern.demo(), "composite entity");

        assertEquals(List.of(7), ObserverPattern.demo(), "observer");
        assertEquals(List.of(List.of(1, 2, 3), List.of(3, 2, 1)), StrategyPattern.demo(), "strategy");
        assertEquals("light:on", CommandPattern.demo(), "command");
        assertEquals(List.of("pending->paid", "paid->shipped", "shipped->shipped"), StatePattern.demo(), "state");
        assertEquals(List.of("read:csv", "transform:normalize", "write:warehouse"), TemplateMethodPattern.demo(), "template method");
        assertEquals(List.of("team-lead", "manager", "unhandled:4"), ChainOfResponsibilityPattern.demo(), "chain of responsibility");
        assertEquals(List.of("intro", "verse", "outro"), IteratorPattern.demo(), "iterator");
        assertEquals(List.of("alex:ready"), MediatorPattern.demo(), "mediator");
        assertEquals("draft", MementoPattern.demo(), "memento");

        assertTrue(PatternRegistry.list().size() == 24, "registry size");
        assertEquals(true, PatternRegistry.runPattern("singleton"), "registry singleton");
        assertEquals(List.of("team-lead", "manager", "unhandled:4"), PatternRegistry.runPattern("chain of responsibility"),
                "registry normalized id");
        assertTrue(PatternRegistry.runAllPatterns().size() == 24, "registry all");

        System.out.println("Java pattern tests passed: " + passed);
    }
}
