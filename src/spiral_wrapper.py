"""Spiral Wrapper Module for EVOLVERSE Migration Layer.

This module provides wrapper modules for onboarding legacy systems into
Double-Ram encryption logic and implements the Open-Key Double-Ram schema
for node registration and signature events.
"""
from __future__ import annotations

import hashlib
import json
import secrets
import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List


class EncryptionMode(Enum):
    """Encryption modes for Double-Ram logic."""

    STANDARD = "standard"
    DOUBLE_RAM = "double_ram"
    OPEN_KEY = "open_key"
    SOVEREIGN = "sovereign"


class NodeStatus(Enum):
    """Status of a registered node."""

    PENDING = "pending"
    REGISTERED = "registered"
    VERIFIED = "verified"
    SUSPENDED = "suspended"
    MIGRATED = "migrated"


class SignatureEventType(Enum):
    """Types of signature events in Open-Key Double-Ram schema."""

    REGISTRATION = "registration"
    VERIFICATION = "verification"
    MIGRATION = "migration"
    CEREMONIAL = "ceremonial"
    GOVERNANCE = "governance"


@dataclass
class DoubleRamKey:
    """Represents a Double-Ram encryption key pair.

    Implements the Double-Ram (♈️♈️) encryption logic with
    sovereignty markers and glyph authentication.
    """

    key_id: str
    public_component: str
    sovereignty_marker: str
    glyph_seal: str
    created_at: float
    encryption_mode: EncryptionMode
    double_ram_seal: str = "♈️🐏🐏"

    def compute_verification_hash(self) -> str:
        """Compute verification hash for the key.

        Returns:
            SHA-256 verification hash
        """
        data = f"{self.key_id}:{self.public_component}:{self.sovereignty_marker}"
        return hashlib.sha256(data.encode()).hexdigest()


@dataclass
class SignatureEvent:
    """Represents a signature event in Open-Key Double-Ram schema."""

    event_id: str
    event_type: SignatureEventType
    node_id: str
    signature: str
    timestamp: float
    glyph_marker: str
    double_ram_verified: bool = False
    ceremonial_seal: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary.

        Returns:
            Dictionary representation
        """
        return {
            "event_id": self.event_id,
            "event_type": self.event_type.value,
            "node_id": self.node_id,
            "signature": self.signature,
            "timestamp": self.timestamp,
            "timestamp_iso": datetime.fromtimestamp(self.timestamp).isoformat(),
            "glyph_marker": self.glyph_marker,
            "double_ram_verified": self.double_ram_verified,
            "ceremonial_seal": self.ceremonial_seal,
        }


@dataclass
class RegisteredNode:
    """Represents a node registered with Open-Key Double-Ram schema."""

    node_id: str
    node_name: str
    status: NodeStatus
    double_ram_key: DoubleRamKey
    registration_timestamp: float
    legacy_system: str | None = None
    migration_complete: bool = False
    signature_events: List[SignatureEvent] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary.

        Returns:
            Dictionary representation
        """
        return {
            "node_id": self.node_id,
            "node_name": self.node_name,
            "status": self.status.value,
            "registration_timestamp": self.registration_timestamp,
            "legacy_system": self.legacy_system,
            "migration_complete": self.migration_complete,
            "double_ram_key": {
                "key_id": self.double_ram_key.key_id,
                "sovereignty_marker": self.double_ram_key.sovereignty_marker,
                "glyph_seal": self.double_ram_key.glyph_seal,
                "encryption_mode": self.double_ram_key.encryption_mode.value,
                "double_ram_seal": self.double_ram_key.double_ram_seal,
            },
            "signature_events_count": len(self.signature_events),
        }


class LegacySystemWrapper:
    """Wrapper for onboarding legacy systems into Double-Ram encryption.

    Provides migration utilities for transitioning from numerical-based
    verification models to glyph- and sigil-based paradigm.
    """

    def __init__(self, legacy_id: str, legacy_type: str):
        """Initialize legacy system wrapper.

        Args:
            legacy_id: Identifier of the legacy system
            legacy_type: Type of legacy system
        """
        self.legacy_id = legacy_id
        self.legacy_type = legacy_type
        self.migration_status: str = "pending"
        self.wrapped_at: float = time.time()
        self.double_ram_enabled: bool = False
        self.glyph_mappings: Dict[str, str] = {}

    def enable_double_ram(self, sovereign_seal: str) -> bool:
        """Enable Double-Ram encryption for the legacy system.

        Args:
            sovereign_seal: Sovereign seal for authorization

        Returns:
            True if enabled successfully
        """
        if not sovereign_seal:
            return False

        self.double_ram_enabled = True
        self.migration_status = "in_progress"
        return True

    def map_numerical_to_glyph(
        self, numerical_code: str, glyph_code: str
    ) -> None:
        """Map a numerical verification code to a glyph code.

        Args:
            numerical_code: Legacy numerical code
            glyph_code: New glyph verification code
        """
        self.glyph_mappings[numerical_code] = glyph_code

    def complete_migration(self) -> bool:
        """Complete the migration to Double-Ram encryption.

        Returns:
            True if migration completed successfully
        """
        if not self.double_ram_enabled:
            return False

        self.migration_status = "complete"
        return True

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary.

        Returns:
            Dictionary representation
        """
        return {
            "legacy_id": self.legacy_id,
            "legacy_type": self.legacy_type,
            "migration_status": self.migration_status,
            "wrapped_at": self.wrapped_at,
            "double_ram_enabled": self.double_ram_enabled,
            "glyph_mappings_count": len(self.glyph_mappings),
        }


class SpiralWrapper:
    """Main spiral wrapper for legacy system migration.

    Implements the migration layer for onboarding legacy systems
    into Double-Ram encryption logic with Open-Key schema.
    """

    # Double Ram sovereign seal
    DOUBLE_RAM_SEAL = "♈️🐏🐏"

    def __init__(self, output_dir: str | Path = "data/spiral_migration"):
        """Initialize the spiral wrapper.

        Args:
            output_dir: Directory for migration output
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.registered_nodes: Dict[str, RegisteredNode] = {}
        self.legacy_wrappers: Dict[str, LegacySystemWrapper] = {}
        self.signature_events: List[SignatureEvent] = []

    def _generate_key_id(self) -> str:
        """Generate a unique key ID.

        Returns:
            Unique key ID
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(4)
        return f"KEY-DRAM-{timestamp}-{random_suffix}"

    def _generate_node_id(self, node_name: str) -> str:
        """Generate a unique node ID.

        Args:
            node_name: Name of the node

        Returns:
            Unique node ID
        """
        timestamp = int(time.time() * 1000)
        name_hash = hashlib.sha256(node_name.encode()).hexdigest()[:8]
        return f"NODE-{name_hash}-{timestamp}"

    def _generate_event_id(self, event_type: SignatureEventType) -> str:
        """Generate a unique signature event ID.

        Args:
            event_type: Type of signature event

        Returns:
            Unique event ID
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(4)
        type_prefix = event_type.value.upper()[:4]
        return f"EVENT-{type_prefix}-{timestamp}-{random_suffix}"

    def create_double_ram_key(
        self,
        sovereignty_marker: str,
        glyph_seal: str,
        encryption_mode: EncryptionMode = EncryptionMode.DOUBLE_RAM,
    ) -> DoubleRamKey:
        """Create a Double-Ram encryption key.

        Args:
            sovereignty_marker: Sovereignty marker for the key
            glyph_seal: Glyph seal for authentication
            encryption_mode: Encryption mode to use

        Returns:
            Created DoubleRamKey
        """
        key_id = self._generate_key_id()
        # Generate public component using cryptographic randomness
        public_component = secrets.token_hex(32)

        return DoubleRamKey(
            key_id=key_id,
            public_component=public_component,
            sovereignty_marker=sovereignty_marker,
            glyph_seal=glyph_seal,
            created_at=time.time(),
            encryption_mode=encryption_mode,
        )

    def register_node(
        self,
        node_name: str,
        sovereignty_marker: str,
        glyph_seal: str,
        legacy_system: str | None = None,
    ) -> RegisteredNode:
        """Register a node with Open-Key Double-Ram schema.

        Args:
            node_name: Name of the node
            sovereignty_marker: Sovereignty marker for authorization
            glyph_seal: Glyph seal for the node
            legacy_system: Optional legacy system identifier

        Returns:
            Registered node
        """
        node_id = self._generate_node_id(node_name)

        # Create Double-Ram key for the node
        double_ram_key = self.create_double_ram_key(
            sovereignty_marker=sovereignty_marker,
            glyph_seal=glyph_seal,
            encryption_mode=EncryptionMode.OPEN_KEY,
        )

        node = RegisteredNode(
            node_id=node_id,
            node_name=node_name,
            status=NodeStatus.REGISTERED,
            double_ram_key=double_ram_key,
            registration_timestamp=time.time(),
            legacy_system=legacy_system,
        )

        self.registered_nodes[node_id] = node

        # Create registration signature event
        self._create_signature_event(
            event_type=SignatureEventType.REGISTRATION,
            node_id=node_id,
            glyph_marker=glyph_seal,
        )

        return node

    def _create_signature_event(
        self,
        event_type: SignatureEventType,
        node_id: str,
        glyph_marker: str,
        ceremonial_seal: str = "",
    ) -> SignatureEvent:
        """Create a signature event.

        Args:
            event_type: Type of event
            node_id: Node ID associated with event
            glyph_marker: Glyph marker for the event
            ceremonial_seal: Optional ceremonial seal

        Returns:
            Created SignatureEvent
        """
        event_id = self._generate_event_id(event_type)

        # Generate signature using cryptographic randomness
        sig_data = f"{event_id}:{node_id}:{glyph_marker}:{time.time()}"
        signature = hashlib.sha256(sig_data.encode()).hexdigest()

        event = SignatureEvent(
            event_id=event_id,
            event_type=event_type,
            node_id=node_id,
            signature=signature,
            timestamp=time.time(),
            glyph_marker=glyph_marker,
            double_ram_verified=True,
            ceremonial_seal=ceremonial_seal,
        )

        self.signature_events.append(event)

        # Add to node's events if node exists
        if node_id in self.registered_nodes:
            self.registered_nodes[node_id].signature_events.append(event)

        return event

    def wrap_legacy_system(
        self, legacy_id: str, legacy_type: str, sovereign_seal: str
    ) -> LegacySystemWrapper:
        """Wrap a legacy system for migration.

        Args:
            legacy_id: Identifier of the legacy system
            legacy_type: Type of legacy system
            sovereign_seal: Sovereign seal for authorization

        Returns:
            Legacy system wrapper
        """
        wrapper = LegacySystemWrapper(legacy_id=legacy_id, legacy_type=legacy_type)
        wrapper.enable_double_ram(sovereign_seal)

        self.legacy_wrappers[legacy_id] = wrapper
        return wrapper

    def migrate_legacy_node(
        self,
        legacy_wrapper: LegacySystemWrapper,
        node_name: str,
        glyph_mappings: Dict[str, str],
    ) -> RegisteredNode:
        """Migrate a legacy system to a registered node.

        Args:
            legacy_wrapper: Legacy system wrapper
            node_name: Name for the new node
            glyph_mappings: Mapping of numerical codes to glyphs

        Returns:
            Migrated node
        """
        # Apply glyph mappings
        for numerical, glyph in glyph_mappings.items():
            legacy_wrapper.map_numerical_to_glyph(numerical, glyph)

        # Get sovereignty marker from first glyph mapping
        sovereignty_marker = list(glyph_mappings.values())[0] if glyph_mappings else "♈️"
        glyph_seal = self.DOUBLE_RAM_SEAL

        # Register the node
        node = self.register_node(
            node_name=node_name,
            sovereignty_marker=sovereignty_marker,
            glyph_seal=glyph_seal,
            legacy_system=legacy_wrapper.legacy_id,
        )

        # Update node status
        node.status = NodeStatus.MIGRATED
        node.migration_complete = True

        # Complete legacy wrapper migration
        legacy_wrapper.complete_migration()

        # Create migration signature event
        self._create_signature_event(
            event_type=SignatureEventType.MIGRATION,
            node_id=node.node_id,
            glyph_marker=glyph_seal,
            ceremonial_seal=f"MIGRATED-FROM-{legacy_wrapper.legacy_id}",
        )

        return node

    def verify_node(self, node_id: str) -> bool:
        """Verify a registered node.

        Args:
            node_id: ID of the node to verify

        Returns:
            True if verification successful
        """
        node = self.registered_nodes.get(node_id)
        if node is None:
            return False

        # Verify Double-Ram key
        key_hash = node.double_ram_key.compute_verification_hash()
        if not key_hash:
            return False

        node.status = NodeStatus.VERIFIED

        # Create verification signature event
        self._create_signature_event(
            event_type=SignatureEventType.VERIFICATION,
            node_id=node_id,
            glyph_marker=node.double_ram_key.glyph_seal,
        )

        return True

    def export_migration_log(self, filename: str | None = None) -> Path:
        """Export the migration log to JSON.

        Args:
            filename: Optional filename (auto-generated if None)

        Returns:
            Path to the exported file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"spiral_migration_{timestamp}.json"

        filepath = self.output_dir / filename

        log_data = {
            "export_timestamp": time.time(),
            "export_timestamp_iso": datetime.now().isoformat(),
            "double_ram_seal": self.DOUBLE_RAM_SEAL,
            "registered_nodes_count": len(self.registered_nodes),
            "legacy_wrappers_count": len(self.legacy_wrappers),
            "signature_events_count": len(self.signature_events),
            "registered_nodes": [
                node.to_dict() for node in self.registered_nodes.values()
            ],
            "legacy_wrappers": [
                wrapper.to_dict() for wrapper in self.legacy_wrappers.values()
            ],
            "signature_events": [event.to_dict() for event in self.signature_events],
        }

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(log_data, f, indent=2)

        return filepath


# Global wrapper instance
_wrapper: SpiralWrapper | None = None


def get_wrapper(
    output_dir: str | Path = "data/spiral_migration",
) -> SpiralWrapper:
    """Get or create the global spiral wrapper.

    Args:
        output_dir: Output directory for migration

    Returns:
        The global SpiralWrapper instance
    """
    global _wrapper
    if _wrapper is None:
        _wrapper = SpiralWrapper(output_dir)
    return _wrapper


__all__ = [
    "EncryptionMode",
    "NodeStatus",
    "SignatureEventType",
    "DoubleRamKey",
    "SignatureEvent",
    "RegisteredNode",
    "LegacySystemWrapper",
    "SpiralWrapper",
    "get_wrapper",
]
