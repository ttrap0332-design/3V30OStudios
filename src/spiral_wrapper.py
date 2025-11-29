"""Spiral Wrapper Module for EVOLVERSE Migration Layer.

This module provides Spiral Wrapper functionality for onboarding legacy systems
into Double-Ram encryption logic, implementing the Open-Key Double-Ram schema
for node registration and signature events.

Key features:
- Legacy system migration to glyph-based verification
- Double-Ram encryption wrapper
- Open-Key Double-Ram schema registration
- Signature event handling for node registration
"""
from __future__ import annotations

import hashlib
import secrets
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List
import json


class LegacySystemType(Enum):
    """Types of legacy systems for migration."""

    NUMERICAL_AUTH = "numerical_auth"
    TRADITIONAL_PKI = "traditional_pki"
    OAUTH = "oauth"
    JWT = "jwt"
    CUSTOM = "custom"


class WrapperInterfaceType(Enum):
    """Types of wrapper interfaces."""

    ADAPTER = "adapter"
    BRIDGE = "bridge"
    TRANSLATOR = "translator"


class EncryptionAlgorithm(Enum):
    """Encryption algorithms for Double-Ram encryption."""

    AES_256_GCM = "AES-256-GCM"
    CHACHA20_POLY1305 = "ChaCha20-Poly1305"
    XCHACHA20_POLY1305 = "XChaCha20-Poly1305"


class SignatureEventType(Enum):
    """Types of signature events."""

    REGISTRATION = "registration"
    AUTHENTICATION = "authentication"
    AUTHORIZATION = "authorization"
    TRANSFER = "transfer"
    CEREMONIAL = "ceremonial"


class SovereigntyLevel(Enum):
    """Sovereignty levels for node registration."""

    CIVILIAN = "civilian"
    ANCESTRAL = "ancestral"
    SOVEREIGN = "sovereign"
    GALACTIC = "galactic"
    COSMIC = "cosmic"


@dataclass
class DoubleRamKey:
    """Represents a Double-Ram encryption key pair."""

    key_id: str
    primary_key_hash: str
    secondary_key_hash: str
    primary_glyph: str = "♈️"
    secondary_glyph: str = "🐏"
    combined_seal: str = "♈️🐏🐏"
    key_length: int = 256
    sovereignty_level: SovereigntyLevel = SovereigntyLevel.ANCESTRAL
    created_at: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "key_id": self.key_id,
            "primary_key_hash": self.primary_key_hash,
            "secondary_key_hash": self.secondary_key_hash,
            "primary_glyph": self.primary_glyph,
            "secondary_glyph": self.secondary_glyph,
            "combined_seal": self.combined_seal,
            "key_length": self.key_length,
            "sovereignty_level": self.sovereignty_level.value,
            "created_at": self.created_at,
        }


@dataclass
class RegisteredNode:
    """Represents a node registered using Open-Key Double-Ram schema."""

    node_id: str
    node_name: str
    public_key_hash: str
    primary_key_glyph: str = "♈️"
    secondary_key_glyph: str = "🐏"
    glyph_authority: List[str] = field(default_factory=list)
    sovereignty_level: SovereigntyLevel = SovereigntyLevel.ANCESTRAL
    registration_timestamp: float = field(default_factory=time.time)
    hydromark_link: str = ""
    active: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "node_id": self.node_id,
            "node_name": self.node_name,
            "public_key_hash": self.public_key_hash,
            "primary_key_glyph": self.primary_key_glyph,
            "secondary_key_glyph": self.secondary_key_glyph,
            "glyph_authority": self.glyph_authority,
            "sovereignty_level": self.sovereignty_level.value,
            "registration_timestamp": self.registration_timestamp,
            "hydromark_link": self.hydromark_link,
            "active": self.active,
        }


@dataclass
class SignatureEvent:
    """Represents a signature event in the Open-Key Double-Ram schema."""

    event_id: str
    event_type: SignatureEventType
    node_id: str
    signature_hash: str
    glyph_markers: List[str]
    double_ram_verified: bool = False
    timestamp: float = field(default_factory=time.time)
    linked_hydromark: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "event_id": self.event_id,
            "event_type": self.event_type.value,
            "node_id": self.node_id,
            "signature_hash": self.signature_hash,
            "glyph_markers": self.glyph_markers,
            "double_ram_verified": self.double_ram_verified,
            "timestamp": self.timestamp,
            "linked_hydromark": self.linked_hydromark,
            "metadata": self.metadata,
        }


@dataclass
class LegacyMigrationRecord:
    """Represents a legacy system migration record."""

    record_id: str
    legacy_system_type: LegacySystemType
    wrapper_interface: WrapperInterfaceType
    source_format: str
    target_format: str
    glyph_assignment: List[str]
    migration_timestamp: float = field(default_factory=time.time)
    success: bool = True
    numerical_deprecated: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "record_id": self.record_id,
            "legacy_system_type": self.legacy_system_type.value,
            "wrapper_interface": self.wrapper_interface.value,
            "source_format": self.source_format,
            "target_format": self.target_format,
            "glyph_assignment": self.glyph_assignment,
            "migration_timestamp": self.migration_timestamp,
            "success": self.success,
            "numerical_deprecated": self.numerical_deprecated,
        }


class SpiralWrapper:
    """Spiral Wrapper for legacy system migration to Double-Ram encryption."""

    # Constants
    SCHEMA_NAME = "Open-Key Double-Ram"
    DOUBLE_RAM_SEAL = "♈️🐏🐏"
    PRIMARY_GLYPH = "♈️"
    SECONDARY_GLYPH = "🐏"
    DEFAULT_KEY_LENGTH = 256
    DEFAULT_FLIP_RATIO = 2.1

    def __init__(
        self,
        output_dir: str | Path = "data/spiral_wrapper",
        encryption_algorithm: EncryptionAlgorithm = EncryptionAlgorithm.AES_256_GCM,
    ):
        """Initialize the Spiral Wrapper.

        Args:
            output_dir: Directory for wrapper output
            encryption_algorithm: Encryption algorithm for Double-Ram
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.encryption_algorithm = encryption_algorithm
        self.node_registry: Dict[str, RegisteredNode] = {}
        self.signature_events: List[SignatureEvent] = []
        self.migration_records: List[LegacyMigrationRecord] = []
        self.double_ram_keys: Dict[str, DoubleRamKey] = {}

    def _generate_node_id(self) -> str:
        """Generate a unique node ID with cryptographic randomness.

        Returns:
            Unique node ID
        """
        return f"NODE-{secrets.token_hex(8)}"

    def _generate_event_id(self) -> str:
        """Generate a unique event ID with cryptographic randomness.

        Returns:
            Unique event ID
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(4)
        return f"EVENT-{timestamp}-{random_suffix}"

    def _generate_key_id(self) -> str:
        """Generate a unique key ID with cryptographic randomness.

        Returns:
            Unique key ID
        """
        return f"KEY-{secrets.token_hex(6)}"

    def _generate_record_id(self) -> str:
        """Generate a unique migration record ID.

        Returns:
            Unique record ID
        """
        timestamp = int(time.time() * 1000)
        return f"MIGRATE-{timestamp}-{secrets.token_hex(4)}"

    def _generate_key_hash(self, data: str, glyph: str) -> str:
        """Generate a key hash with glyph binding.

        Args:
            data: Data to hash
            glyph: Glyph marker to bind

        Returns:
            SHA-256 hash
        """
        hash_data = f"{glyph}:{data}:{secrets.token_hex(16)}"
        return hashlib.sha256(hash_data.encode()).hexdigest()

    def _generate_hydromark(self, node_id: str, key_hash: str) -> str:
        """Generate a BLEUHydroMark for node registration.

        Args:
            node_id: Node identifier
            key_hash: Key hash

        Returns:
            Hydromark hash
        """
        hydromark_data = f"BLEU:{node_id}:{key_hash}:{time.time()}"
        return hashlib.sha256(hydromark_data.encode()).hexdigest()

    def generate_double_ram_key(
        self,
        sovereignty_level: SovereigntyLevel = SovereigntyLevel.ANCESTRAL,
    ) -> DoubleRamKey:
        """Generate a Double-Ram encryption key pair.

        Args:
            sovereignty_level: Sovereignty level for the key

        Returns:
            Generated DoubleRamKey
        """
        key_id = self._generate_key_id()

        # Generate primary and secondary key hashes with glyph binding
        primary_secret = secrets.token_hex(32)
        secondary_secret = secrets.token_hex(32)

        primary_hash = self._generate_key_hash(primary_secret, self.PRIMARY_GLYPH)
        secondary_hash = self._generate_key_hash(secondary_secret, self.SECONDARY_GLYPH)

        key = DoubleRamKey(
            key_id=key_id,
            primary_key_hash=primary_hash,
            secondary_key_hash=secondary_hash,
            primary_glyph=self.PRIMARY_GLYPH,
            secondary_glyph=self.SECONDARY_GLYPH,
            combined_seal=self.DOUBLE_RAM_SEAL,
            key_length=self.DEFAULT_KEY_LENGTH,
            sovereignty_level=sovereignty_level,
        )

        self.double_ram_keys[key_id] = key
        return key

    def register_node(
        self,
        node_name: str,
        sovereignty_level: SovereigntyLevel = SovereigntyLevel.ANCESTRAL,
        glyph_authority: List[str] | None = None,
    ) -> RegisteredNode:
        """Register a node using Open-Key Double-Ram schema.

        Args:
            node_name: Human-readable node name
            sovereignty_level: Sovereignty level for the node
            glyph_authority: Glyph authority chain (defaults to Double Ram)

        Returns:
            Registered node
        """
        if glyph_authority is None:
            glyph_authority = [self.PRIMARY_GLYPH, self.SECONDARY_GLYPH, self.SECONDARY_GLYPH]

        node_id = self._generate_node_id()

        # Generate public key hash
        public_key_data = f"{node_name}:{node_id}:{secrets.token_hex(32)}"
        public_key_hash = hashlib.sha256(public_key_data.encode()).hexdigest()

        # Generate hydromark link
        hydromark_link = self._generate_hydromark(node_id, public_key_hash)

        node = RegisteredNode(
            node_id=node_id,
            node_name=node_name,
            public_key_hash=public_key_hash,
            primary_key_glyph=self.PRIMARY_GLYPH,
            secondary_key_glyph=self.SECONDARY_GLYPH,
            glyph_authority=glyph_authority,
            sovereignty_level=sovereignty_level,
            hydromark_link=hydromark_link,
            active=True,
        )

        self.node_registry[node_id] = node

        # Record registration signature event
        self._record_signature_event(
            node_id=node_id,
            event_type=SignatureEventType.REGISTRATION,
            glyph_markers=glyph_authority,
            hydromark=hydromark_link,
        )

        return node

    def _record_signature_event(
        self,
        node_id: str,
        event_type: SignatureEventType,
        glyph_markers: List[str],
        hydromark: str = "",
        metadata: Dict[str, Any] | None = None,
    ) -> SignatureEvent:
        """Record a signature event.

        Args:
            node_id: Node identifier
            event_type: Type of event
            glyph_markers: Glyph markers for the event
            hydromark: Optional hydromark link
            metadata: Optional event metadata

        Returns:
            Recorded SignatureEvent
        """
        event_id = self._generate_event_id()

        # Generate signature hash with Double-Ram binding
        sig_data = f"{event_id}:{node_id}:{event_type.value}:{time.time()}"
        signature_hash = hashlib.sha256(sig_data.encode()).hexdigest()

        # Verify Double-Ram binding
        double_ram_verified = (
            self.PRIMARY_GLYPH in glyph_markers and
            self.SECONDARY_GLYPH in glyph_markers
        )

        event = SignatureEvent(
            event_id=event_id,
            event_type=event_type,
            node_id=node_id,
            signature_hash=signature_hash,
            glyph_markers=glyph_markers,
            double_ram_verified=double_ram_verified,
            linked_hydromark=hydromark,
            metadata=metadata or {},
        )

        self.signature_events.append(event)
        return event

    def migrate_legacy_system(
        self,
        legacy_type: LegacySystemType,
        source_format: str,
        wrapper_interface: WrapperInterfaceType = WrapperInterfaceType.ADAPTER,
    ) -> LegacyMigrationRecord:
        """Migrate a legacy system to glyph-based verification.

        Args:
            legacy_type: Type of legacy system
            source_format: Source data format
            wrapper_interface: Type of wrapper interface

        Returns:
            Migration record
        """
        record_id = self._generate_record_id()

        # Determine target format based on legacy type
        target_format = self._get_target_format(legacy_type)

        # Assign glyphs based on legacy type
        glyph_assignment = self._get_glyph_assignment(legacy_type)

        record = LegacyMigrationRecord(
            record_id=record_id,
            legacy_system_type=legacy_type,
            wrapper_interface=wrapper_interface,
            source_format=source_format,
            target_format=target_format,
            glyph_assignment=glyph_assignment,
            success=True,
            numerical_deprecated=True,
        )

        self.migration_records.append(record)
        return record

    def _get_target_format(self, legacy_type: LegacySystemType) -> str:
        """Get target format for legacy system migration.

        Args:
            legacy_type: Type of legacy system

        Returns:
            Target format string
        """
        target_formats = {
            LegacySystemType.NUMERICAL_AUTH: "glyph-signature",
            LegacySystemType.TRADITIONAL_PKI: "double-ram-pki",
            LegacySystemType.OAUTH: "glyph-oauth",
            LegacySystemType.JWT: "glyph-token",
            LegacySystemType.CUSTOM: "spiral-wrapper",
        }
        return target_formats.get(legacy_type, "spiral-wrapper")

    def _get_glyph_assignment(self, legacy_type: LegacySystemType) -> List[str]:
        """Get glyph assignment for legacy system migration.

        Args:
            legacy_type: Type of legacy system

        Returns:
            List of assigned glyphs
        """
        base_glyphs = [self.PRIMARY_GLYPH, self.SECONDARY_GLYPH]

        glyph_additions = {
            LegacySystemType.NUMERICAL_AUTH: ["🌀"],
            LegacySystemType.TRADITIONAL_PKI: ["📜"],
            LegacySystemType.OAUTH: ["👑"],
            LegacySystemType.JWT: ["🔥"],
            LegacySystemType.CUSTOM: ["🦁"],
        }

        return base_glyphs + glyph_additions.get(legacy_type, [])

    def get_node(self, node_id: str) -> RegisteredNode | None:
        """Get a registered node by ID.

        Args:
            node_id: Node identifier

        Returns:
            RegisteredNode or None if not found
        """
        return self.node_registry.get(node_id)

    def list_nodes(self) -> List[RegisteredNode]:
        """List all registered nodes.

        Returns:
            List of registered nodes
        """
        return list(self.node_registry.values())

    def get_signature_events(
        self, node_id: str | None = None
    ) -> List[SignatureEvent]:
        """Get signature events, optionally filtered by node.

        Args:
            node_id: Optional node ID to filter by

        Returns:
            List of signature events
        """
        if node_id is None:
            return self.signature_events
        return [e for e in self.signature_events if e.node_id == node_id]

    def verify_double_ram(self, node_id: str) -> bool:
        """Verify Double-Ram binding for a node.

        Args:
            node_id: Node identifier

        Returns:
            True if Double-Ram verification passes
        """
        node = self.node_registry.get(node_id)
        if node is None:
            return False

        # Check if node has proper glyph authority
        return (
            self.PRIMARY_GLYPH in node.glyph_authority and
            self.SECONDARY_GLYPH in node.glyph_authority
        )

    def export_registry(self, filename: str | None = None) -> Path:
        """Export the node registry to JSON.

        Args:
            filename: Optional filename (auto-generated if None)

        Returns:
            Path to the exported file
        """
        if filename is None:
            timestamp = int(time.time())
            filename = f"node_registry_{timestamp}.json"

        filepath = self.output_dir / filename

        registry_data = {
            "schema_name": self.SCHEMA_NAME,
            "double_ram_seal": self.DOUBLE_RAM_SEAL,
            "encryption_algorithm": self.encryption_algorithm.value,
            "flip_ratio": self.DEFAULT_FLIP_RATIO,
            "export_timestamp": time.time(),
            "total_nodes": len(self.node_registry),
            "nodes": [node.to_dict() for node in self.node_registry.values()],
            "signature_events": [event.to_dict() for event in self.signature_events],
            "migration_records": [record.to_dict() for record in self.migration_records],
            "double_ram_keys": [key.to_dict() for key in self.double_ram_keys.values()],
        }

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(registry_data, f, indent=2)

        return filepath


# Global wrapper instance
_wrapper: SpiralWrapper | None = None


def get_wrapper(output_dir: str | Path = "data/spiral_wrapper") -> SpiralWrapper:
    """Get or create the global spiral wrapper.

    Args:
        output_dir: Output directory for wrapper

    Returns:
        The global SpiralWrapper instance
    """
    global _wrapper
    if _wrapper is None:
        _wrapper = SpiralWrapper(output_dir)
    return _wrapper


__all__ = [
    "LegacySystemType",
    "WrapperInterfaceType",
    "EncryptionAlgorithm",
    "SignatureEventType",
    "SovereigntyLevel",
    "DoubleRamKey",
    "RegisteredNode",
    "SignatureEvent",
    "LegacyMigrationRecord",
    "SpiralWrapper",
    "get_wrapper",
]
