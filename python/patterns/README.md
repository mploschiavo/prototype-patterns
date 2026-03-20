# Python Design Pattern Prototypes

Academic-style examples for 24 patterns.

## Structure

- `src/prototype_patterns/creational/*`
- `src/prototype_patterns/structural/*`
- `src/prototype_patterns/behavioral/*`
- `tests/test_patterns.py` (pytest style)
- `tests/test_patterns_unittest.py` (stdlib unittest)

## Run Tests

Using stdlib only:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_patterns_unittest.py' -v
```

Using pytest (optional):

```bash
python3 -m pytest -q
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
