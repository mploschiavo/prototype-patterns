package org.prototypepatterns.behavioral.strategy;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public final class StrategyPattern {
    private StrategyPattern() {
    }

    interface SortStrategy {
        List<Integer> sort(List<Integer> data);
    }

    static final class AscendingSort implements SortStrategy {
        @Override
        public List<Integer> sort(List<Integer> data) {
            List<Integer> copy = new ArrayList<>(data);
            copy.sort(Comparator.naturalOrder());
            return copy;
        }
    }

    static final class DescendingSort implements SortStrategy {
        @Override
        public List<Integer> sort(List<Integer> data) {
            List<Integer> copy = new ArrayList<>(data);
            copy.sort(Comparator.reverseOrder());
            return copy;
        }
    }

    static final class SortContext {
        private SortStrategy strategy;

        SortContext(SortStrategy strategy) {
            this.strategy = strategy;
        }

        void setStrategy(SortStrategy strategy) {
            this.strategy = strategy;
        }

        List<Integer> run(List<Integer> data) {
            return strategy.sort(data);
        }
    }

    public static List<List<Integer>> demo() {
        SortContext context = new SortContext(new AscendingSort());
        List<Integer> ascending = context.run(List.of(3, 1, 2));
        context.setStrategy(new DescendingSort());
        List<Integer> descending = context.run(List.of(3, 1, 2));
        return List.of(ascending, descending);
    }
}
