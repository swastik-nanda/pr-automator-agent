"""CLI entrypoint for the PR automator agent."""

from __future__ import annotations

import argparse
from typing import Sequence

from starter.agent_starter import AgentStarter


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="agent",
        description="PR automator agent CLI",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    submit_parser = subparsers.add_parser(
        "submit",
        help="Submit code changes for review",
    )
    submit_parser.add_argument(
        "--story",
        required=True,
        help="Agility story identifier, for example B-12345",
    )

    subparsers.add_parser(
        "review",
        help="Run review flow for the current repository",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Parse CLI arguments and delegate to the agent starter."""
    parser = build_parser()
    args = parser.parse_args(argv)
    starter = AgentStarter()
    return starter.run(args)


if __name__ == "__main__":
    raise SystemExit(main())
