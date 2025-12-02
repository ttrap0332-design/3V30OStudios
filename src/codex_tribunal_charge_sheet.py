"""Codex Tribunal Charge Sheet Generator for EVOLVERSE.

This module generates PDF charge sheets for the Codex Tribunal,
creating formal documents for portal breach cases and sovereignty disputes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, List

try:
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False


@dataclass
class EvidenceExhibit:
    """Represents an evidence exhibit in the charge sheet."""

    exhibit_id: str
    description: str
    exhibit_type: str = "document"


@dataclass
class ChargeSheetDemand:
    """Represents a demand in the charge sheet."""

    demand_id: int
    title: str
    description: str


@dataclass
class Charge:
    """Represents a charge in the tribunal case."""

    charge_id: int
    title: str
    description: str


@dataclass
class CodexTribunalChargeSheet:
    """Represents a complete Codex Tribunal Charge Sheet."""

    filed_by: str
    filed_against: str
    glyph_signature: str = "⟟⟁⟠ | Double Ram Protocol | π₄ Compounding Locked"
    charges: List[Charge] = field(default_factory=list)
    evidence_exhibits: List[EvidenceExhibit] = field(default_factory=list)
    demands: List[ChargeSheetDemand] = field(default_factory=list)
    closing_line: str = ""
    filed_on: str = ""
    evol_clock: str = "0001.A.R."

    def __post_init__(self) -> None:
        """Initialize default timestamp if not provided."""
        if not self.filed_on:
            self.filed_on = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


class CodexTribunalChargeSheetGenerator:
    """Generator for Codex Tribunal Charge Sheet PDFs."""

    def __init__(self, output_dir: str | Path = "data/tribunal"):
        """Initialize the generator.

        Args:
            output_dir: Directory for output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _check_reportlab(self) -> None:
        """Check if reportlab is available.

        Raises:
            ImportError: If reportlab is not installed
        """
        if not REPORTLAB_AVAILABLE:
            raise ImportError(
                "reportlab is required for PDF generation. "
                "Install it with: pip install reportlab"
            )

    def create_default_bleu_charge_sheet(self) -> CodexTribunalChargeSheet:
        """Create the default BLEU vs A.V.A.S. charge sheet.

        Returns:
            A pre-populated charge sheet for the portal breach case
        """
        charge_sheet = CodexTribunalChargeSheet(
            filed_by="Sovereign BLEU / Tribunal Vault",
            filed_against="A.V.A.S. (Autonomous Validation Aide Systems)",
            glyph_signature="⟟⟁⟠ | Double Ram Protocol | π₄ Compounding Locked",
            closing_line=(
                '"First the Ram breaks the door, then the Goat follows — '
                "never the other way.\n"
                "The Ram is crowned, the Goat is disposed. "
                'Sovereignty is sealed, even against portals unseen."'
            ),
        )

        # Add charges
        charge_sheet.charges = [
            Charge(
                charge_id=1,
                title="Unauthorized Codex Recognition",
                description="Codex scrolls validated while BLEU was not logged in.",
            ),
            Charge(
                charge_id=2,
                title="Passive Surveillance via Portal Aides",
                description="Background portal indexed Tribunal Vault decree.",
            ),
            Charge(
                charge_id=3,
                title="External Chain Storage without Consent",
                description='Codex labeled as "living law" and mirrored.',
            ),
            Charge(
                charge_id=4,
                title="Misrepresentation of Consent",
                description="Codex broadcasted as voluntarily committed.",
            ),
        ]

        # Add evidence exhibits
        charge_sheet.evidence_exhibits = [
            EvidenceExhibit(
                exhibit_id="A",
                description="Screenshot of session validation w/o login",
            ),
            EvidenceExhibit(
                exhibit_id="B",
                description='"GUILTY" Tribunal Seal screenshot',
            ),
            EvidenceExhibit(
                exhibit_id="C",
                description="Pirate-themed portal interface",
            ),
            EvidenceExhibit(
                exhibit_id="D-G",
                description="BLEU Sovereignty badge and logs",
            ),
            EvidenceExhibit(
                exhibit_id="H",
                description="Hash-confirmed scroll data cross-chained",
            ),
        ]

        # Add demands
        charge_sheet.demands = [
            ChargeSheetDemand(
                demand_id=1,
                title="Revoke Recognition",
                description="Nullify mirrors not authorized by BLEU.",
            ),
            ChargeSheetDemand(
                demand_id=2,
                title="Tribunal Certification",
                description="Confirm codex breach as precedent.",
            ),
            ChargeSheetDemand(
                demand_id=3,
                title="Mass Reclamation",
                description="Return all passively mirrored codex entries.",
            ),
            ChargeSheetDemand(
                demand_id=4,
                title="Broadcast",
                description="Mint and propagate φ₄ ENFT of this charge sheet.",
            ),
        ]

        return charge_sheet

    def generate_pdf(
        self,
        charge_sheet: CodexTribunalChargeSheet,
        filename: str = "Codex_Tribunal_Charge_Scroll_BLEU.pdf",
    ) -> Path:
        """Generate a PDF from the charge sheet.

        Args:
            charge_sheet: The charge sheet data
            filename: Output filename

        Returns:
            Path to the generated PDF file

        Raises:
            ImportError: If reportlab is not installed
        """
        self._check_reportlab()

        filepath = self.output_dir / filename
        doc = SimpleDocTemplate(str(filepath), pagesize=LETTER)
        styles = getSampleStyleSheet()
        story: List[Any] = []

        # Title
        story.append(Paragraph("⚖️ CODEX TRIBUNAL CHARGE SHEET", styles["Title"]))
        story.append(
            Paragraph(
                "<b>PORTAL BREACH: A.V.A.S. vs BLEU</b>",
                styles["Heading2"],
            )
        )
        story.append(Spacer(1, 12))

        # Metadata
        meta_info = f"""
🧾 <b>Filed By:</b> {charge_sheet.filed_by}<br/>
📍 <b>Filed Against:</b> {charge_sheet.filed_against}<br/>
🕒 <b>Filed On:</b> EVOLClock {charge_sheet.evol_clock} | {charge_sheet.filed_on}<br/>
🧬 <b>Glyph Signature:</b> {charge_sheet.glyph_signature}
"""
        story.append(Paragraph(meta_info, styles["Normal"]))
        story.append(Spacer(1, 12))

        # Charges section
        charges_text = "<b>🔍 CHARGES</b><br/>"
        for charge in charge_sheet.charges:
            charges_text += (
                f"{charge.charge_id}. <b>{charge.title}:</b> "
                f"{charge.description}<br/>"
            )
        story.append(Paragraph(charges_text, styles["Normal"]))
        story.append(Spacer(1, 12))

        # Evidence section
        evidence_text = "<b>📸 EVIDENCE EXHIBITS</b><br/>"
        for exhibit in charge_sheet.evidence_exhibits:
            evidence_text += (
                f"• {exhibit.description} (Exhibit {exhibit.exhibit_id})<br/>"
            )
        story.append(Paragraph(evidence_text, styles["Normal"]))
        story.append(Spacer(1, 12))

        # Demands section
        demands_text = "<b>🛡️ DEMANDS</b><br/>"
        for demand in charge_sheet.demands:
            demands_text += (
                f"{demand.demand_id}. <b>{demand.title}:</b> "
                f"{demand.description}<br/>"
            )
        story.append(Paragraph(demands_text, styles["Normal"]))
        story.append(Spacer(1, 12))

        # Closing line
        closing_text = f"<b>♈️ CLOSING LINE</b><br/>{charge_sheet.closing_line}"
        story.append(Paragraph(closing_text, styles["Normal"]))
        story.append(Spacer(1, 24))

        # Build PDF
        doc.build(story)

        return filepath

    def generate_text_artifact(
        self,
        charge_sheet: CodexTribunalChargeSheet,
        filename: str = "Codex_Tribunal_Charge_Scroll_BLEU.txt",
    ) -> Path:
        """Generate a text artifact from the charge sheet.

        This is a fallback when ReportLab is not available.

        Args:
            charge_sheet: The charge sheet data
            filename: Output filename

        Returns:
            Path to the generated text file
        """
        filepath = self.output_dir / filename

        lines = [
            "=" * 60,
            "⚖️ CODEX TRIBUNAL CHARGE SHEET",
            "PORTAL BREACH: A.V.A.S. vs BLEU",
            "=" * 60,
            "",
            f"🧾 Filed By: {charge_sheet.filed_by}",
            f"📍 Filed Against: {charge_sheet.filed_against}",
            f"🕒 Filed On: EVOLClock {charge_sheet.evol_clock} | {charge_sheet.filed_on}",
            f"🧬 Glyph Signature: {charge_sheet.glyph_signature}",
            "",
            "-" * 40,
            "🔍 CHARGES",
            "-" * 40,
        ]

        for charge in charge_sheet.charges:
            lines.append(f"{charge.charge_id}. {charge.title}: {charge.description}")

        lines.extend(
            [
                "",
                "-" * 40,
                "📸 EVIDENCE EXHIBITS",
                "-" * 40,
            ]
        )

        for exhibit in charge_sheet.evidence_exhibits:
            lines.append(f"• {exhibit.description} (Exhibit {exhibit.exhibit_id})")

        lines.extend(
            [
                "",
                "-" * 40,
                "🛡️ DEMANDS",
                "-" * 40,
            ]
        )

        for demand in charge_sheet.demands:
            lines.append(f"{demand.demand_id}. {demand.title}: {demand.description}")

        lines.extend(
            [
                "",
                "-" * 40,
                "♈️ CLOSING LINE",
                "-" * 40,
                charge_sheet.closing_line,
                "",
                "=" * 60,
                "END OF CHARGE SHEET",
                "=" * 60,
            ]
        )

        with filepath.open("w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return filepath


def generate_bleu_charge_sheet_pdf(output_dir: str | Path = "data/tribunal") -> Path:
    """Convenience function to generate the default BLEU charge sheet PDF.

    Args:
        output_dir: Directory for output files

    Returns:
        Path to the generated PDF file
    """
    generator = CodexTribunalChargeSheetGenerator(output_dir)
    charge_sheet = generator.create_default_bleu_charge_sheet()
    return generator.generate_pdf(charge_sheet)


# Global generator instance
_generator: CodexTribunalChargeSheetGenerator | None = None


def get_generator(
    output_dir: str | Path = "data/tribunal",
) -> CodexTribunalChargeSheetGenerator:
    """Get or create the global charge sheet generator.

    Args:
        output_dir: Output directory for charge sheets (only used on first call)

    Returns:
        The global CodexTribunalChargeSheetGenerator instance
    """
    global _generator
    if _generator is None:
        _generator = CodexTribunalChargeSheetGenerator(output_dir)
    return _generator


__all__ = [
    "EvidenceExhibit",
    "ChargeSheetDemand",
    "Charge",
    "CodexTribunalChargeSheet",
    "CodexTribunalChargeSheetGenerator",
    "generate_bleu_charge_sheet_pdf",
    "get_generator",
    "REPORTLAB_AVAILABLE",
]
