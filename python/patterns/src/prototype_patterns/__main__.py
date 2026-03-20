"""CLI for running one design pattern demo at a time."""

from __future__ import annotations

import argparse
import sys

from prototype_patterns.pattern_runner import format_result, list_patterns, run_all_patterns, run_pattern


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run prototype pattern demos one pattern at a time.")
    parser.add_argument("--list", action="store_true", help="List available pattern ids.")
    parser.add_argument("--all", action="store_true", help="Run all patterns.")
    parser.add_argument("--pattern", type=str, help="Run one pattern, e.g. singleton or chain-of-responsibility.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list:
        for pattern_id, category in list_patterns():
            print(f"{pattern_id}\t{category}")
        return 0

    if args.all:
        for pattern_id, result in run_all_patterns().items():
            print(f"{pattern_id}: {format_result(result)}")
        return 0

    if args.pattern:
        try:
            result = run_pattern(args.pattern)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2
        print(f"{args.pattern}: {format_result(result)}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
