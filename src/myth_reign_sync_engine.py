"""Myth-to-Reign Sync Engine for EVOLVERSE.

This module provides synchronized global broadcast capabilities, storyline
staging, and glyph-enhanced reinforcement for the EV0LVerse roadmap.
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Protocol

if TYPE_CHECKING:
    from .timeline_truth_engine import TimelineTruthEngine, TimelineTruthMap

logger = logging.getLogger(__name__)


class TimelineEngineProtocol(Protocol):
    """Protocol defining the interface for timeline engine compatibility."""

    def get_truth_map(self) -> Any:
        """Get the loaded truth map."""
        ...


class BroadcastType(Enum):
    """Types of broadcast signals."""

    REALM_WIDE = "realm_wide"
    SECTOR_SPECIFIC = "sector_specific"
    CEREMONIAL = "ceremonial"
    MASS_ACTIVATION = "mass_activation"


class ContentType(Enum):
    """Types of storyline content."""

    MYTH_TRAILER = "myth_trailer"
    AUDIO_BOOK = "audio_book"
    TRUTH_GLYPH_MAP = "truth_glyph_map"
    DISCOVERY_CHRONICLE = "discovery_chronicle"
    METRO_MASTER_PLAN = "metro_master_plan"


@dataclass
class StorylineContent:
    """Represents a storyline content item."""

    content_id: str
    title: str
    content_type: ContentType
    description: str
    glyph_binding: str
    visual_alignment: Dict[str, Any]
    sonic_alignment: Dict[str, Any]
    activation_status: str = "pending"

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "content_id": self.content_id,
            "title": self.title,
            "content_type": self.content_type.value,
            "description": self.description,
            "glyph_binding": self.glyph_binding,
            "visual_alignment": self.visual_alignment,
            "sonic_alignment": self.sonic_alignment,
            "activation_status": self.activation_status,
        }


@dataclass
class BroadcastSignal:
    """Represents a broadcast signal for realm-wide interruption."""

    signal_id: str
    signal_type: BroadcastType
    target_event: str
    activation_time: str
    mirror_override: bool
    payload: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "signal_id": self.signal_id,
            "signal_type": self.signal_type.value,
            "target_event": self.target_event,
            "activation_time": self.activation_time,
            "mirror_override": self.mirror_override,
            "payload": self.payload,
        }


@dataclass
class MythTrailerIntegration:
    """Represents a myth trailer integration."""

    trailer_id: str
    title: str
    synthesis_partner: str
    duration_seconds: int
    glyph_sequence: List[str]
    visual_effects: Dict[str, Any]
    sonic_frequencies: List[str]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "trailer_id": self.trailer_id,
            "title": self.title,
            "synthesis_partner": self.synthesis_partner,
            "duration_seconds": self.duration_seconds,
            "glyph_sequence": self.glyph_sequence,
            "visual_effects": self.visual_effects,
            "sonic_frequencies": self.sonic_frequencies,
        }


@dataclass
class ExecutionSafeHaven:
    """Represents an execution-safe haven in the multi-path framework."""

    haven_id: str
    name: str
    security_level: int
    path_connections: List[str]
    backup_protocols: List[str]
    failover_enabled: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "haven_id": self.haven_id,
            "name": self.name,
            "security_level": self.security_level,
            "path_connections": self.path_connections,
            "backup_protocols": self.backup_protocols,
            "failover_enabled": self.failover_enabled,
        }


class MythReignSyncEngine:
    """Engine for Myth-to-Reign synchronization and global broadcast."""

    DEFAULT_CONFIG_PATH = Path("config/myth_reign_sync.json")

    def __init__(self, config_path: Path | None = None):
        """Initialize the Myth-to-Reign sync engine.

        Args:
            config_path: Path to the configuration JSON file
        """
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH
        self.storyline_content: List[StorylineContent] = []
        self.broadcast_signals: List[BroadcastSignal] = []
        self.myth_trailers: List[MythTrailerIntegration] = []
        self.safe_havens: List[ExecutionSafeHaven] = []
        self._initialized = False
        self._initialize_default_content()

    def _initialize_default_content(self) -> None:
        """Initialize default storyline content and broadcast signals."""
        # Shades of Bleu content
        self.storyline_content.append(
            StorylineContent(
                content_id="SL-SHADES-001",
                title="Shades of Bleu",
                content_type=ContentType.DISCOVERY_CHRONICLE,
                description="The definitive discovery chronicle of BLEU Nation origins",
                glyph_binding="⫷💙⫸",
                visual_alignment={
                    "primary_color": "#4169E1",
                    "secondary_color": "#191970",
                    "glyph_overlay": True,
                    "animation_style": "spiral_reveal",
                },
                sonic_alignment={
                    "base_frequency": "432Hz",
                    "harmonic_layers": ["528Hz", "639Hz"],
                    "rhythm_pattern": "ancestral_pulse",
                },
                activation_status="staged",
            )
        )

        # Discovery Chronicles
        self.storyline_content.append(
            StorylineContent(
                content_id="SL-DISCOVER-002",
                title="Discovery Chronicles: Origins",
                content_type=ContentType.DISCOVERY_CHRONICLE,
                description="Complete discovery chronicles documenting sovereign origins",
                glyph_binding="📜🔥",
                visual_alignment={
                    "primary_color": "#FFD700",
                    "secondary_color": "#FF4500",
                    "glyph_overlay": True,
                    "animation_style": "scroll_unfurl",
                },
                sonic_alignment={
                    "base_frequency": "528Hz",
                    "harmonic_layers": ["741Hz", "852Hz"],
                    "rhythm_pattern": "creation_pulse",
                },
                activation_status="staged",
            )
        )

        # Metro Master Plans
        self.storyline_content.append(
            StorylineContent(
                content_id="SL-METRO-003",
                title="Metro Master Plans",
                content_type=ContentType.METRO_MASTER_PLAN,
                description="Sovereign city infrastructure and development blueprints",
                glyph_binding="🏛️⚙️",
                visual_alignment={
                    "primary_color": "#00CED1",
                    "secondary_color": "#008B8B",
                    "glyph_overlay": True,
                    "animation_style": "blueprint_build",
                },
                sonic_alignment={
                    "base_frequency": "396Hz",
                    "harmonic_layers": ["417Hz", "528Hz"],
                    "rhythm_pattern": "construction_pulse",
                },
                activation_status="staged",
            )
        )

        # Pika x Synthesis Myth Trailer
        self.myth_trailers.append(
            MythTrailerIntegration(
                trailer_id="MT-PIKA-SYNTH-001",
                title="Pika x Synthesis",
                synthesis_partner="Pika",
                duration_seconds=120,
                glyph_sequence=["⚡", "🌀", "♾️", "⫷⟟⫸"],
                visual_effects={
                    "style": "cinematic_myth",
                    "transitions": "glyph_morph",
                    "color_grading": "sovereign_palette",
                    "particle_systems": ["energy_flow", "spiral_dust"],
                },
                sonic_frequencies=["432Hz", "528Hz", "639Hz", "741Hz"],
            )
        )

        # New Year's Eve Mass Activation Broadcast
        self.broadcast_signals.append(
            BroadcastSignal(
                signal_id="BC-NYE-MASS-001",
                signal_type=BroadcastType.MASS_ACTIVATION,
                target_event="New Year's Eve Mass Activation Beyond",
                activation_time="2025-12-31T23:59:00Z",  # Target event date
                mirror_override=True,
                payload={
                    "message": "Mass Activation Beyond - Sovereign Awakening",
                    "glyph_sequence": ["🌍", "♾️", "👑"],
                    "broadcast_channels": ["global", "cosmic", "ancestral"],
                    "realm_interruption": True,
                    "sync_with_truth_map": True,
                },
            )
        )

        # Execution Safe Havens
        self.safe_havens.append(
            ExecutionSafeHaven(
                haven_id="ESH-PRIMARY-001",
                name="Primary Execution Haven",
                security_level=5,
                path_connections=["BLEUCHAIN", "COSMOS", "POLYGON"],
                backup_protocols=["redundant_sync", "failover_cascade"],
                failover_enabled=True,
            )
        )

        self.safe_havens.append(
            ExecutionSafeHaven(
                haven_id="ESH-BACKUP-002",
                name="Backup Haven Alpha",
                security_level=4,
                path_connections=["AVALANCHE", "ARBITRUM"],
                backup_protocols=["emergency_sync", "cold_storage_restore"],
                failover_enabled=True,
            )
        )

        self._initialized = True

    def stage_content(
        self, content: StorylineContent
    ) -> Dict[str, Any]:
        """Stage storyline content for deployment.

        Args:
            content: The storyline content to stage

        Returns:
            Staging result with confirmation
        """
        self.storyline_content.append(content)
        return {
            "success": True,
            "content_id": content.content_id,
            "title": content.title,
            "staged_at": datetime.utcnow().isoformat(),
            "activation_status": "staged",
        }

    def register_myth_trailer(
        self, trailer: MythTrailerIntegration
    ) -> Dict[str, Any]:
        """Register a myth trailer integration.

        Args:
            trailer: The myth trailer to register

        Returns:
            Registration result with confirmation
        """
        self.myth_trailers.append(trailer)
        return {
            "success": True,
            "trailer_id": trailer.trailer_id,
            "title": trailer.title,
            "synthesis_partner": trailer.synthesis_partner,
            "registered_at": datetime.utcnow().isoformat(),
        }

    def schedule_broadcast(
        self, signal: BroadcastSignal
    ) -> Dict[str, Any]:
        """Schedule a broadcast signal.

        Args:
            signal: The broadcast signal to schedule

        Returns:
            Scheduling result with confirmation
        """
        self.broadcast_signals.append(signal)
        return {
            "success": True,
            "signal_id": signal.signal_id,
            "target_event": signal.target_event,
            "activation_time": signal.activation_time,
            "mirror_override": signal.mirror_override,
            "scheduled_at": datetime.utcnow().isoformat(),
        }

    def execute_realm_interruption(
        self, signal_id: str
    ) -> Dict[str, Any]:
        """Execute a realm-wide interruption broadcast.

        Args:
            signal_id: The broadcast signal ID to execute

        Returns:
            Execution result
        """
        signal = next(
            (s for s in self.broadcast_signals if s.signal_id == signal_id),
            None
        )

        if signal is None:
            return {
                "success": False,
                "message": f"Signal not found: {signal_id}",
            }

        return {
            "success": True,
            "signal_id": signal.signal_id,
            "signal_type": signal.signal_type.value,
            "target_event": signal.target_event,
            "mirror_override_active": signal.mirror_override,
            "execution_timestamp": datetime.utcnow().isoformat(),
            "payload_delivered": signal.payload,
            "realm_status": "interrupted",
        }

    def get_glyph_reinforcement(
        self, content_id: str
    ) -> Dict[str, Any] | None:
        """Get glyph-enhanced reinforcement for content.

        Args:
            content_id: The content ID to get reinforcement for

        Returns:
            Glyph reinforcement data or None
        """
        content = next(
            (c for c in self.storyline_content if c.content_id == content_id),
            None
        )

        if content is None:
            return None

        return {
            "content_id": content.content_id,
            "glyph_binding": content.glyph_binding,
            "visual_alignment": content.visual_alignment,
            "sonic_alignment": content.sonic_alignment,
            "reinforcement_active": True,
        }

    def activate_safe_haven(
        self, haven_id: str
    ) -> Dict[str, Any]:
        """Activate an execution-safe haven.

        Args:
            haven_id: The haven ID to activate

        Returns:
            Activation result
        """
        haven = next(
            (h for h in self.safe_havens if h.haven_id == haven_id),
            None
        )

        if haven is None:
            return {
                "success": False,
                "message": f"Haven not found: {haven_id}",
            }

        return {
            "success": True,
            "haven_id": haven.haven_id,
            "name": haven.name,
            "security_level": haven.security_level,
            "path_connections": haven.path_connections,
            "backup_protocols_ready": haven.backup_protocols,
            "failover_status": "ready" if haven.failover_enabled else "disabled",
            "activated_at": datetime.utcnow().isoformat(),
        }

    def get_multi_path_framework(self) -> Dict[str, Any]:
        """Get the complete multi-path framework configuration.

        Returns:
            Multi-path framework configuration
        """
        return {
            "framework_version": "1.0.0",
            "safe_havens": [h.to_dict() for h in self.safe_havens],
            "total_paths": sum(
                len(h.path_connections) for h in self.safe_havens
            ),
            "failover_coverage": sum(
                1 for h in self.safe_havens if h.failover_enabled
            ) / len(self.safe_havens) * 100 if self.safe_havens else 0,
            "status": "operational",
        }

    def get_deployment_manifest(self) -> Dict[str, Any]:
        """Get the complete deployment manifest.

        Returns:
            Deployment manifest with all components
        """
        return {
            "manifest_version": "1.0.0",
            "generated_at": datetime.utcnow().isoformat(),
            "storyline_content": [c.to_dict() for c in self.storyline_content],
            "myth_trailers": [t.to_dict() for t in self.myth_trailers],
            "broadcast_signals": [s.to_dict() for s in self.broadcast_signals],
            "safe_havens": [h.to_dict() for h in self.safe_havens],
            "deployment_status": {
                "content_staged": len(self.storyline_content),
                "trailers_registered": len(self.myth_trailers),
                "broadcasts_scheduled": len(self.broadcast_signals),
                "havens_configured": len(self.safe_havens),
            },
        }

    def sync_with_timeline_truth(
        self, timeline_engine: TimelineEngineProtocol | None
    ) -> Dict[str, Any]:
        """Synchronize with the Timeline Truth Engine.

        Args:
            timeline_engine: The TimelineTruthEngine instance

        Returns:
            Synchronization result
        """
        if timeline_engine is None:
            return {
                "success": False,
                "message": "Timeline engine not provided",
            }

        truth_map = timeline_engine.get_truth_map()
        if truth_map is None:
            return {
                "success": False,
                "message": "Truth map not loaded in timeline engine",
            }

        return {
            "success": True,
            "myth_content_synced": len(self.storyline_content),
            "truth_nodes_linked": len(truth_map.truth_nodes),
            "ancestral_symbol": truth_map.ancestral_symbol,
            "activation_glyph": truth_map.activation_glyph,
            "sync_timestamp": datetime.utcnow().isoformat(),
        }


# Global engine instance
_engine: MythReignSyncEngine | None = None


def get_myth_reign_engine(
    config_path: Path | None = None
) -> MythReignSyncEngine:
    """Get or create the global Myth-to-Reign sync engine.

    Args:
        config_path: Optional path to configuration JSON file

    Returns:
        The global MythReignSyncEngine instance
    """
    global _engine
    if _engine is None:
        _engine = MythReignSyncEngine(config_path)
    return _engine


__all__ = [
    "BroadcastType",
    "ContentType",
    "StorylineContent",
    "BroadcastSignal",
    "MythTrailerIntegration",
    "ExecutionSafeHaven",
    "MythReignSyncEngine",
    "get_myth_reign_engine",
]
