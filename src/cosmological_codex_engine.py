"""Cosmological Codex Engine for EVOLVERSE.

This module incorporates cosmological references from codex points across
all systems for thematic and ontological unity.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List


@dataclass(frozen=True)
class CodexCoordinates:
    """Represents celestial, temporal, and dimensional coordinates."""

    celestial: str
    temporal: str
    dimensional: str


@dataclass
class CodexPoint:
    """Represents a single codex point in the cosmological system."""

    id: str
    name: str
    layer: str
    cosmological_reference: str
    ontological_unity: str
    symbolism: str
    coordinates: CodexCoordinates
    governance_binding: str
    description: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CodexPoint":
        """Create a CodexPoint from dictionary.

        Args:
            data: Dictionary with codex point data

        Returns:
            CodexPoint instance
        """
        coords = data.get("coordinates", {})
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            layer=data.get("layer", ""),
            cosmological_reference=data.get("cosmologicalReference", ""),
            ontological_unity=data.get("ontologicalUnity", ""),
            symbolism=data.get("symbolism", ""),
            coordinates=CodexCoordinates(
                celestial=coords.get("celestial", ""),
                temporal=coords.get("temporal", ""),
                dimensional=coords.get("dimensional", ""),
            ),
            governance_binding=data.get("governanceBinding", ""),
            description=data.get("description", ""),
        )


@dataclass
class LayerDefinition:
    """Represents a codex layer definition."""

    name: str
    description: str
    color: str
    priority: int


@dataclass
class CosmologicalCodex:
    """Represents the complete cosmological codex."""

    codex_name: str
    version: str
    double_aries_symbol: str
    codex_points: List[CodexPoint]
    layer_definitions: Dict[str, LayerDefinition]
    thematic_unity: Dict[str, str]

    def get_points_by_layer(self, layer: str) -> List[CodexPoint]:
        """Get all codex points for a specific layer.

        Args:
            layer: Layer name

        Returns:
            List of CodexPoints in the layer
        """
        return [p for p in self.codex_points if p.layer == layer]

    def get_point_by_governance(self, governance_binding: str) -> CodexPoint | None:
        """Get codex point by governance binding.

        Args:
            governance_binding: The governance binding to search for

        Returns:
            CodexPoint if found, None otherwise
        """
        for point in self.codex_points:
            if point.governance_binding == governance_binding:
                return point
        return None

    def get_point_by_id(self, codex_id: str) -> CodexPoint | None:
        """Get codex point by ID.

        Args:
            codex_id: The codex point ID

        Returns:
            CodexPoint if found, None otherwise
        """
        for point in self.codex_points:
            if point.id == codex_id:
                return point
        return None


class CosmologicalCodexEngine:
    """Engine for managing and querying the cosmological codex."""

    DEFAULT_CODEX_PATH = Path("data/cosmological_codex.json")

    def __init__(self, codex_path: Path | None = None):
        """Initialize the codex engine.

        Args:
            codex_path: Path to the codex JSON file
        """
        self.codex_path = codex_path or self.DEFAULT_CODEX_PATH
        self.codex: CosmologicalCodex | None = None
        self._load_codex()

    def _load_codex(self) -> None:
        """Load the codex from the JSON file."""
        if not self.codex_path.exists():
            return

        with self.codex_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        # Parse codex points
        codex_points = [
            CodexPoint.from_dict(p) for p in data.get("codexPoints", [])
        ]

        # Parse layer definitions
        layer_defs = {}
        for layer_id, layer_data in data.get("layerDefinitions", {}).items():
            layer_defs[layer_id] = LayerDefinition(
                name=layer_data.get("name", ""),
                description=layer_data.get("description", ""),
                color=layer_data.get("color", ""),
                priority=layer_data.get("priority", 0),
            )

        # Create codex
        double_aries = data.get("doubleAries", {})
        self.codex = CosmologicalCodex(
            codex_name=data.get("codex_name", ""),
            version=data.get("version", ""),
            double_aries_symbol=double_aries.get("symbol", "♈️🐏🐏"),
            codex_points=codex_points,
            layer_definitions=layer_defs,
            thematic_unity=data.get("thematicUnity", {}),
        )

    def get_codex(self) -> CosmologicalCodex | None:
        """Get the loaded codex.

        Returns:
            The CosmologicalCodex if loaded, None otherwise
        """
        return self.codex

    def resolve_governance_action(
        self, action: str
    ) -> Dict[str, Any] | None:
        """Resolve a governance action to its codex binding.

        Args:
            action: The governance action name

        Returns:
            Dictionary with codex information or None
        """
        if self.codex is None:
            return None

        point = self.codex.get_point_by_governance(action)
        if point is None:
            return None

        return {
            "codex_id": point.id,
            "codex_name": point.name,
            "layer": point.layer,
            "cosmological_reference": point.cosmological_reference,
            "symbolism": point.symbolism,
            "coordinates": {
                "celestial": point.coordinates.celestial,
                "temporal": point.coordinates.temporal,
                "dimensional": point.coordinates.dimensional,
            },
            "ontological_unity": point.ontological_unity,
        }

    def get_mythic_timestamp(self, codex_id: str) -> str | None:
        """Get the mythic timestamp for a codex point.

        Args:
            codex_id: The codex point ID

        Returns:
            Temporal coordinate (mythic timestamp) or None
        """
        if self.codex is None:
            return None

        point = self.codex.get_point_by_id(codex_id)
        if point is None:
            return None

        return point.coordinates.temporal

    def get_layer_info(self, layer: str) -> LayerDefinition | None:
        """Get layer definition information.

        Args:
            layer: Layer name

        Returns:
            LayerDefinition or None
        """
        if self.codex is None:
            return None

        return self.codex.layer_definitions.get(layer)

    def embed_cosmological_reference(
        self, data: Dict[str, Any], governance_action: str
    ) -> Dict[str, Any]:
        """Embed cosmological reference into data.

        Args:
            data: The data to embed reference into
            governance_action: The governance action for reference lookup

        Returns:
            Data with embedded cosmological reference
        """
        resolution = self.resolve_governance_action(governance_action)

        if resolution is None:
            data["cosmological_binding"] = None
            return data

        data["cosmological_binding"] = {
            "codex_id": resolution["codex_id"],
            "cosmological_reference": resolution["cosmological_reference"],
            "symbolism": resolution["symbolism"],
            "celestial_coordinate": resolution["coordinates"]["celestial"],
            "mythic_timestamp": resolution["coordinates"]["temporal"],
            "dimensional_layer": resolution["coordinates"]["dimensional"],
            "ontological_unity": resolution["ontological_unity"],
        }

        return data

    def validate_thematic_unity(
        self, system_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Validate thematic unity across system data.

        Args:
            system_data: System data to validate

        Returns:
            Validation result with unity status
        """
        if self.codex is None:
            return {
                "valid": False,
                "message": "Codex not loaded",
                "bindings": [],
            }

        bindings = []
        valid = True

        # Check for governance actions in data
        if "governance_action" in system_data:
            action = system_data["governance_action"]
            resolution = self.resolve_governance_action(action)
            if resolution:
                bindings.append(
                    {
                        "action": action,
                        "codex_binding": resolution["codex_id"],
                        "unified": True,
                    }
                )
            else:
                bindings.append(
                    {
                        "action": action,
                        "codex_binding": None,
                        "unified": False,
                    }
                )
                valid = False

        return {
            "valid": valid,
            "thematic_principle": self.codex.thematic_unity.get("principle", ""),
            "bindings": bindings,
            "double_aries_seal": self.codex.double_aries_symbol,
        }

    def get_all_codex_points(self) -> List[Dict[str, Any]]:
        """Get all codex points as dictionaries.

        Returns:
            List of codex point dictionaries
        """
        if self.codex is None:
            return []

        return [
            {
                "id": p.id,
                "name": p.name,
                "layer": p.layer,
                "cosmological_reference": p.cosmological_reference,
                "symbolism": p.symbolism,
                "governance_binding": p.governance_binding,
                "coordinates": {
                    "celestial": p.coordinates.celestial,
                    "temporal": p.coordinates.temporal,
                    "dimensional": p.coordinates.dimensional,
                },
            }
            for p in self.codex.codex_points
        ]


# Global engine instance
_engine: CosmologicalCodexEngine | None = None


def get_codex_engine(codex_path: Path | None = None) -> CosmologicalCodexEngine:
    """Get or create the global codex engine.

    Args:
        codex_path: Optional path to codex JSON file

    Returns:
        The global CosmologicalCodexEngine instance
    """
    global _engine
    if _engine is None:
        _engine = CosmologicalCodexEngine(codex_path)
    return _engine


__all__ = [
    "CodexCoordinates",
    "CodexPoint",
    "LayerDefinition",
    "CosmologicalCodex",
    "CosmologicalCodexEngine",
    "get_codex_engine",
]
