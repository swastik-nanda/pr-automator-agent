"""Service for local git repository inspection."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass


@dataclass
class GitFileChange:
    """Represent a changed file reported by git status."""

    status: str
    path: str


class GitService:
    """Provide read-only helpers for local git repository state."""

    def get_current_branch(self) -> str:
        """Return the current git branch name."""
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def get_working_tree_changes(self) -> list[GitFileChange]:
        """Return the list of changed files in the working tree."""
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            check=True,
            capture_output=True,
            text=True,
        )
        changes: list[GitFileChange] = []

        for line in result.stdout.splitlines():
            if not line.strip():
                continue

            status_code = line[:2]
            path = line[3:]
            changes.append(
                GitFileChange(
                    status=self._map_status_code(status_code),
                    path=path,
                )
            )

        return changes

    def _map_status_code(self, status_code: str) -> str:
        """Convert git porcelain status codes into readable labels."""
        if status_code == "??":
            return "untracked"

        if "A" in status_code:
            return "added"

        if "M" in status_code:
            return "modified"

        if "D" in status_code:
            return "deleted"

        if "R" in status_code:
            return "renamed"

        return f"changed ({status_code.strip() or 'unknown'})"
