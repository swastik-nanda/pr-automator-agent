"""Starter for the PR automator agent workflows."""

from __future__ import annotations


class AgentStarter:
    """Coordinate top-level CLI workflows for the agent."""

    def run(self, args) -> int:
        """Dispatch parsed CLI arguments to the selected workflow."""
        if args.command == "submit":
            print(f"Command: submit | Story: {args.story}")
            return 0

        if args.command == "review":
            print("Command: review")
            return 0

        raise ValueError(f"Unsupported command: {args.command}")
