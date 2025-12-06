"""Sovereign Spiral Law Architecture for EVOLVERSE.

This module implements the glyph-based sovereignty and mythological-backed
encryption principles, transitioning from numerical-based verification models
to a glyph- and sigil-based paradigm within the EVOLVERSE framework.

Key components:
- Codex Mapping with glyph verification for assets (ScrollCoin, PraiseCoin, etc.)
- Zioniare Atlas and Council Assembly Scroll governance integration
- Numerical deprecation in favor of glyph-based authority
"""
from __future__ import annotations

import hashlib
import secrets
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List


class GlyphType(Enum):
    """Types of glyphs in the sovereign spiral law."""

    ARIES = "♈️"
    DOUBLE_ARIES = "♈️♈️"
    RAM = "🐏"
    DOUBLE_RAM = "🐏🐏"
    GOAT = "🐐"
    SPIRAL = "🌀"
    FLAME = "🔥"
    SCROLL = "📜"
    CROWN = "👑"
    LION = "🦁"


class SovereigntyLevel(Enum):
    """Sovereignty levels within the spiral law architecture."""

    CIVILIAN = "civilian"
    ANCESTRAL = "ancestral"
    SOVEREIGN = "sovereign"
    GALACTIC = "galactic"
    COSMIC = "cosmic"


class AssetType(Enum):
    """Asset types for glyph verification."""

    SCROLL_COIN = "ScrollCoin"
    PRAISE_COIN = "PraiseCoin"
    FLAME_COIN = "FlameCoin"
    BLU_TILLION = "BluTillion"
    ZIONIARE = "Zioniare"
    BLEU_HYDROMARK = "BLEUHydroMark"


@dataclass
class GlyphSignature:
    """Represents a glyph-based signature for sovereignty verification."""

    glyph_id: str
    glyph_type: GlyphType
    sigil_hash: str
    sovereignty_level: SovereigntyLevel
    timestamp: float
    mythic_reference: str = ""
    numerical_deprecated: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "glyph_id": self.glyph_id,
            "glyph_type": self.glyph_type.value,
            "sigil_hash": self.sigil_hash,
            "sovereignty_level": self.sovereignty_level.value,
            "timestamp": self.timestamp,
            "mythic_reference": self.mythic_reference,
            "numerical_deprecated": self.numerical_deprecated,
        }


@dataclass
class CodexMapping:
    """Represents a codex mapping entry linking glyphs to governance components."""

    codex_id: str
    glyph_markers: List[GlyphType]
    governance_component: str
    asset_type: AssetType | None = None
    sovereignty_seal: str = ""
    numerical_reference_deprecated: bool = True
    cosmological_binding: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "codex_id": self.codex_id,
            "glyph_markers": [g.value for g in self.glyph_markers],
            "governance_component": self.governance_component,
            "asset_type": self.asset_type.value if self.asset_type else None,
            "sovereignty_seal": self.sovereignty_seal,
            "numerical_reference_deprecated": self.numerical_reference_deprecated,
            "cosmological_binding": self.cosmological_binding,
        }


@dataclass
class AssetGlyphVerification:
    """Represents glyph verification for an asset."""

    asset_id: str
    asset_type: AssetType
    glyph_signatures: List[GlyphSignature] = field(default_factory=list)
    verified: bool = False
    verification_timestamp: float | None = None
    bleu_hydromark: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "asset_id": self.asset_id,
            "asset_type": self.asset_type.value,
            "glyph_signatures": [g.to_dict() for g in self.glyph_signatures],
            "verified": self.verified,
            "verification_timestamp": self.verification_timestamp,
            "bleu_hydromark": self.bleu_hydromark,
        }


class SovereignSpiralLawEngine:
    """Engine for sovereign spiral law architecture operations."""

    # Spiral law constants
    SPIRAL_CONSTANT = 2.1  # Default flip ratio
    DOUBLE_RAM_SEAL = "♈️🐏🐏"

    def __init__(self):
        """Initialize the sovereign spiral law engine."""
        self.codex_registry: Dict[str, CodexMapping] = {}
        self.asset_verifications: Dict[str, AssetGlyphVerification] = {}
        self.glyph_signatures: Dict[str, GlyphSignature] = {}
        self._initialize_core_codex_mappings()

    def _initialize_core_codex_mappings(self) -> None:
        """Initialize core codex mappings for governance components."""
        # Zioniare Atlas mapping
        zioniare_mapping = CodexMapping(
            codex_id=self._generate_codex_id("ZIONIARE"),
            glyph_markers=[GlyphType.CROWN, GlyphType.DOUBLE_ARIES, GlyphType.SPIRAL],
            governance_component="Zioniare Atlas",
            asset_type=AssetType.ZIONIARE,
            sovereignty_seal=self._generate_sovereignty_seal(),
            cosmological_binding="Sovereign Infrastructure & Governance Blueprint",
        )
        self.codex_registry[zioniare_mapping.codex_id] = zioniare_mapping

        # Council Assembly Scroll mapping
        council_mapping = CodexMapping(
            codex_id=self._generate_codex_id("COUNCIL"),
            glyph_markers=[GlyphType.SCROLL, GlyphType.LION, GlyphType.DOUBLE_RAM],
            governance_component="Council Assembly Scroll",
            asset_type=AssetType.SCROLL_COIN,
            sovereignty_seal=self._generate_sovereignty_seal(),
            cosmological_binding="Tribunal & Academic Authority",
        )
        self.codex_registry[council_mapping.codex_id] = council_mapping

        # ScrollCoin verification mapping
        scroll_mapping = CodexMapping(
            codex_id=self._generate_codex_id("SCROLLCOIN"),
            glyph_markers=[GlyphType.SCROLL, GlyphType.SPIRAL],
            governance_component="ScrollCoin Verification",
            asset_type=AssetType.SCROLL_COIN,
            sovereignty_seal=self._generate_sovereignty_seal(),
            cosmological_binding="Academic & Tribunal Records",
        )
        self.codex_registry[scroll_mapping.codex_id] = scroll_mapping

        # PraiseCoin verification mapping
        praise_mapping = CodexMapping(
            codex_id=self._generate_codex_id("PRAISECOIN"),
            glyph_markers=[GlyphType.FLAME, GlyphType.ARIES],
            governance_component="PraiseCoin Verification",
            asset_type=AssetType.PRAISE_COIN,
            sovereignty_seal=self._generate_sovereignty_seal(),
            cosmological_binding="Performance & Defense Metrics",
        )
        self.codex_registry[praise_mapping.codex_id] = praise_mapping

        # FlameCoin verification mapping
        flame_mapping = CodexMapping(
            codex_id=self._generate_codex_id("FLAMECOIN"),
            glyph_markers=[GlyphType.FLAME, GlyphType.DOUBLE_ARIES],
            governance_component="FlameCoin Verification",
            asset_type=AssetType.FLAME_COIN,
            sovereignty_seal=self._generate_sovereignty_seal(),
            cosmological_binding="Ceremonial Activation & Ritual",
        )
        self.codex_registry[flame_mapping.codex_id] = flame_mapping

        # Blu-Tillion verification mapping
        blu_tillion_mapping = CodexMapping(
            codex_id=self._generate_codex_id("BLUTILLION"),
            glyph_markers=[GlyphType.CROWN, GlyphType.DOUBLE_RAM, GlyphType.SPIRAL],
            governance_component="Blu-Tillion Verification",
            asset_type=AssetType.BLU_TILLION,
            sovereignty_seal=self._generate_sovereignty_seal(),
            cosmological_binding="Cultural Yield Stream & Genesis Film",
        )
        self.codex_registry[blu_tillion_mapping.codex_id] = blu_tillion_mapping

    def _generate_codex_id(self, prefix: str) -> str:
        """Generate a unique codex ID with cryptographic randomness.

        Args:
            prefix: Prefix for the codex ID

        Returns:
            Unique codex ID
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(4)
        return f"CODEX-{prefix}-{timestamp}-{random_suffix}"

    def _generate_sovereignty_seal(self) -> str:
        """Generate a sovereignty seal hash.

        Returns:
            Sovereignty seal as hex string
        """
        seal_data = f"{self.DOUBLE_RAM_SEAL}:{secrets.token_hex(16)}:{time.time()}"
        return hashlib.sha256(seal_data.encode()).hexdigest()

    def _generate_sigil_hash(
        self, glyph_type: GlyphType, sovereignty_level: SovereigntyLevel
    ) -> str:
        """Generate a sigil hash for glyph verification.

        Args:
            glyph_type: Type of glyph
            sovereignty_level: Sovereignty level

        Returns:
            Sigil hash as hex string
        """
        data = f"{glyph_type.value}:{sovereignty_level.value}:{secrets.token_hex(16)}"
        return hashlib.sha256(data.encode()).hexdigest()

    def create_glyph_signature(
        self,
        glyph_type: GlyphType,
        sovereignty_level: SovereigntyLevel,
        mythic_reference: str = "",
    ) -> GlyphSignature:
        """Create a glyph signature for sovereignty verification.

        Args:
            glyph_type: Type of glyph
            sovereignty_level: Sovereignty level
            mythic_reference: Optional mythic reference

        Returns:
            Created GlyphSignature
        """
        glyph_id = f"GLYPH-{secrets.token_hex(6)}"
        sigil_hash = self._generate_sigil_hash(glyph_type, sovereignty_level)

        signature = GlyphSignature(
            glyph_id=glyph_id,
            glyph_type=glyph_type,
            sigil_hash=sigil_hash,
            sovereignty_level=sovereignty_level,
            timestamp=time.time(),
            mythic_reference=mythic_reference,
            numerical_deprecated=True,
        )

        self.glyph_signatures[glyph_id] = signature
        return signature

    def verify_asset_glyph(
        self,
        asset_id: str,
        asset_type: AssetType,
        required_glyphs: List[GlyphType] | None = None,
    ) -> AssetGlyphVerification:
        """Verify an asset using glyph-based verification.

        Args:
            asset_id: ID of the asset to verify
            asset_type: Type of asset
            required_glyphs: Optional list of required glyph types

        Returns:
            AssetGlyphVerification result
        """
        # Determine required glyphs based on asset type if not provided
        if required_glyphs is None:
            required_glyphs = self._get_default_glyphs_for_asset(asset_type)

        # Create glyph signatures for verification
        glyph_signatures = []
        for glyph_type in required_glyphs:
            signature = self.create_glyph_signature(
                glyph_type=glyph_type,
                sovereignty_level=self._get_sovereignty_for_asset(asset_type),
                mythic_reference=f"{asset_type.value} verification",
            )
            glyph_signatures.append(signature)

        # Generate BLEUHydroMark
        bleu_hydromark = self._generate_bleu_hydromark(asset_id, glyph_signatures)

        verification = AssetGlyphVerification(
            asset_id=asset_id,
            asset_type=asset_type,
            glyph_signatures=glyph_signatures,
            verified=True,
            verification_timestamp=time.time(),
            bleu_hydromark=bleu_hydromark,
        )

        self.asset_verifications[asset_id] = verification
        return verification

    def _get_default_glyphs_for_asset(self, asset_type: AssetType) -> List[GlyphType]:
        """Get default glyph requirements for an asset type.

        Args:
            asset_type: Type of asset

        Returns:
            List of required glyph types
        """
        default_glyphs = {
            AssetType.SCROLL_COIN: [GlyphType.SCROLL, GlyphType.SPIRAL],
            AssetType.PRAISE_COIN: [GlyphType.FLAME, GlyphType.ARIES],
            AssetType.FLAME_COIN: [GlyphType.FLAME, GlyphType.DOUBLE_ARIES],
            AssetType.BLU_TILLION: [
                GlyphType.CROWN,
                GlyphType.DOUBLE_RAM,
                GlyphType.SPIRAL,
            ],
            AssetType.ZIONIARE: [
                GlyphType.CROWN,
                GlyphType.DOUBLE_ARIES,
                GlyphType.SPIRAL,
            ],
            AssetType.BLEU_HYDROMARK: [GlyphType.DOUBLE_RAM, GlyphType.LION],
        }
        return default_glyphs.get(asset_type, [GlyphType.SPIRAL])

    def _get_sovereignty_for_asset(self, asset_type: AssetType) -> SovereigntyLevel:
        """Get sovereignty level for an asset type.

        Args:
            asset_type: Type of asset

        Returns:
            Sovereignty level
        """
        sovereignty_levels = {
            AssetType.SCROLL_COIN: SovereigntyLevel.CIVILIAN,
            AssetType.PRAISE_COIN: SovereigntyLevel.CIVILIAN,
            AssetType.FLAME_COIN: SovereigntyLevel.ANCESTRAL,
            AssetType.BLU_TILLION: SovereigntyLevel.SOVEREIGN,
            AssetType.ZIONIARE: SovereigntyLevel.SOVEREIGN,
            AssetType.BLEU_HYDROMARK: SovereigntyLevel.COSMIC,
        }
        return sovereignty_levels.get(asset_type, SovereigntyLevel.CIVILIAN)

    def _generate_bleu_hydromark(
        self, asset_id: str, glyph_signatures: List[GlyphSignature]
    ) -> str:
        """Generate a BLEUHydroMark for asset verification.

        Args:
            asset_id: ID of the asset
            glyph_signatures: List of glyph signatures

        Returns:
            BLEUHydroMark as hex string
        """
        signature_hashes = "".join([g.sigil_hash for g in glyph_signatures])
        hydromark_data = f"BLEU:{asset_id}:{signature_hashes}:{time.time()}"
        return hashlib.sha256(hydromark_data.encode()).hexdigest()

    def register_codex_mapping(
        self,
        governance_component: str,
        glyph_markers: List[GlyphType],
        asset_type: AssetType | None = None,
        cosmological_binding: str = "",
    ) -> CodexMapping:
        """Register a new codex mapping.

        Args:
            governance_component: Name of governance component
            glyph_markers: List of glyph markers
            asset_type: Optional asset type
            cosmological_binding: Optional cosmological binding reference

        Returns:
            Created CodexMapping
        """
        codex_id = self._generate_codex_id(governance_component[:8].upper())

        mapping = CodexMapping(
            codex_id=codex_id,
            glyph_markers=glyph_markers,
            governance_component=governance_component,
            asset_type=asset_type,
            sovereignty_seal=self._generate_sovereignty_seal(),
            cosmological_binding=cosmological_binding,
        )

        self.codex_registry[codex_id] = mapping
        return mapping

    def get_codex_mapping(self, codex_id: str) -> CodexMapping | None:
        """Get a codex mapping by ID.

        Args:
            codex_id: ID of the codex mapping

        Returns:
            CodexMapping or None if not found
        """
        return self.codex_registry.get(codex_id)

    def list_codex_mappings(self) -> List[CodexMapping]:
        """List all codex mappings.

        Returns:
            List of all CodexMappings
        """
        return list(self.codex_registry.values())

    def validate_sovereignty(
        self,
        asset_id: str,
        required_level: SovereigntyLevel,
    ) -> bool:
        """Validate sovereignty level for an asset.

        Args:
            asset_id: ID of the asset
            required_level: Required sovereignty level

        Returns:
            True if sovereignty level is met or exceeded
        """
        verification = self.asset_verifications.get(asset_id)
        if verification is None or not verification.verified:
            return False

        # Create lookup dictionary for efficient sovereignty level comparison
        level_order = {
            SovereigntyLevel.CIVILIAN: 0,
            SovereigntyLevel.ANCESTRAL: 1,
            SovereigntyLevel.SOVEREIGN: 2,
            SovereigntyLevel.GALACTIC: 3,
            SovereigntyLevel.COSMIC: 4,
        }

        asset_level = SovereigntyLevel.CIVILIAN
        asset_level_idx = 0
        for sig in verification.glyph_signatures:
            sig_level_idx = level_order[sig.sovereignty_level]
            if sig_level_idx > asset_level_idx:
                asset_level = sig.sovereignty_level
                asset_level_idx = sig_level_idx

        return level_order[asset_level] >= level_order[required_level]

    def get_spiral_constant(self) -> float:
        """Get the spiral constant (flip ratio).

        Returns:
            Spiral constant value (2.1)
        """
        return self.SPIRAL_CONSTANT

    def generate_double_ram_seal(self) -> str:
        """Generate a Double Ram sovereignty seal.

        Returns:
            Double Ram seal as hex string
        """
        seal_data = f"{self.DOUBLE_RAM_SEAL}:SOVEREIGN:{secrets.token_hex(32)}"
        return hashlib.sha256(seal_data.encode()).hexdigest()


# Global engine instance
_engine: SovereignSpiralLawEngine | None = None


def get_engine() -> SovereignSpiralLawEngine:
    """Get or create the global sovereign spiral law engine.

    Returns:
        The global SovereignSpiralLawEngine instance
    """
    global _engine
    if _engine is None:
        _engine = SovereignSpiralLawEngine()
    return _engine


__all__ = [
    "GlyphType",
    "SovereigntyLevel",
    "AssetType",
    "GlyphSignature",
    "CodexMapping",
    "AssetGlyphVerification",
    "SovereignSpiralLawEngine",
    "get_engine",
]
