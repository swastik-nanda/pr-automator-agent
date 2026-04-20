"""Starter for the PR automator agent workflows."""

from __future__ import annotations

from services.git_service import GitService
from services.story_resolution_service import StoryResolutionService


class AgentStarter:
    """Coordinate top-level CLI workflows for the agent."""

    def __init__(self) -> None:
        self.git_service = GitService()
        self.story_resolution_service = StoryResolutionService()

    def run(self, args) -> int:
        """Dispatch parsed CLI arguments to the selected workflow."""
        if args.command == "submit":
            branch_name = self.git_service.get_current_branch()
            changes = self.git_service.get_working_tree_changes()

            print(f"Current branch: {branch_name}")
            if changes:
                print("Working tree changes:")
                for change in changes:
                    print(f"- {change.status}: {change.path}")
            else:
                print("Working tree changes: none")

            if not self.story_resolution_service.validate_story_id(args.story):
                print(
                    "Error: invalid story format. Expected something like B-12345."
                )
                return 1

            print(f"Submit command accepted for story: {args.story}")
            return 0

        if args.command == "review":
            print("Command: review")
            return 0

        raise ValueError(f"Unsupported command: {args.command}")
