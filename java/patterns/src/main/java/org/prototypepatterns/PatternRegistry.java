package org.prototypepatterns;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Supplier;
import java.util.stream.Collectors;
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

public final class PatternRegistry {
    public record PatternEntry(String id, String category, Supplier<Object> demo) {
    }

    private static final List<PatternEntry> PATTERNS = List.of(
            new PatternEntry("singleton", "creational", () -> SingletonPattern.demo()),
            new PatternEntry("factory-method", "creational", () -> FactoryMethodPattern.demo()),
            new PatternEntry("abstract-factory", "creational", () -> AbstractFactoryPattern.demo()),
            new PatternEntry("builder", "creational", () -> BuilderPattern.demo()),
            new PatternEntry("prototype", "creational", () -> PrototypePattern.demo()),
            new PatternEntry("object-pool", "creational", () -> ObjectPoolPattern.demo()),
            new PatternEntry("lazy-initialization", "creational", () -> LazyInitializationPattern.demo()),
            new PatternEntry("adapter", "structural", () -> AdapterPattern.demo()),
            new PatternEntry("decorator", "structural", () -> DecoratorPattern.demo()),
            new PatternEntry("composite", "structural", () -> CompositePattern.demo()),
            new PatternEntry("facade", "structural", () -> FacadePattern.demo()),
            new PatternEntry("proxy", "structural", () -> ProxyPattern.demo()),
            new PatternEntry("bridge", "structural", () -> BridgePattern.demo()),
            new PatternEntry("flyweight", "structural", () -> FlyweightPattern.demo()),
            new PatternEntry("composite-entity", "structural", () -> CompositeEntityPattern.demo()),
            new PatternEntry("observer", "behavioral", () -> ObserverPattern.demo()),
            new PatternEntry("strategy", "behavioral", () -> StrategyPattern.demo()),
            new PatternEntry("command", "behavioral", () -> CommandPattern.demo()),
            new PatternEntry("state", "behavioral", () -> StatePattern.demo()),
            new PatternEntry("template-method", "behavioral", () -> TemplateMethodPattern.demo()),
            new PatternEntry("chain-of-responsibility", "behavioral", () -> ChainOfResponsibilityPattern.demo()),
            new PatternEntry("iterator", "behavioral", () -> IteratorPattern.demo()),
            new PatternEntry("mediator", "behavioral", () -> MediatorPattern.demo()),
            new PatternEntry("memento", "behavioral", () -> MementoPattern.demo()));

    private static final Map<String, PatternEntry> PATTERN_BY_ID = PATTERNS.stream()
            .collect(Collectors.toMap(PatternEntry::id, entry -> entry));

    private PatternRegistry() {
    }

    public static String normalizePatternId(String patternId) {
        return patternId.strip().toLowerCase().replace('_', ' ').replaceAll("\\s+", "-");
    }

    public static List<PatternEntry> list() {
        return PATTERNS;
    }

    public static Object runPattern(String patternId) {
        String normalized = normalizePatternId(patternId);
        PatternEntry entry = PATTERN_BY_ID.get(normalized);
        if (entry == null) {
            throw new IllegalArgumentException("Unknown pattern: " + patternId);
        }
        return entry.demo().get();
    }

    public static Map<String, Object> runAllPatterns() {
        Map<String, Object> results = new LinkedHashMap<>();
        for (PatternEntry entry : PATTERNS) {
            results.put(entry.id(), entry.demo().get());
        }
        return results;
    }
}
