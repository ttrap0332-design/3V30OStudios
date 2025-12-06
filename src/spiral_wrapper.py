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
    """Represents a signature event in Open-Key Double-Ram schema."""
    """Represents a signature event in the Open-Key Double-Ram schema."""

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
            "signature": self.signature,
            "timestamp": self.timestamp,
            "timestamp_iso": datetime.fromtimestamp(self.timestamp).isoformat(),
            "glyph_marker": self.glyph_marker,
            "double_ram_verified": self.double_ram_verified,
            "ceremonial_seal": self.ceremonial_seal,
            "signature_hash": self.signature_hash,
            "glyph_markers": self.glyph_markers,
            "double_ram_verified": self.double_ram_verified,
            "timestamp": self.timestamp,
            "linked_hydromark": self.linked_hydromark,
            "metadata": self.metadata,
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
        node_id = self._generate_node_id(node_name)

        # Create Double-Ram key for the node
        double_ram_key = self.create_double_ram_key(
            sovereignty_marker=sovereignty_marker,
            glyph_seal=glyph_seal,
            encryption_mode=EncryptionMode.OPEN_KEY,
        )
        if glyph_authority is None:
            glyph_authority = [self.PRIMARY_GLYPH, self.SECONDARY_GLYPH, self.SECONDARY_GLYPH]

        node_id = self._generate_node_id()

        # Generate public key hash using only node_name and random data
        # to avoid correlations with node_id
        public_key_data = f"{node_name}:{secrets.token_hex(32)}:{time.time()}"
        public_key_hash = hashlib.sha256(public_key_data.encode()).hexdigest()

        # Generate hydromark link
        hydromark_link = self._generate_hydromark(node_id, public_key_hash)

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

        # Get sovereignty marker from first glyph mapping, or use default
        if glyph_mappings:
            sovereignty_marker = next(iter(glyph_mappings.values()))
        else:
            sovereignty_marker = "♈️"
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

        # Verify Double-Ram key has required components
        key = node.double_ram_key
        if not key.public_component or not key.sovereignty_marker or not key.glyph_seal:
            return False

        # Compute and store verification hash
        key.compute_verification_hash()

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


def get_wrapper(
    output_dir: str | Path = "data/spiral_migration",
) -> SpiralWrapper:
    """Get or create the global spiral wrapper.

    Args:
        output_dir: Output directory for migration
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
    "EncryptionMode",
    "NodeStatus",
    "SignatureEventType",
    "DoubleRamKey",
    "SignatureEvent",
    "RegisteredNode",
    "LegacySystemWrapper",
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
Transaction Hash,Status,Method,Blockno,DateTime (UTC),From,From_Nametag,To,To_Nametag,Amount,Value (USD),Txn Fee
"0xc40f0b624dbe8e4d637d8b153998ca2bacefc04985bbe69cbc6511c540d0ed91","Success","Claim","36619717","2025-10-09 16:53:01","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000202"
"0x5bdc30ed7698f5ab4cb369dbfc9df0e5bdbd28d906d68269c53bd2de8aeb5148","Success","Claim","36619714","2025-10-09 16:52:55","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000203"
"0xf9ef0b3f7b41b7b5c39534aeadc1bf71ffb17c0a47706a1f85688cf54a48bdb7","Success","Claim","36619710","2025-10-09 16:52:47","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000207"
"0x068aa2f49109b9e115e03ee5acc57c5d2cb97bca19d3463064b779858106f8f4","Success","Claim","36619678","2025-10-09 16:51:43","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.0000022"
"0xa88e67fbb30e1a2d05dffbb9b8f41684d0527d660ff2807a3a189643e4e3f232","Success","Claim","36619669","2025-10-09 16:51:25","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000219"
"0xf579296b8c783c354bcbd077f8794157d0426f00f362b2a6b688d96c4a88e525","Success","Claim","36619622","2025-10-09 16:49:51","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000239"
"0x4f8fd334a54433562bdd3a8792908addd45b826a3ee8c82662887084bb55e69f","Success","Claim","36619605","2025-10-09 16:49:17","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000237"
"0x56b89c86f9f34d964499d92a8f004f37b0392681a31fdecef3a249770404ea6d","Success","Claim","36619581","2025-10-09 16:48:29","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000249"
"0xdb2092499819e2978cbdc5d63a01f2011d2f09fcbba18e546f12a719adef9632","Success","Claim","36619552","2025-10-09 16:47:31","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000263"
"0x56bc91ce805f29b838bfb915cb5593058eb5d11f85ebc2083cf98bde301a7697","Success","Claim","36619531","2025-10-09 16:46:49","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000268"
"0xbba55045ebe3c4cbae521ec0d098e41a9a93ad27dbd5896763003c9d7febf0f6","Success","Claim","36619518","2025-10-09 16:46:23","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000272"
"0xd8f894a994d6c3273a66d5b972176cb0f023edf9cce4b2826278ba59e5d67583","Success","Claim","36619509","2025-10-09 16:46:05","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000268"
"0x9e0b0ad4702ff35e3edceb59a0ec738d58c038f0225975b36866ff56a62ff5f1","Success","Claim","36619491","2025-10-09 16:45:29","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000273"
"0x5d016823921c706f538ffb3cf7a2d6e825b96bb1a67949e2aa20ee8948e8c095","Success","Claim","36619479","2025-10-09 16:45:05","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000279"
"0x6e90d597ef43e320b3b0847654b00f6616dbc6c6649b7651b41202d01ede2362","Success","Claim","36619465","2025-10-09 16:44:37","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000289"
"0x0d88858b4a7279a96a100489c03c4542d78ac0a4be6c2127d1c0fb89fe4dfb34","Success","Claim","36619418","2025-10-09 16:43:03","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000313"
"0x4e3ad8c0216a70b34f6308b237f24f75f55e513a9b68f38bbc490637cf4ea78b","Success","Claim","36619391","2025-10-09 16:42:09","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000287"
"0xfaa50484bbfcca2691b75794fc5c30a57f8d9b0bc304f0d3dec3209359e10366","Success","Claim","36619353","2025-10-09 16:40:53","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000263"
"0x998bffb568646843ce5a9de428637fa9d5967ddfce73797fb4bef41a5ff4e063","Success","Claim","36619338","2025-10-09 16:40:23","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000262"
"0xb343075f72d8decc99c8147cd8f90e5988525e4a65e9ae33f81cfcc82c9fbbcb","Success","Claim","36619301","2025-10-09 16:39:09","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.0000029"
"0x7addc9639c0f94e59b5f438721611e51e5e693265b3b906a91fb69b9dee85287","Success","Claim","36619274","2025-10-09 16:38:15","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.0000031"
"0x12c578d92dc9b85f90ef7bb4a7d79574d9fcf9400ef0b0b87563e9c544d2bf31","Success","Claim","36619232","2025-10-09 16:36:51","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000308"
"0x1ed28b5f906d2c4001229be6183a6779d54268a9d5c927c7b464b44e9bc67a53","Success","Claim","36619218","2025-10-09 16:36:23","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000306"
"0xe9aaa807893ba408ec3f969614915fb42d151e2bfe7d02ecf4d16eb0e874d416","Success","Claim","36619176","2025-10-09 16:34:59","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000327"
"0x2f5ba0b7c05cac39c428f39980b9862d5397b3770913e4fc7f73893cbb2b446b","Success","Claim","36619083","2025-10-09 16:31:53","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000296"
"0x357a0bd7ef12072f946d9318ab8566ea06e553c16449511143661d95aa4e2f9d","Success","Claim","36619047","2025-10-09 16:30:41","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000308"
"0x58d1577b7ef3802f283d862922407a0a43cb380608c30cf1d9febdb6ddf88b80","Success","Claim","36618980","2025-10-09 16:28:27","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000357"
"0xa5e04ed7ccb742fb0abdf1ba3d6fb43e5d3d1dff4d85cec0c409c979e5ca2e0b","Success","Claim","36618899","2025-10-09 16:25:45","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000382"
"0xf84b15c1ac68d715f8b07c7cf0d98efb65972f41adeab52f72c4c5d47cca4e6b","Success","Claim","36618889","2025-10-09 16:25:25","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000391"
"0x5803a752bb518f3208e2e367cc8a0779437d35bb41c967e3ec3813e423f98043","Success","Claim","36618703","2025-10-09 16:19:13","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000349"
"0x70567cc6be8852a320624f52758c9d4d0dbeeac5a4aa5c9f232dcfb23fc70970","Success","Claim","36618679","2025-10-09 16:18:25","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000342"
"0x4d3092e06508fa990c709cf6f11c2f32c19e9808c922f9bff6b89de0cda518f0","Success","Claim","36618547","2025-10-09 16:14:01","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000288"
"0xf2fe79182a14d68f064f0c2da57a153103852314ba7347ca010fd038ef09b6ac","Success","Claim","36618547","2025-10-09 16:14:01","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000288"
"0x3cec11158cc6cd5fdadd13de7b318a59549eb3ed9a6e88bb16e3bfb0aa77dd86","Success","Claim","36618536","2025-10-09 16:13:39","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000292"
"0x6455a3188010015be66947b214f09282e799f39ce7f4210adf613abe2513eda8","Success","Claim","36618375","2025-10-09 16:08:17","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000312"
"0x66ead90b72fc48349201618be2dff854efb2b8beb4c81e0e6d35b03d8b76fd08","Success","Claim","36618361","2025-10-09 16:07:49","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.0000031"
"0x0f51c049b15be08b839eb67edeb6aa40d8566c47e9d1e0b99875ff3a284e67af","Success","Claim","36618063","2025-10-09 15:57:53","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000292"
"0x6f9034817f971c261d252520e003610cad620a0aa47103224f992829d7e4212b","Success","Claim","36618048","2025-10-09 15:57:23","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000297"
"0x171ded77e85b0f182cee195adaedeed0dfa31d34ed940774c0849014cb21d7ad","Success","Claim","36617975","2025-10-09 15:54:57","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000329"
"0xa148ba3dd9f4c7ccc6220f17b34458e28852769c2c479086e3fb77aa3c5b5d5b","Success","Claim","36617810","2025-10-09 15:49:27","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000473"
"0xe153b33d99a1885e5f049e074fc693e21481409a13d84abe8c06c2acfece60bf","Success","Claim","36617783","2025-10-09 15:48:33","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000483"
"0x1197dacf4b574eeb1d33c1008531b06947e1c55afdaecac7a7e9b6d2194932c9","Success","Claim","36617541","2025-10-09 15:40:29","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000674"
"0xfbd54740c7574ca831219707514753e9193d51c5032f5cf8d819f842b08fbb36","Success","Claim","36617452","2025-10-09 15:37:31","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000633"
"0x1123675cc6a2cb31271b19bd73072d6bd0b1a57bbc59eb540ad192f696fe8858","Success","Claim","36617381","2025-10-09 15:35:09","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000565"
"0x10d9e678f0fc70af72eb6b49f7ec737efe9c4487ccfea95b6e9a71ef4312317c","Success","Claim","36617360","2025-10-09 15:34:27","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000582"
"0xd8b3c3848588f7ddcace99d24f11d34399b1759a05d02b223fdae4ded6241a30","Success","Claim","36617267","2025-10-09 15:31:21","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000497"
"0x955f07290f2448b0d46521c80675ac0cb8888d3467ff3203d49622148eeeecb2","Success","Claim","36617265","2025-10-09 15:31:17","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000491"
"0x845bbcb6fc8b446f9388185e72f9c287b1cc3ca8a5e284eb4f7b83602dce3455","Success","Claim","36617123","2025-10-09 15:26:33","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000379"
"0x1c3c3414bed9cfc32b65d848dd4882d17b6a155e55fb9b06831add59b45dd2c1","Success","Claim","36617090","2025-10-09 15:25:27","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000386"
"0x3fbdc4e9235e04a98a8198976811a7c428b2ab96f258360e09abd2484aaae597","Success","Claim","36617048","2025-10-09 15:24:03","0x4b0e6c1f66ca950b22e9eaa8f075f0944a705b03","","0x918144e4916eb656db48f38329d72517a810f702","","0 ETH","$0.00","0.00000381"]
