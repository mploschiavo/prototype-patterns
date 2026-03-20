# Java Design Pattern Prototypes

Academic-style examples for 24 patterns using package-per-pattern organization.

## Structure

- `src/main/java/org/prototypepatterns/creational/*`
- `src/main/java/org/prototypepatterns/structural/*`
- `src/main/java/org/prototypepatterns/behavioral/*`
- `src/test/java/org/prototypepatterns/PatternTests.java`

## Run Tests

```bash
./scripts/test.sh
```

This requires a JDK with `javac` (not just a JRE).

## Explore One Pattern At A Time

List all patterns:

```bash
./scripts/run-pattern.sh --list
```

Run one pattern:

```bash
./scripts/run-pattern.sh --pattern singleton
./scripts/run-pattern.sh --pattern "chain of responsibility"
```

Run all patterns:

```bash
./scripts/run-pattern.sh --all
```
