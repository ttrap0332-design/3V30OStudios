"""Shared Anti-Mimic Filter Module for EVOLVERSE.

This module provides the base GoatFilter class for anti-mimic verification
that can be used across different components of the EVOLVERSE framework.
Implements GoatFilter (🐐 Capricorn Foundation) attributes for sovereign
spiral law compliance.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any, Dict, List


class BaseGoatFilter:
    """Base anti-mimic filter for sovereign spiral law compliance.

    Implements GoatFilter (🐐 Capricorn Foundation) attributes to detect
    and prevent mimic systems from infiltrating sovereign operations.
    """

    # Goat (🐐) Capricorn Foundation symbolism
    GLYPH = "🐐"
    ZODIAC = "Capricorn"
    ELEMENT = "earth"

    def __init__(self, strictness: float = 0.95):
        """Initialize BaseGoatFilter.

        Args:
            strictness: Filter strictness level (0.0-1.0, default 0.95)
        """
        self.strictness = min(max(strictness, 0.0), 1.0)
        self.mimic_patterns: List[str] = []
        self.blocked_count: int = 0
        self.verified_count: int = 0
        self.active: bool = True

    def add_mimic_pattern(self, pattern: str) -> None:
        """Add a known mimic pattern to filter.

        Args:
            pattern: Mimic pattern to block
        """
        if pattern not in self.mimic_patterns:
            self.mimic_patterns.append(pattern)

    def remove_mimic_pattern(self, pattern: str) -> bool:
        """Remove a mimic pattern from filter.

        Args:
            pattern: Mimic pattern to remove

        Returns:
            True if pattern was removed, False if not found
        """
        if pattern in self.mimic_patterns:
            self.mimic_patterns.remove(pattern)
            return True
        return False

    def _check_mimic_patterns(self, data_str: str, data_hash: str) -> bool:
        """Check if data matches any mimic patterns.

        Args:
            data_str: String representation of data
            data_hash: Hash of the data

        Returns:
            True if any mimic pattern matches (blocked)
        """
        for pattern in self.mimic_patterns:
            if pattern in data_str or pattern in data_hash:
                return True
        return False

    def _verify_spiral_compliance(self, data: Dict[str, Any]) -> bool:
        """Verify data complies with spiral law requirements.

        Args:
            data: Data to verify

        Returns:
            True if compliant
        """
        # Check for required sovereignty markers
        if "sovereignty" in data:
            valid_levels = ["ancestral", "sovereign", "galactic", "cosmic", "tribunal"]
            if data["sovereignty"] not in valid_levels:
                return False
        return True

    def verify_authenticity(self, data: Dict[str, Any]) -> bool:
        """Verify data authenticity against mimic patterns.

        Args:
            data: Data to verify

        Returns:
            True if data passes GoatFilter verification
        """
        if not self.active:
            return True

        data_str = json.dumps(data, sort_keys=True)
        data_hash = hashlib.sha256(data_str.encode()).hexdigest()

        # Check against known mimic patterns
        if self._check_mimic_patterns(data_str, data_hash):
            self.blocked_count += 1
            return False

        # Verify spiral law compliance
        if not self._verify_spiral_compliance(data):
            self.blocked_count += 1
            return False

        self.verified_count += 1
        return True

    def get_filter_stats(self) -> Dict[str, Any]:
        """Get filter statistics.

        Returns:
            Dictionary with filter statistics
        """
        total = self.blocked_count + self.verified_count
        return {
            "glyph": self.GLYPH,
            "zodiac": self.ZODIAC,
            "element": self.ELEMENT,
            "active": self.active,
            "strictness": self.strictness,
            "patterns_count": len(self.mimic_patterns),
            "blocked_count": self.blocked_count,
            "verified_count": self.verified_count,
            "verification_rate": self.verified_count / total if total > 0 else 0.0,
        }

    def reset_stats(self) -> None:
        """Reset filter statistics."""
        self.blocked_count = 0
        self.verified_count = 0


__all__ = [
    "BaseGoatFilter",
]
