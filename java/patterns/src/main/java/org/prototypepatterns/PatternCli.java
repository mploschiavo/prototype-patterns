package org.prototypepatterns;

import java.util.Map;
import org.prototypepatterns.creational.builder.BuilderPattern;

public final class PatternCli {
    private PatternCli() {
    }

    public static void main(String[] args) {
        int exitCode = run(args);
        if (exitCode != 0) {
            System.exit(exitCode);
        }
    }

    static int run(String[] args) {
        if (args.length == 1 && "--list".equals(args[0])) {
            for (PatternRegistry.PatternEntry entry : PatternRegistry.list()) {
                System.out.println(entry.id() + "\t" + entry.category());
            }
            return 0;
        }

        if (args.length == 1 && "--all".equals(args[0])) {
            for (Map.Entry<String, Object> result : PatternRegistry.runAllPatterns().entrySet()) {
                System.out.println(result.getKey() + ": " + formatResult(result.getValue()));
            }
            return 0;
        }

        if (args.length == 2 && "--pattern".equals(args[0])) {
            String patternId = args[1];
            try {
                Object result = PatternRegistry.runPattern(patternId);
                System.out.println(patternId + ": " + formatResult(result));
            } catch (IllegalArgumentException exception) {
                System.err.println(exception.getMessage());
                return 2;
            }
            return 0;
        }

        printUsage();
        return 1;
    }

    private static void printUsage() {
        System.err.println("Usage:");
        System.err.println("  ./scripts/run-pattern.sh --list");
        System.err.println("  ./scripts/run-pattern.sh --pattern <pattern-id>");
        System.err.println("  ./scripts/run-pattern.sh --all");
    }

    private static String formatResult(Object result) {
        if (result instanceof BuilderPattern.House house) {
            return "{rooms=" + house.rooms + ", hasGarage=" + house.hasGarage + ", hasGarden=" + house.hasGarden + "}";
        }
        return String.valueOf(result);
    }
}
