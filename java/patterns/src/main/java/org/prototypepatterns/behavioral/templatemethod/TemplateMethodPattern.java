package org.prototypepatterns.behavioral.templatemethod;

import java.util.List;

public final class TemplateMethodPattern {
    private TemplateMethodPattern() {
    }

    abstract static class DataPipeline {
        final List<String> run() {
            return List.of(read(), transform(), write());
        }

        abstract String read();

        abstract String transform();

        abstract String write();
    }

    static final class CsvPipeline extends DataPipeline {
        @Override
        String read() {
            return "read:csv";
        }

        @Override
        String transform() {
            return "transform:normalize";
        }

        @Override
        String write() {
            return "write:warehouse";
        }
    }

    public static List<String> demo() {
        return new CsvPipeline().run();
    }
}
