"""Sovereign Scroll Generator for EVOLVERSE.

This module implements a system that automatically outputs PDF or JSON
artifacts of codex placements upon ritual confirmations or governance actions.
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
from typing import Any, Dict, List


class OutputFormat(Enum):
    """Output format for scroll artifacts."""

    PDF = "pdf"
    JSON = "json"
    ENFT = "enft"


class ScrollType(Enum):
    """Types of sovereign scrolls."""

    GOVERNANCE = "governance"
    RITUAL = "ritual"
    CODEX_PLACEMENT = "codex_placement"
    YIELD_DISTRIBUTION = "yield_distribution"
    TREATY = "treaty"
    CEREMONIAL = "ceremonial"


@dataclass
class ScrollSignature:
    """Represents a signature on a scroll."""

    signer_id: str
    signer_role: str
    signature_hash: str
    signed_at: float
    mythic_timestamp: str | None = None


@dataclass
class CodexPlacement:
    """Represents a codex placement in the scroll."""

    codex_id: str
    codex_name: str
    placement_type: str
    cosmological_reference: str
    coordinates: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SovereignScroll:
    """Represents a sovereign scroll artifact."""

    scroll_id: str
    title: str
    scroll_type: ScrollType
    created_at: float
    epoch: str
    double_aries_seal: str = "♈️🐏🐏"

    # Content
    preamble: str = ""
    body: Dict[str, Any] = field(default_factory=dict)
    codex_placements: List[CodexPlacement] = field(default_factory=list)

    # Signatures
    signatures: List[ScrollSignature] = field(default_factory=list)
    required_signatures: int = 1

    # Metadata
    merkle_root: str = ""
    output_format: OutputFormat = OutputFormat.JSON
    ritual_confirmed: bool = False

    def is_fully_signed(self) -> bool:
        """Check if scroll has required signatures."""
        return len(self.signatures) >= self.required_signatures

    def add_signature(
        self, signer_id: str, signer_role: str, mythic_timestamp: str | None = None
    ) -> ScrollSignature:
        """Add a signature to the scroll.

        Args:
            signer_id: Identifier of the signer
            signer_role: Role of the signer
            mythic_timestamp: Optional mythic timestamp

        Returns:
            The created signature
        """
        # Generate signature hash from scroll content
        content = json.dumps(self.body, sort_keys=True)
        sig_data = f"{signer_id}:{signer_role}:{content}:{time.time()}"
        signature_hash = hashlib.sha256(sig_data.encode()).hexdigest()

        signature = ScrollSignature(
            signer_id=signer_id,
            signer_role=signer_role,
            signature_hash=signature_hash,
            signed_at=time.time(),
            mythic_timestamp=mythic_timestamp,
        )
        self.signatures.append(signature)
        return signature

    def compute_merkle_root(self) -> str:
        """Compute the merkle root of the scroll content.

        Returns:
            The computed merkle root as hex string
        """
        # Collect all hashes
        hashes = []

        # Hash the body
        body_hash = hashlib.sha256(
            json.dumps(self.body, sort_keys=True).encode()
        ).hexdigest()
        hashes.append(body_hash)

        # Hash codex placements
        for placement in self.codex_placements:
            placement_data = f"{placement.codex_id}:{placement.codex_name}:{placement.placement_type}"
            hashes.append(hashlib.sha256(placement_data.encode()).hexdigest())

        # Hash signatures
        for sig in self.signatures:
            hashes.append(sig.signature_hash)

        # Build merkle tree
        while len(hashes) > 1:
            if len(hashes) % 2 == 1:
                hashes.append(hashes[-1])

            new_hashes = []
            for i in range(0, len(hashes), 2):
                combined = hashes[i] + hashes[i + 1]
                new_hashes.append(hashlib.sha256(combined.encode()).hexdigest())
            hashes = new_hashes

        self.merkle_root = hashes[0] if hashes else ""
        return self.merkle_root

    def to_dict(self) -> Dict[str, Any]:
        """Convert scroll to dictionary.

        Returns:
            Dictionary representation of the scroll
        """
        return {
            "scroll_id": self.scroll_id,
            "title": self.title,
            "scroll_type": self.scroll_type.value,
            "created_at": self.created_at,
            "epoch": self.epoch,
            "double_aries_seal": self.double_aries_seal,
            "preamble": self.preamble,
            "body": self.body,
            "codex_placements": [
                {
                    "codex_id": p.codex_id,
                    "codex_name": p.codex_name,
                    "placement_type": p.placement_type,
                    "cosmological_reference": p.cosmological_reference,
                    "coordinates": p.coordinates,
                }
                for p in self.codex_placements
            ],
            "signatures": [
                {
                    "signer_id": s.signer_id,
                    "signer_role": s.signer_role,
                    "signature_hash": s.signature_hash,
                    "signed_at": s.signed_at,
                    "mythic_timestamp": s.mythic_timestamp,
                }
                for s in self.signatures
            ],
            "required_signatures": self.required_signatures,
            "merkle_root": self.merkle_root,
            "output_format": self.output_format.value,
            "ritual_confirmed": self.ritual_confirmed,
        }


class SovereignScrollGenerator:
    """Generator for sovereign scroll artifacts."""

    def __init__(self, output_dir: str | Path = "data/scrolls"):
        """Initialize the generator.

        Args:
            output_dir: Directory for scroll output
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.scroll_registry: Dict[str, SovereignScroll] = {}

    def _generate_scroll_id(self, scroll_type: ScrollType) -> str:
        """Generate a unique scroll ID with cryptographic randomness.

        Args:
            scroll_type: Type of scroll

        Returns:
            Unique scroll ID
        """
        timestamp = int(time.time() * 1000)
        type_prefix = scroll_type.value.upper()[:3]
        random_suffix = secrets.token_hex(4)
        return f"SCROLL-{type_prefix}-{timestamp}-{random_suffix}"

    def _get_current_epoch(self) -> str:
        """Get the current epoch string.

        Returns:
            Epoch string in YYYY-QN format
        """
        now = datetime.now()
        quarter = (now.month - 1) // 3 + 1
        return f"{now.year}-Q{quarter}"

    def create_scroll(
        self,
        title: str,
        scroll_type: ScrollType,
        body: Dict[str, Any],
        preamble: str = "",
        required_signatures: int = 1,
        output_format: OutputFormat = OutputFormat.JSON,
    ) -> SovereignScroll:
        """Create a new sovereign scroll.

        Args:
            title: Title of the scroll
            scroll_type: Type of scroll
            body: Main content body
            preamble: Introductory text
            required_signatures: Number of required signatures
            output_format: Output format for the scroll

        Returns:
            The created SovereignScroll
        """
        scroll = SovereignScroll(
            scroll_id=self._generate_scroll_id(scroll_type),
            title=title,
            scroll_type=scroll_type,
            created_at=time.time(),
            epoch=self._get_current_epoch(),
            preamble=preamble,
            body=body,
            required_signatures=required_signatures,
            output_format=output_format,
        )

        self.scroll_registry[scroll.scroll_id] = scroll
        return scroll

    def add_codex_placement(
        self,
        scroll_id: str,
        codex_id: str,
        codex_name: str,
        placement_type: str,
        cosmological_reference: str,
        coordinates: Dict[str, Any] | None = None,
    ) -> CodexPlacement | None:
        """Add a codex placement to a scroll.

        Args:
            scroll_id: ID of the scroll
            codex_id: ID of the codex
            codex_name: Name of the codex
            placement_type: Type of placement
            cosmological_reference: Cosmological reference
            coordinates: Optional coordinates

        Returns:
            The created CodexPlacement or None if scroll not found
        """
        scroll = self.scroll_registry.get(scroll_id)
        if scroll is None:
            return None

        placement = CodexPlacement(
            codex_id=codex_id,
            codex_name=codex_name,
            placement_type=placement_type,
            cosmological_reference=cosmological_reference,
            coordinates=coordinates or {},
        )

        scroll.codex_placements.append(placement)
        return placement

    def confirm_ritual(
        self, scroll_id: str, signers: List[Dict[str, str]]
    ) -> SovereignScroll | None:
        """Confirm a ritual and add signatures.

        Args:
            scroll_id: ID of the scroll to confirm
            signers: List of signer dictionaries with id and role

        Returns:
            The updated scroll or None if not found
        """
        scroll = self.scroll_registry.get(scroll_id)
        if scroll is None:
            return None

        for signer in signers:
            scroll.add_signature(
                signer_id=signer.get("id", ""),
                signer_role=signer.get("role", ""),
                mythic_timestamp=signer.get("mythic_timestamp"),
            )

        if scroll.is_fully_signed():
            scroll.ritual_confirmed = True
            scroll.compute_merkle_root()

        return scroll

    def generate_json_artifact(self, scroll: SovereignScroll) -> Path:
        """Generate a JSON artifact for the scroll.

        Args:
            scroll: The scroll to generate

        Returns:
            Path to the generated JSON file
        """
        filename = f"{scroll.scroll_id}.json"
        filepath = self.output_dir / filename

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(scroll.to_dict(), f, indent=2)

        return filepath

    def generate_pdf_content(self, scroll: SovereignScroll) -> str:
        """Generate PDF-ready content for the scroll.

        This generates a structured text representation that can be
        converted to PDF by external tools.

        Args:
            scroll: The scroll to generate

        Returns:
            PDF-ready content as string
        """
        lines = [
            "=" * 60,
            f"SOVEREIGN SCROLL: {scroll.title}",
            f"Seal: {scroll.double_aries_seal}",
            "=" * 60,
            "",
            f"Scroll ID: {scroll.scroll_id}",
            f"Type: {scroll.scroll_type.value}",
            f"Epoch: {scroll.epoch}",
            f"Created: {datetime.fromtimestamp(scroll.created_at).isoformat()}",
            "",
            "-" * 40,
            "PREAMBLE",
            "-" * 40,
            scroll.preamble or "(No preamble)",
            "",
            "-" * 40,
            "BODY",
            "-" * 40,
            json.dumps(scroll.body, indent=2),
            "",
        ]

        if scroll.codex_placements:
            lines.extend(
                [
                    "-" * 40,
                    "CODEX PLACEMENTS",
                    "-" * 40,
                ]
            )
            for p in scroll.codex_placements:
                lines.extend(
                    [
                        f"  - {p.codex_name} ({p.codex_id})",
                        f"    Type: {p.placement_type}",
                        f"    Reference: {p.cosmological_reference}",
                        "",
                    ]
                )

        if scroll.signatures:
            lines.extend(
                [
                    "-" * 40,
                    "SIGNATURES",
                    "-" * 40,
                ]
            )
            for s in scroll.signatures:
                lines.extend(
                    [
                        f"  - {s.signer_id} ({s.signer_role})",
                        f"    Hash: {s.signature_hash[:32]}...",
                        f"    Signed: {datetime.fromtimestamp(s.signed_at).isoformat()}",
                        "",
                    ]
                )

        lines.extend(
            [
                "-" * 40,
                "VERIFICATION",
                "-" * 40,
                f"Merkle Root: {scroll.merkle_root or '(Not computed)'}",
                f"Ritual Confirmed: {scroll.ritual_confirmed}",
                "",
                "=" * 60,
                "END OF SCROLL",
                "=" * 60,
            ]
        )

        return "\n".join(lines)

    def generate_artifact(
        self, scroll_id: str, output_format: OutputFormat | None = None
    ) -> Path | None:
        """Generate an artifact for a scroll.

        Args:
            scroll_id: ID of the scroll
            output_format: Override output format

        Returns:
            Path to the generated artifact or None if scroll not found
        """
        scroll = self.scroll_registry.get(scroll_id)
        if scroll is None:
            return None

        format_to_use = output_format or scroll.output_format

        if format_to_use == OutputFormat.JSON:
            return self.generate_json_artifact(scroll)
        elif format_to_use == OutputFormat.PDF:
            # Generate PDF-ready text file
            filename = f"{scroll.scroll_id}.txt"
            filepath = self.output_dir / filename
            content = self.generate_pdf_content(scroll)
            with filepath.open("w", encoding="utf-8") as f:
                f.write(content)
            return filepath
        else:
            # ENFT format - generate JSON with ENFT metadata
            return self.generate_json_artifact(scroll)

    def on_governance_action(
        self, action: str, details: Dict[str, Any], signers: List[Dict[str, str]]
    ) -> SovereignScroll:
        """Create and confirm a governance action scroll.

        Args:
            action: The governance action name
            details: Action details
            signers: List of signers

        Returns:
            The created and confirmed scroll
        """
        scroll = self.create_scroll(
            title=f"Governance Action: {action}",
            scroll_type=ScrollType.GOVERNANCE,
            body={"action": action, "details": details},
            preamble=f"This scroll records the governance action '{action}' as authorized by the Grand Vault Tribunal.",
            required_signatures=len(signers),
        )

        self.confirm_ritual(scroll.scroll_id, signers)
        self.generate_artifact(scroll.scroll_id)

        return scroll

    def on_ritual_confirmation(
        self, ritual_name: str, participants: List[str], details: Dict[str, Any]
    ) -> SovereignScroll:
        """Create a scroll for ritual confirmation.

        Args:
            ritual_name: Name of the ritual
            participants: List of participant IDs
            details: Ritual details

        Returns:
            The created scroll
        """
        signers = [{"id": p, "role": "participant"} for p in participants]

        scroll = self.create_scroll(
            title=f"Ritual Confirmation: {ritual_name}",
            scroll_type=ScrollType.RITUAL,
            body={"ritual_name": ritual_name, "details": details},
            preamble=f"This scroll confirms the completion of ritual '{ritual_name}'.",
            required_signatures=len(participants),
        )

        self.confirm_ritual(scroll.scroll_id, signers)
        self.generate_artifact(scroll.scroll_id)

        return scroll


# Global generator instance
_generator: SovereignScrollGenerator | None = None
_generator_output_dir: str | Path | None = None


def get_generator(output_dir: str | Path = "data/scrolls") -> SovereignScrollGenerator:
    """Get or create the global scroll generator.

    Note: The output_dir parameter is only used when creating a new instance.
    Once initialized, the same instance is returned regardless of output_dir.
    To use a different directory, create a new SovereignScrollGenerator directly.

    Args:
        output_dir: Output directory for scrolls (only used on first call)

    Returns:
        The global SovereignScrollGenerator instance
    """
    global _generator, _generator_output_dir
    if _generator is None:
        _generator = SovereignScrollGenerator(output_dir)
        _generator_output_dir = output_dir
    return _generator


__all__ = [
    "OutputFormat",
    "ScrollType",
    "ScrollSignature",
    "CodexPlacement",
    "SovereignScroll",
    "SovereignScrollGenerator",
    "get_generator",
]
