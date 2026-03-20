package org.prototypepatterns.creational.lazyinitialization;

import java.util.List;

public final class LazyInitializationPattern {
    private LazyInitializationPattern() {
    }

    public static final class LazyDataset {
        private List<String> records;
        private int loadCount;

        public List<String> records() {
            if (records == null) {
                loadCount++;
                records = List.of("row-1", "row-2", "row-3");
            }
            return records;
        }

        public int loadCount() {
            return loadCount;
        }
    }

    public static boolean demo() {
        LazyDataset dataset = new LazyDataset();
        dataset.records();
        dataset.records();
        return dataset.loadCount() == 1;
    }
}
