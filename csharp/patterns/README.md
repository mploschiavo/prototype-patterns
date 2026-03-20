# C# Design Pattern Prototypes

Academic-style examples for 24 GoF/J2EE-inspired patterns.

## Structure

- `src/PrototypePatterns/Creational/*`
- `src/PrototypePatterns/Structural/*`
- `src/PrototypePatterns/Behavioral/*`
- `tests/PrototypePatterns.Tests`: xUnit tests.

## Run Tests

```bash
dotnet test PrototypePatterns.sln
```

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
