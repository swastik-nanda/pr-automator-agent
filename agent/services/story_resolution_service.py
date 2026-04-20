"""Story resolution and validation service."""

from __future__ import annotations

import re


class StoryResolutionService:
    """Handle story identifier validation logic."""

    STORY_PATTERN = re.compile(r"^[A-Z]-\d+$")

    def validate_story_id(self, story_id: str) -> bool:
        """Return True when the story identifier matches the expected format."""
        if not story_id:
            return False

        return bool(self.STORY_PATTERN.fullmatch(story_id.strip()))
