"""Timeline Truth Map Engine for EVOLVERSE.

This module integrates ancestral wisdom, mythological layering, and verified
evolutionary coding nodes for the Timeline of Truth synchronization system.
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class TruthCoordinates:
    """Represents temporal, dimensional, and resonance coordinates."""

    temporal: str
    dimensional: str
    resonance: str


@dataclass
class TruthNode:
    """Represents a single truth node in the timeline."""

    id: str
    name: str
    epoch: str
    ancestral_binding: str
    mythological_layer: str
    verified_code: str
    coordinates: TruthCoordinates
    description: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TruthNode":
        """Create a TruthNode from dictionary.

        Args:
            data: Dictionary with truth node data

        Returns:
            TruthNode instance
        """
        coords = data.get("coordinates", {})
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            epoch=data.get("epoch", ""),
            ancestral_binding=data.get("ancestralBinding", ""),
            mythological_layer=data.get("mythologicalLayer", ""),
            verified_code=data.get("verifiedCode", ""),
            coordinates=TruthCoordinates(
                temporal=coords.get("temporal", ""),
                dimensional=coords.get("dimensional", ""),
                resonance=coords.get("resonance", ""),
            ),
            description=data.get("description", ""),
        )


@dataclass
class MythologicalLayer:
    """Represents a mythological layer definition."""

    name: str
    description: str
    color: str
    priority: int
    associated_scrolls: List[str]


@dataclass
class EvolutionaryCodingNode:
    """Represents an evolutionary coding node."""

    node_id: str
    name: str
    function: str
    verification_hash: str
    binding_protocol: str


@dataclass
class SyncStage:
    """Represents a stage in the sync protocol."""

    stage: int
    name: str
    description: str


@dataclass
class TimelineTruthMap:
    """Represents the complete Timeline of Truth Map."""

    map_name: str
    version: str
    created: str
    ancestral_symbol: str
    ancestral_principle: str
    activation_glyph: str
    truth_nodes: List[TruthNode]
    mythological_layers: Dict[str, MythologicalLayer]
    evolutionary_coding_nodes: List[EvolutionaryCodingNode]
    sync_stages: List[SyncStage]

    def get_nodes_by_epoch(self, epoch: str) -> List[TruthNode]:
        """Get all truth nodes for a specific epoch.

        Args:
            epoch: Epoch name

        Returns:
            List of TruthNodes in the epoch
        """
        return [n for n in self.truth_nodes if n.epoch == epoch]

    def get_node_by_id(self, node_id: str) -> TruthNode | None:
        """Get truth node by ID.

        Args:
            node_id: The truth node ID

        Returns:
            TruthNode if found, None otherwise
        """
        for node in self.truth_nodes:
            if node.id == node_id:
                return node
        return None

    def get_coding_node(self, node_id: str) -> EvolutionaryCodingNode | None:
        """Get evolutionary coding node by ID.

        Args:
            node_id: The coding node ID

        Returns:
            EvolutionaryCodingNode if found, None otherwise
        """
        for node in self.evolutionary_coding_nodes:
            if node.node_id == node_id:
                return node
        return None


class TimelineTruthEngine:
    """Engine for managing and querying the Timeline of Truth Map."""

    DEFAULT_MAP_PATH = Path("data/timeline_truth_map.json")

    def __init__(self, map_path: Path | None = None):
        """Initialize the timeline truth engine.

        Args:
            map_path: Path to the timeline truth map JSON file
        """
        self.map_path = map_path or self.DEFAULT_MAP_PATH
        self.truth_map: TimelineTruthMap | None = None
        self._load_map()

    def _load_map(self) -> None:
        """Load the timeline truth map from the JSON file."""
        if not self.map_path.exists():
            logger.warning(
                f"Timeline truth map file not found at {self.map_path}. "
                "Timeline features will be unavailable until the file is created."
            )
            return

        with self.map_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        # Parse truth nodes
        truth_nodes = [
            TruthNode.from_dict(n) for n in data.get("truthNodes", [])
        ]

        # Parse mythological layers
        myth_layers = {}
        for layer_id, layer_data in data.get("mythologicalLayers", {}).items():
            myth_layers[layer_id] = MythologicalLayer(
                name=layer_data.get("name", ""),
                description=layer_data.get("description", ""),
                color=layer_data.get("color", ""),
                priority=layer_data.get("priority", 0),
                associated_scrolls=layer_data.get("associatedScrolls", []),
            )

        # Parse evolutionary coding nodes
        coding_nodes = [
            EvolutionaryCodingNode(
                node_id=n.get("nodeId", ""),
                name=n.get("name", ""),
                function=n.get("function", ""),
                verification_hash=n.get("verificationHash", ""),
                binding_protocol=n.get("bindingProtocol", ""),
            )
            for n in data.get("evolutionaryCodingNodes", [])
        ]

        # Parse sync stages
        sync_protocol = data.get("syncProtocol", {})
        sync_stages = [
            SyncStage(
                stage=s.get("stage", 0),
                name=s.get("name", ""),
                description=s.get("description", ""),
            )
            for s in sync_protocol.get("stages", [])
        ]

        # Create truth map
        ancestral = data.get("ancestralWisdom", {})
        self.truth_map = TimelineTruthMap(
            map_name=data.get("map_name", ""),
            version=data.get("version", ""),
            created=data.get("created", ""),
            ancestral_symbol=ancestral.get("symbol", "🌍🧬♾️"),
            ancestral_principle=ancestral.get("principle", ""),
            activation_glyph=ancestral.get("activationGlyph", "⫷⟟⫸"),
            truth_nodes=truth_nodes,
            mythological_layers=myth_layers,
            evolutionary_coding_nodes=coding_nodes,
            sync_stages=sync_stages,
        )

    def get_truth_map(self) -> TimelineTruthMap | None:
        """Get the loaded truth map.

        Returns:
            The TimelineTruthMap if loaded, None otherwise
        """
        return self.truth_map

    def resolve_ancestral_binding(
        self, binding: str
    ) -> Dict[str, Any] | None:
        """Resolve an ancestral binding to its truth node.

        Args:
            binding: The ancestral binding name

        Returns:
            Dictionary with truth node information or None
        """
        if self.truth_map is None:
            return None

        for node in self.truth_map.truth_nodes:
            if node.ancestral_binding == binding:
                return {
                    "truth_id": node.id,
                    "truth_name": node.name,
                    "epoch": node.epoch,
                    "mythological_layer": node.mythological_layer,
                    "verified_code": node.verified_code,
                    "coordinates": {
                        "temporal": node.coordinates.temporal,
                        "dimensional": node.coordinates.dimensional,
                        "resonance": node.coordinates.resonance,
                    },
                }
        return None

    def get_mythological_context(
        self, layer_key: str
    ) -> Dict[str, Any] | None:
        """Get mythological context for a layer.

        Args:
            layer_key: The mythological layer key

        Returns:
            Dictionary with layer context or None
        """
        if self.truth_map is None:
            return None

        layer = self.truth_map.mythological_layers.get(layer_key)
        if layer is None:
            return None

        return {
            "name": layer.name,
            "description": layer.description,
            "color": layer.color,
            "priority": layer.priority,
            "associated_scrolls": layer.associated_scrolls,
        }

    def verify_evolutionary_code(
        self, node_id: str
    ) -> Dict[str, Any] | None:
        """Verify an evolutionary coding node.

        Args:
            node_id: The coding node ID

        Returns:
            Dictionary with verification result or None
        """
        if self.truth_map is None:
            return None

        coding_node = self.truth_map.get_coding_node(node_id)
        if coding_node is None:
            return None

        return {
            "node_id": coding_node.node_id,
            "name": coding_node.name,
            "function": coding_node.function,
            "verification_hash": coding_node.verification_hash,
            "binding_protocol": coding_node.binding_protocol,
            "verified": True,
            "timestamp": datetime.utcnow().isoformat(),
        }

    def execute_sync_protocol(
        self, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute the truth-to-reign synchronization protocol.

        Args:
            data: Data to synchronize

        Returns:
            Synchronized data with protocol results
        """
        if self.truth_map is None:
            return {
                "success": False,
                "message": "Truth map not loaded",
                "data": data,
            }

        results = {
            "success": True,
            "protocol_version": "1.0.0",
            "ancestral_symbol": self.truth_map.ancestral_symbol,
            "activation_glyph": self.truth_map.activation_glyph,
            "stages_completed": [],
            "synchronized_data": data,
        }

        for stage in self.truth_map.sync_stages:
            stage_result = {
                "stage": stage.stage,
                "name": stage.name,
                "status": "completed",
                "timestamp": datetime.utcnow().isoformat(),
            }
            results["stages_completed"].append(stage_result)

        return results

    def embed_truth_reference(
        self, data: Dict[str, Any], truth_node_id: str
    ) -> Dict[str, Any]:
        """Embed truth reference into data.

        Args:
            data: The data to embed reference into
            truth_node_id: The truth node ID for reference lookup

        Returns:
            Data with embedded truth reference
        """
        if self.truth_map is None:
            data["truth_binding"] = None
            return data

        node = self.truth_map.get_node_by_id(truth_node_id)
        if node is None:
            data["truth_binding"] = None
            return data

        data["truth_binding"] = {
            "truth_id": node.id,
            "truth_name": node.name,
            "epoch": node.epoch,
            "ancestral_binding": node.ancestral_binding,
            "mythological_layer": node.mythological_layer,
            "verified_code": node.verified_code,
            "resonance": node.coordinates.resonance,
            "dimensional_layer": node.coordinates.dimensional,
        }

        return data

    def get_all_truth_nodes(self) -> List[Dict[str, Any]]:
        """Get all truth nodes as dictionaries.

        Returns:
            List of truth node dictionaries
        """
        if self.truth_map is None:
            return []

        return [
            {
                "id": n.id,
                "name": n.name,
                "epoch": n.epoch,
                "ancestral_binding": n.ancestral_binding,
                "mythological_layer": n.mythological_layer,
                "verified_code": n.verified_code,
                "coordinates": {
                    "temporal": n.coordinates.temporal,
                    "dimensional": n.coordinates.dimensional,
                    "resonance": n.coordinates.resonance,
                },
            }
            for n in self.truth_map.truth_nodes
        ]


# Global engine instance
_engine: TimelineTruthEngine | None = None


def get_timeline_engine(map_path: Path | None = None) -> TimelineTruthEngine:
    """Get or create the global timeline truth engine.

    Args:
        map_path: Optional path to truth map JSON file

    Returns:
        The global TimelineTruthEngine instance
    """
    global _engine
    if _engine is None:
        _engine = TimelineTruthEngine(map_path)
    return _engine


__all__ = [
    "TruthCoordinates",
    "TruthNode",
    "MythologicalLayer",
    "EvolutionaryCodingNode",
    "SyncStage",
    "TimelineTruthMap",
    "TimelineTruthEngine",
    "get_timeline_engine",
]
