"""Proof-of-Flip Economic Audit Pipeline for EVOLVERSE.

This module implements audit logs reflecting runtime metrics, showcasing
yield differentials matched against the BLEUFLIP system's promises.
Integrates cross-referenced Mythic Proof Layers connecting practical
governance outcomes with ceremonial claims.

Includes Exponential Proof-of-Flip with spiral ledger protocols and
GoatFilter anti-mimic attributes for sovereign spiral law compliance.
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


class AuditStatus(Enum):
    """Status of an audit entry."""

    PENDING = "pending"
    VERIFIED = "verified"
    DISCREPANCY = "discrepancy"
    RESOLVED = "resolved"


class MythicProofLayer(Enum):
    """Mythic proof layers for ceremonial-governance integration."""

    GENESIS = "genesis"
    SPIRAL = "spiral"
    FLAME = "flame"
    TRIBUNAL = "tribunal"
    COSMIC = "cosmic"


class SpiralLedgerProtocol(Enum):
    """Spiral ledger protocols for exponential proof-of-flip."""

    STANDARD = "standard"
    EXPONENTIAL = "exponential"
    CEREMONIAL = "ceremonial"
    SOVEREIGN = "sovereign"
class GoatFilterMode(Enum):
    """Detection modes for GoatFilter anti-mimic attributes."""

    PASSIVE = "passive"
    ACTIVE = "active"
    AGGRESSIVE = "aggressive"


class GoatFilterAction(Enum):
    """Actions on detected mimic attempts."""

    BLOCK = "block"
    REDIRECT = "redirect"
    YIELD_MULTIPLY = "yield_multiply"


@dataclass
class GoatFilterResult:
    """Result of GoatFilter anti-mimic detection."""

    filter_id: str
    detected: bool
    detection_mode: GoatFilterMode
    action_taken: GoatFilterAction
    timestamp: float
    mimic_signature: str = ""
    glyph_marker: str = "🐐"
    neutralized: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "filter_id": self.filter_id,
            "detected": self.detected,
            "detection_mode": self.detection_mode.value,
            "action_taken": self.action_taken.value,
            "timestamp": self.timestamp,
            "mimic_signature": self.mimic_signature,
            "glyph_marker": self.glyph_marker,
            "neutralized": self.neutralized,
        }


@dataclass
class SpiralLedgerEntry:
    """Represents an entry in the spiral ledger protocol."""

    entry_id: str
    flip_ratio: float
    glyph_markers: List[str]
    timestamp: float
    block_number: int = 0
    previous_hash: str = ""
    entry_hash: str = ""
    sovereignty_level: str = "civilian"
    numerical_deprecated: bool = True

    def compute_hash(self) -> str:
        """Compute hash for the ledger entry.

        Returns:
            SHA-256 hash of the entry
        """
        data = {
            "entry_id": self.entry_id,
            "flip_ratio": self.flip_ratio,
            "glyph_markers": self.glyph_markers,
            "timestamp": self.timestamp,
            "block_number": self.block_number,
            "previous_hash": self.previous_hash,
        }
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "entry_id": self.entry_id,
            "flip_ratio": self.flip_ratio,
            "glyph_markers": self.glyph_markers,
            "timestamp": self.timestamp,
            "block_number": self.block_number,
            "previous_hash": self.previous_hash,
            "entry_hash": self.entry_hash,
            "sovereignty_level": self.sovereignty_level,
            "numerical_deprecated": self.numerical_deprecated,
        }


@dataclass
class YieldDifferential:
    """Represents a yield differential measurement."""

    expected_yield: float
    actual_yield: float
    differential: float
    differential_pct: float
    tri_cycle_number: int
    timestamp: float

    def is_within_tolerance(self, tolerance: float = 0.05) -> bool:
        """Check if differential is within acceptable tolerance.

        Args:
            tolerance: Acceptable tolerance as decimal (default 5%)

        Returns:
            True if within tolerance
        """
        return abs(self.differential_pct) <= tolerance


@dataclass
class RuntimeMetric:
    """Represents a runtime metric measurement."""

    metric_id: str
    metric_name: str
    value: float
    unit: str
    timestamp: float
    source: str
    mythic_layer: MythicProofLayer | None = None


@dataclass
class MythicProof:
    """Represents a mythic proof linking governance to ceremony."""

    proof_id: str
    layer: MythicProofLayer
    governance_outcome: str
    ceremonial_claim: str
    proof_hash: str
    verified: bool
    verification_timestamp: float | None = None
    act_scene_ref: str = ""  # EVOLVERSE Act I Scene reference


@dataclass
class SpiralLedgerEntry:
    """Represents a spiral ledger entry for exponential proof-of-flip.

    Implements spiral ledger protocols with governing flip ratios
    for sovereign spiral law compliance.
    """

    entry_id: str
    protocol: SpiralLedgerProtocol
    flip_ratio: float
    glyph_marker: str
    timestamp: float
    sovereign_seal: str
    goat_filter_applied: bool = False
    anti_mimic_verified: bool = False
    spiral_hash: str = ""

    def compute_spiral_hash(self) -> str:
        """Compute spiral hash for the ledger entry.

        Returns:
            SHA-256 hash with spiral encoding
        """
        data = f"{self.entry_id}:{self.protocol.value}:{self.flip_ratio}:{self.glyph_marker}"
        base_hash = hashlib.sha256(data.encode()).hexdigest()
        # Apply spiral encoding
        self.spiral_hash = f"SPIRAL-{base_hash[:48]}"
        return self.spiral_hash


class GoatFilter:
    """Anti-mimic filter for audit operations.

    Implements GoatFilter attributes to detect and prevent mimic
    systems from infiltrating sovereign spiral law operations.

    Note: This is a convenience wrapper that delegates to BaseGoatFilter
    from the shared goat_filter module.
    """

    # Goat (🐐) Capricorn Foundation symbolism
    GLYPH = "🐐"
    ZODIAC = "Capricorn"
    ELEMENT = "earth"

    def __init__(self, strictness: float = 0.95):
        """Initialize GoatFilter.

        Args:
            strictness: Filter strictness level (0.0-1.0, default 0.95)
        """
        # Import here to avoid circular imports
        from src.goat_filter import BaseGoatFilter

        self._base_filter = BaseGoatFilter(strictness)

    @property
    def strictness(self) -> float:
        """Get filter strictness."""
        return self._base_filter.strictness

    @property
    def mimic_patterns(self) -> List[str]:
        """Get mimic patterns list."""
        return self._base_filter.mimic_patterns

    @property
    def blocked_count(self) -> int:
        """Get blocked count."""
        return self._base_filter.blocked_count

    @property
    def verified_count(self) -> int:
        """Get verified count."""
        return self._base_filter.verified_count

    def add_mimic_pattern(self, pattern: str) -> None:
        """Add a known mimic pattern to filter.

        Args:
            pattern: Mimic pattern to block
        """
        self._base_filter.add_mimic_pattern(pattern)

    def verify_authenticity(self, data: Dict[str, Any]) -> bool:
        """Verify data authenticity against mimic patterns.

        Args:
            data: Data to verify

        Returns:
            True if data passes GoatFilter verification
        """
        return self._base_filter.verify_authenticity(data)

    def get_filter_stats(self) -> Dict[str, Any]:
        """Get filter statistics.

        Returns:
            Dictionary with filter statistics
        """
        stats = self._base_filter.get_filter_stats()
        # Remove element key for backward compatibility with existing code
        return {k: v for k, v in stats.items() if k != "active"}


@dataclass
class AuditEntry:
    """Represents a single audit log entry."""

    entry_id: str
    timestamp: float
    status: AuditStatus
    yield_differential: YieldDifferential | None
    runtime_metrics: List[RuntimeMetric]
    mythic_proofs: List[MythicProof]
    bleuflip_promise: Dict[str, Any]
    actual_outcome: Dict[str, Any]
    notes: str = ""

    def compute_hash(self) -> str:
        """Compute hash for the audit entry.

        Returns:
            SHA-256 hash of the entry
        """
        data = {
            "entry_id": self.entry_id,
            "timestamp": self.timestamp,
            "status": self.status.value,
            "yield_differential": (
                {
                    "expected": self.yield_differential.expected_yield,
                    "actual": self.yield_differential.actual_yield,
                    "differential": self.yield_differential.differential,
                }
                if self.yield_differential
                else None
            ),
            "bleuflip_promise": self.bleuflip_promise,
            "actual_outcome": self.actual_outcome,
        }
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary.

        Returns:
            Dictionary representation
        """
        return {
            "entry_id": self.entry_id,
            "timestamp": self.timestamp,
            "timestamp_iso": datetime.fromtimestamp(self.timestamp).isoformat(),
            "status": self.status.value,
            "yield_differential": (
                {
                    "expected_yield": self.yield_differential.expected_yield,
                    "actual_yield": self.yield_differential.actual_yield,
                    "differential": self.yield_differential.differential,
                    "differential_pct": self.yield_differential.differential_pct,
                    "tri_cycle_number": self.yield_differential.tri_cycle_number,
                }
                if self.yield_differential
                else None
            ),
            "runtime_metrics": [
                {
                    "metric_id": m.metric_id,
                    "metric_name": m.metric_name,
                    "value": m.value,
                    "unit": m.unit,
                    "source": m.source,
                    "mythic_layer": m.mythic_layer.value if m.mythic_layer else None,
                }
                for m in self.runtime_metrics
            ],
            "mythic_proofs": [
                {
                    "proof_id": p.proof_id,
                    "layer": p.layer.value,
                    "governance_outcome": p.governance_outcome,
                    "ceremonial_claim": p.ceremonial_claim,
                    "proof_hash": p.proof_hash,
                    "verified": p.verified,
                    "act_scene_ref": p.act_scene_ref,
                }
                for p in self.mythic_proofs
            ],
            "bleuflip_promise": self.bleuflip_promise,
            "actual_outcome": self.actual_outcome,
            "entry_hash": self.compute_hash(),
            "notes": self.notes,
        }


class ProofOfFlipAuditPipeline:
    """Audit pipeline for Proof-of-Flip economic verification.

    Implements exponential proof-of-flip with spiral ledger protocols
    and GoatFilter anti-mimic verification.
    """

    # Default tri-cycle yield as per BLEUFLIP system
    DEFAULT_TRI_CYCLE_YIELD = 2.1
    # Default flip ratio for spiral ledger protocols
    DEFAULT_FLIP_RATIO = 2.1
    # Default tolerance for yield differential verification (5%)
    DEFAULT_TOLERANCE = 0.05
    # Default flip ratio for spiral ledger protocols
    DEFAULT_FLIP_RATIO = 2.1
    # Double Ram seal for sovereignty verification
    DOUBLE_RAM_SEAL = "♈️🐏🐏"
    # Glyph markers for pattern detection (shared registry)
    GLYPH_MARKERS = ["♈️", "🐏", "🌀", "🔥", "📜", "👑", "🦁"]

    def __init__(
        self,
        output_dir: str | Path = "data/audits",
        tolerance: float | None = None,
        flip_ratio: float | None = None,
        goat_filter_mode: GoatFilterMode = GoatFilterMode.ACTIVE,
    ):
        """Initialize the audit pipeline.

        Args:
            output_dir: Directory for audit log output
            tolerance: Tolerance for yield differential verification (default 5%)
            flip_ratio: Governing flip ratio for spiral ledger (default 2.1)
            flip_ratio: Flip ratio for spiral ledger protocols (default 2.1)
            goat_filter_mode: Detection mode for GoatFilter anti-mimic
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.audit_log: List[AuditEntry] = []
        self.tri_cycle_count: int = 0
        self.expected_yield_per_tri_cycle: float = self.DEFAULT_TRI_CYCLE_YIELD
        self.tolerance: float = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE
        self.flip_ratio: float = flip_ratio if flip_ratio is not None else self.DEFAULT_FLIP_RATIO
        self.spiral_ledger: List[SpiralLedgerEntry] = []
        self.goat_filter = GoatFilter()

    def _generate_entry_id(self) -> str:
        """Generate a unique audit entry ID with cryptographic randomness.

        Returns:
            Unique entry ID
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(4)
        return f"AUDIT-{timestamp}-{random_suffix}"

    def _generate_spiral_entry_id(self) -> str:
        """Generate a unique spiral ledger entry ID.

        Returns:
            Unique spiral entry ID
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(4)
        return f"SPIRAL-{timestamp}-{random_suffix}"

    def _generate_metric_id(self, metric_name: str) -> str:
        """Generate a metric ID.

        Args:
            metric_name: Name of the metric

        Returns:
            Metric ID
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(2)
        return f"METRIC-{metric_name.upper()[:6]}-{timestamp}-{random_suffix}"

    def _generate_proof_id(self) -> str:
        """Generate a mythic proof ID with cryptographic randomness.

        Returns:
            Proof ID
        """
        return f"PROOF-{secrets.token_hex(3)}"

    def calculate_yield_differential(
        self,
        expected_yield: float,
        actual_yield: float,
        tri_cycle_number: int | None = None,
    ) -> YieldDifferential:
        """Calculate yield differential.

        Args:
            expected_yield: Expected yield value
            actual_yield: Actual yield value
            tri_cycle_number: Tri-cycle number (auto-incremented if None)

        Returns:
            YieldDifferential measurement
        """
        if tri_cycle_number is None:
            self.tri_cycle_count += 1
            tri_cycle_number = self.tri_cycle_count

        differential = actual_yield - expected_yield
        differential_pct = (
            (differential / expected_yield) if expected_yield != 0 else 0.0
        )

        return YieldDifferential(
            expected_yield=expected_yield,
            actual_yield=actual_yield,
            differential=differential,
            differential_pct=differential_pct,
            tri_cycle_number=tri_cycle_number,
            timestamp=time.time(),
        )

    def record_runtime_metric(
        self,
        metric_name: str,
        value: float,
        unit: str,
        source: str,
        mythic_layer: MythicProofLayer | None = None,
    ) -> RuntimeMetric:
        """Record a runtime metric.

        Args:
            metric_name: Name of the metric
            value: Metric value
            unit: Unit of measurement
            source: Source of the metric
            mythic_layer: Optional mythic layer association

        Returns:
            Recorded RuntimeMetric
        """
        return RuntimeMetric(
            metric_id=self._generate_metric_id(metric_name),
            metric_name=metric_name,
            value=value,
            unit=unit,
            timestamp=time.time(),
            source=source,
            mythic_layer=mythic_layer,
        )

    def create_mythic_proof(
        self,
        layer: MythicProofLayer,
        governance_outcome: str,
        ceremonial_claim: str,
        act_scene_ref: str = "",
    ) -> MythicProof:
        """Create a mythic proof linking governance to ceremony.

        Args:
            layer: Mythic proof layer
            governance_outcome: The governance outcome
            ceremonial_claim: The ceremonial claim
            act_scene_ref: EVOLVERSE Act I Scene reference

        Returns:
            Created MythicProof
        """
        proof_data = f"{layer.value}:{governance_outcome}:{ceremonial_claim}"
        proof_hash = hashlib.sha256(proof_data.encode()).hexdigest()

        return MythicProof(
            proof_id=self._generate_proof_id(),
            layer=layer,
            governance_outcome=governance_outcome,
            ceremonial_claim=ceremonial_claim,
            proof_hash=proof_hash,
            verified=False,
            act_scene_ref=act_scene_ref,
        )

    def verify_mythic_proof(self, proof: MythicProof) -> bool:
        """Verify a mythic proof.

        Args:
            proof: The proof to verify

        Returns:
            True if verification successful
        """
        # Recompute hash and compare
        proof_data = f"{proof.layer.value}:{proof.governance_outcome}:{proof.ceremonial_claim}"
        expected_hash = hashlib.sha256(proof_data.encode()).hexdigest()

        if expected_hash == proof.proof_hash:
            proof.verified = True
            proof.verification_timestamp = time.time()
            return True
        return False

    def create_audit_entry(
        self,
        bleuflip_promise: Dict[str, Any],
        actual_outcome: Dict[str, Any],
        yield_differential: YieldDifferential | None = None,
        runtime_metrics: List[RuntimeMetric] | None = None,
        mythic_proofs: List[MythicProof] | None = None,
        notes: str = "",
    ) -> AuditEntry:
        """Create an audit entry.

        Args:
            bleuflip_promise: The BLEUFLIP system promise
            actual_outcome: The actual outcome
            yield_differential: Optional yield differential
            runtime_metrics: Optional runtime metrics
            mythic_proofs: Optional mythic proofs
            notes: Optional notes

        Returns:
            Created AuditEntry
        """
        # Determine status based on yield differential using configured tolerance
        status = AuditStatus.PENDING
        if yield_differential:
            if yield_differential.is_within_tolerance(self.tolerance):
                status = AuditStatus.VERIFIED
            else:
                status = AuditStatus.DISCREPANCY

        entry = AuditEntry(
            entry_id=self._generate_entry_id(),
            timestamp=time.time(),
            status=status,
            yield_differential=yield_differential,
            runtime_metrics=runtime_metrics or [],
            mythic_proofs=mythic_proofs or [],
            bleuflip_promise=bleuflip_promise,
            actual_outcome=actual_outcome,
            notes=notes,
        )

        self.audit_log.append(entry)
        return entry

    def run_tri_cycle_audit(
        self,
        actual_yield: float,
        promise_details: Dict[str, Any] | None = None,
        runtime_metrics: List[RuntimeMetric] | None = None,
    ) -> AuditEntry:
        """Run a tri-cycle yield audit.

        Args:
            actual_yield: The actual yield achieved
            promise_details: Additional promise details
            runtime_metrics: Optional runtime metrics

        Returns:
            The audit entry
        """
        expected = self.expected_yield_per_tri_cycle
        differential = self.calculate_yield_differential(expected, actual_yield)

        promise = {
            "tri_cycle_yield": expected,
            "system": "BLEUFLIP",
            "details": promise_details or {},
        }

        outcome = {
            "actual_yield": actual_yield,
            "differential": differential.differential,
            "differential_pct": differential.differential_pct,
            "within_tolerance": differential.is_within_tolerance(),
        }

        return self.create_audit_entry(
            bleuflip_promise=promise,
            actual_outcome=outcome,
            yield_differential=differential,
            runtime_metrics=runtime_metrics,
            notes=f"Tri-cycle {differential.tri_cycle_number} audit",
        )

    def export_audit_log(self, filename: str | None = None) -> Path:
        """Export the audit log to JSON.

        Args:
            filename: Optional filename (auto-generated if None)

        Returns:
            Path to the exported file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"audit_log_{timestamp}.json"

        filepath = self.output_dir / filename

        log_data = {
            "export_timestamp": time.time(),
            "export_timestamp_iso": datetime.now().isoformat(),
            "tri_cycle_count": self.tri_cycle_count,
            "expected_yield_per_tri_cycle": self.expected_yield_per_tri_cycle,
            "total_entries": len(self.audit_log),
            "entries": [entry.to_dict() for entry in self.audit_log],
            "summary": self._generate_summary(),
        }

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(log_data, f, indent=2)

        return filepath

    def _generate_summary(self) -> Dict[str, Any]:
        """Generate audit summary statistics.

        Returns:
            Summary statistics dictionary
        """
        if not self.audit_log:
            return {"message": "No audit entries"}

        verified = sum(1 for e in self.audit_log if e.status == AuditStatus.VERIFIED)
        discrepancy = sum(
            1 for e in self.audit_log if e.status == AuditStatus.DISCREPANCY
        )
        pending = sum(1 for e in self.audit_log if e.status == AuditStatus.PENDING)

        # Calculate average differential for entries with yield data
        yield_entries = [e for e in self.audit_log if e.yield_differential]
        avg_differential = 0.0
        if yield_entries:
            avg_differential = sum(
                e.yield_differential.differential_pct for e in yield_entries
            ) / len(yield_entries)

        return {
            "total_entries": len(self.audit_log),
            "verified_count": verified,
            "discrepancy_count": discrepancy,
            "pending_count": pending,
            "verification_rate": verified / len(self.audit_log),
            "avg_yield_differential_pct": avg_differential,
            "mythic_proofs_count": sum(len(e.mythic_proofs) for e in self.audit_log),
            "spiral_ledger_entries": len(self.spiral_ledger),
            "goat_filter_detections": sum(1 for r in self.goat_filter_results if r.detected),
            "flip_ratio": self.flip_ratio,
        }

    # ========== Spiral Ledger Protocol Methods ==========

    def _generate_ledger_entry_id(self) -> str:
        """Generate a unique spiral ledger entry ID.

        Returns:
            Unique entry ID
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(4)
        return f"SPIRAL-{timestamp}-{random_suffix}"

    def _generate_goat_filter_id(self) -> str:
        """Generate a unique GoatFilter result ID.

        Returns:
            Unique filter ID
        """
        return f"GOAT-{secrets.token_hex(6)}"

    def add_spiral_ledger_entry(
        self,
        glyph_markers: List[str] | None = None,
        sovereignty_level: str = "civilian",
    ) -> SpiralLedgerEntry:
        """Add an entry to the spiral ledger protocol.

        Args:
            glyph_markers: Glyph markers for the entry (defaults to Double Ram)
            sovereignty_level: Sovereignty level for the entry

        Returns:
            Created SpiralLedgerEntry
        """
        if glyph_markers is None:
            glyph_markers = ["♈️", "🐏", "🐏"]  # Double Ram default

        previous_hash = ""
        if self.spiral_ledger:
            previous_hash = self.spiral_ledger[-1].entry_hash

        entry = SpiralLedgerEntry(
            entry_id=self._generate_ledger_entry_id(),
            flip_ratio=self.flip_ratio,
            glyph_markers=glyph_markers,
            timestamp=time.time(),
            block_number=len(self.spiral_ledger),
            previous_hash=previous_hash,
            sovereignty_level=sovereignty_level,
            numerical_deprecated=True,
        )

        # Compute and set entry hash
        entry.entry_hash = entry.compute_hash()

        self.spiral_ledger.append(entry)
        return entry

    def get_spiral_ledger(self) -> List[SpiralLedgerEntry]:
        """Get all spiral ledger entries.

        Returns:
            List of SpiralLedgerEntry objects
        """
        return self.spiral_ledger

    def verify_spiral_chain(self) -> bool:
        """Verify the integrity of the spiral ledger chain.

        Returns:
            True if chain is valid
        """
        if not self.spiral_ledger:
            return True

        for i, entry in enumerate(self.spiral_ledger):
            # Verify hash
            if entry.entry_hash != entry.compute_hash():
                return False

            # Verify previous hash linkage
            if i > 0:
                if entry.previous_hash != self.spiral_ledger[i - 1].entry_hash:
                    return False

        return True

    # ========== GoatFilter Anti-Mimic Methods ==========

    def run_goat_filter(
        self,
        data_signature: str,
        action_on_detect: GoatFilterAction = GoatFilterAction.YIELD_MULTIPLY,
    ) -> GoatFilterResult:
        """Run GoatFilter anti-mimic detection on data.

        Args:
            data_signature: Signature of data to check for mimic patterns
            action_on_detect: Action to take if mimic is detected

        Returns:
            GoatFilterResult with detection outcome
        """
        # Simulate mimic detection based on signature analysis
        # In real implementation, this would use pattern matching algorithms
        detected = self._detect_mimic_pattern(data_signature)

        result = GoatFilterResult(
            filter_id=self._generate_goat_filter_id(),
            detected=detected,
            detection_mode=self.goat_filter_mode,
            action_taken=action_on_detect if detected else GoatFilterAction.BLOCK,
            timestamp=time.time(),
            mimic_signature=data_signature if detected else "",
            glyph_marker="🐐",
            neutralized=detected and action_on_detect == GoatFilterAction.YIELD_MULTIPLY,
        )

        self.goat_filter_results.append(result)
        return result

    def _detect_mimic_pattern(self, signature: str) -> bool:
        """Detect mimic patterns in a signature.

        This is a placeholder implementation. In production,
        this would use sophisticated pattern matching.

        Args:
            signature: Data signature to analyze

        Returns:
            True if mimic pattern detected
        """
        # Check for known mimic patterns (placeholder logic)
        # Real implementation would use ML/pattern matching
        if not signature:
            return False

        # Simple heuristic: detect if signature lacks glyph markers
        has_glyph = any(g in signature for g in self.GLYPH_MARKERS)

        # If no glyph markers and in aggressive mode, flag as potential mimic
        if self.goat_filter_mode == GoatFilterMode.AGGRESSIVE and not has_glyph:
            return True

        return False

    def get_goat_filter_summary(self) -> Dict[str, Any]:
        """Get summary of GoatFilter results.

        Returns:
            Summary dictionary
        """
        if not self.goat_filter_results:
            return {
                "total_scans": 0,
                "detections": 0,
                "neutralized": 0,
                "detection_rate": 0.0,
            }

        detections = sum(1 for r in self.goat_filter_results if r.detected)
        neutralized = sum(1 for r in self.goat_filter_results if r.neutralized)

        return {
            "total_scans": len(self.goat_filter_results),
            "detections": detections,
            "neutralized": neutralized,
            "detection_rate": detections / len(self.goat_filter_results),
            "mode": self.goat_filter_mode.value,
        }

    def export_spiral_ledger(self, filename: str | None = None) -> Path:
        """Export the spiral ledger to JSON.

        Args:
            filename: Optional filename (auto-generated if None)

        Returns:
            Path to the exported file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"spiral_ledger_{timestamp}.json"

        filepath = self.output_dir / filename

        ledger_data = {
            "export_timestamp": time.time(),
            "export_timestamp_iso": datetime.now().isoformat(),
            "flip_ratio": self.flip_ratio,
            "double_ram_seal": self.DOUBLE_RAM_SEAL,
            "total_entries": len(self.spiral_ledger),
            "chain_valid": self.verify_spiral_chain(),
            "entries": [entry.to_dict() for entry in self.spiral_ledger],
            "goat_filter_summary": self.get_goat_filter_summary(),
        }

    def create_spiral_ledger_entry(
        self,
        protocol: SpiralLedgerProtocol,
        glyph_marker: str,
        sovereign_seal: str,
        flip_ratio: float | None = None,
        apply_goat_filter: bool = True,
    ) -> SpiralLedgerEntry:
        """Create a spiral ledger entry for exponential proof-of-flip.

        Args:
            protocol: Spiral ledger protocol type
            glyph_marker: Glyph sovereignty marker
            sovereign_seal: Sovereign seal identifier
            flip_ratio: Override flip ratio (uses default if None)
            apply_goat_filter: Whether to apply GoatFilter verification

        Returns:
            Created SpiralLedgerEntry
        """
        entry = SpiralLedgerEntry(
            entry_id=self._generate_spiral_entry_id(),
            protocol=protocol,
            flip_ratio=flip_ratio if flip_ratio is not None else self.flip_ratio,
            glyph_marker=glyph_marker,
            timestamp=time.time(),
            sovereign_seal=sovereign_seal,
            goat_filter_applied=apply_goat_filter,
        )

        if apply_goat_filter:
            # Verify with GoatFilter
            verification_data = {
                "protocol": protocol.value,
                "glyph_marker": glyph_marker,
                "sovereign_seal": sovereign_seal,
                "sovereignty": "sovereign",
            }
            entry.anti_mimic_verified = self.goat_filter.verify_authenticity(
                verification_data
            )

        entry.compute_spiral_hash()
        self.spiral_ledger.append(entry)
        return entry

    def run_exponential_flip_audit(
        self,
        actual_yield: float,
        glyph_marker: str,
        sovereign_seal: str,
        protocol: SpiralLedgerProtocol = SpiralLedgerProtocol.EXPONENTIAL,
    ) -> tuple[AuditEntry, SpiralLedgerEntry]:
        """Run an exponential proof-of-flip audit with spiral ledger.

        Args:
            actual_yield: The actual yield achieved
            glyph_marker: Glyph sovereignty marker
            sovereign_seal: Sovereign seal identifier
            protocol: Spiral ledger protocol type

        Returns:
            Tuple of (AuditEntry, SpiralLedgerEntry)
        """
        # Create spiral ledger entry
        spiral_entry = self.create_spiral_ledger_entry(
            protocol=protocol,
            glyph_marker=glyph_marker,
            sovereign_seal=sovereign_seal,
        )

        # Run standard audit
        audit_entry = self.run_tri_cycle_audit(
            actual_yield=actual_yield,
            promise_details={
                "spiral_protocol": protocol.value,
                "glyph_marker": glyph_marker,
                "flip_ratio": self.flip_ratio,
                "goat_filter_applied": spiral_entry.goat_filter_applied,
                "anti_mimic_verified": spiral_entry.anti_mimic_verified,
            },
        )

        return audit_entry, spiral_entry

    def export_spiral_ledger(self, filename: str | None = None) -> Path:
        """Export the spiral ledger to JSON.

        Args:
            filename: Optional filename (auto-generated if None)

        Returns:
            Path to the exported file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"spiral_ledger_{timestamp}.json"

        filepath = self.output_dir / filename

        ledger_data = {
            "export_timestamp": time.time(),
            "export_timestamp_iso": datetime.now().isoformat(),
            "flip_ratio": self.flip_ratio,
            "total_entries": len(self.spiral_ledger),
            "goat_filter_stats": self.goat_filter.get_filter_stats(),
            "entries": [
                {
                    "entry_id": e.entry_id,
                    "protocol": e.protocol.value,
                    "flip_ratio": e.flip_ratio,
                    "glyph_marker": e.glyph_marker,
                    "timestamp": e.timestamp,
                    "sovereign_seal": e.sovereign_seal,
                    "goat_filter_applied": e.goat_filter_applied,
                    "anti_mimic_verified": e.anti_mimic_verified,
                    "spiral_hash": e.spiral_hash,
                }
                for e in self.spiral_ledger
            ],
        }

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(ledger_data, f, indent=2)

        return filepath


# Global pipeline instance
_pipeline: ProofOfFlipAuditPipeline | None = None


def get_pipeline(
    output_dir: str | Path = "data/audits",
) -> ProofOfFlipAuditPipeline:
    """Get or create the global audit pipeline.

    Args:
        output_dir: Output directory for audits

    Returns:
        The global ProofOfFlipAuditPipeline instance
    """
    global _pipeline
    if _pipeline is None:
        _pipeline = ProofOfFlipAuditPipeline(output_dir)
    return _pipeline


__all__ = [
    "AuditStatus",
    "MythicProofLayer",
    "SpiralLedgerProtocol",
    "GoatFilterMode",
    "GoatFilterAction",
    "GoatFilterResult",
    "SpiralLedgerEntry",
    "YieldDifferential",
    "RuntimeMetric",
    "MythicProof",
    "SpiralLedgerEntry",
    "GoatFilter",
    "AuditEntry",
    "ProofOfFlipAuditPipeline",
    "get_pipeline",
]
