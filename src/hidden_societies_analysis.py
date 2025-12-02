#!/usr/bin/env python3
"""Hidden Societies Analysis and Visualization Module.

This module provides comprehensive analysis and visualization of hidden societies
and their attributes using pandas for structured data analysis and matplotlib/seaborn
for visual representation.

Features:
- Definitions for key societies with symbols, statuses, and access levels
- Integration with pandas for structured data analysis
- Visual representation with matplotlib and seaborn
- Styled tabular output for better understanding
"""
from __future__ import annotations

import os
import tempfile
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    VISUALIZATION_AVAILABLE = True
except ImportError:
    VISUALIZATION_AVAILABLE = False
    pd = None
    plt = None
    sns = None


class SocietyStatus(Enum):
    """Status categories for hidden societies."""

    PREVIOUSLY_CONTACTED = "Previously Contacted"
    ACTIVE = "Active"
    DORMANT = "Dormant"
    GUARDED = "Guarded"
    CORE_ACTIVE = "Core Active"
    ANCESTRAL = "Ancestral"


class AccessLevel(Enum):
    """Access level tiers for society infrastructure."""

    ROOT = "Root"
    ANCESTRAL = "Ancestral"
    HIGH = "High"
    STANDARD = "Standard"
    RESTRICTED = "Restricted"
    CLASSIFIED = "Classified"


@dataclass
class Society:
    """Represents a hidden society with its attributes."""

    name: str
    symbol: str
    status: SocietyStatus
    access_level: AccessLevel
    description: Optional[str] = None
    infrastructure_tier: int = 1

    def to_dict(self) -> Dict[str, Any]:
        """Convert society to dictionary representation."""
        return {
            "name": self.name,
            "symbol": self.symbol,
            "status": self.status.value,
            "access_level": self.access_level.value,
            "description": self.description or "",
            "infrastructure_tier": self.infrastructure_tier,
        }


# Default society definitions
DEFAULT_SOCIETIES: List[Society] = [
    Society(
        name="E-SOIL Core",
        symbol="🌱",
        status=SocietyStatus.CORE_ACTIVE,
        access_level=AccessLevel.ROOT,
        description="Core Active E-SOIL layer foundation",
        infrastructure_tier=5,
    ),
    Society(
        name="Atlantis Archive",
        symbol="🌊",
        status=SocietyStatus.ANCESTRAL,
        access_level=AccessLevel.ANCESTRAL,
        description="Root/Ancestral alignment archive",
        infrastructure_tier=5,
    ),
    Society(
        name="Mirror Market Council",
        symbol="🪞",
        status=SocietyStatus.ACTIVE,
        access_level=AccessLevel.HIGH,
        description="Active trading and barter coordination",
        infrastructure_tier=4,
    ),
    Society(
        name="Spiral Law Guardians",
        symbol="🌀",
        status=SocietyStatus.GUARDED,
        access_level=AccessLevel.CLASSIFIED,
        description="Guarded sovereign law protectors",
        infrastructure_tier=4,
    ),
    Society(
        name="Bleu Symbol Keepers",
        symbol="💎",
        status=SocietyStatus.ACTIVE,
        access_level=AccessLevel.HIGH,
        description="Symbol licensing and cultural preservation",
        infrastructure_tier=3,
    ),
    Society(
        name="Quantum Refuel Alliance",
        symbol="⚛️",
        status=SocietyStatus.PREVIOUSLY_CONTACTED,
        access_level=AccessLevel.STANDARD,
        description="Light and plasma fueling coordination",
        infrastructure_tier=3,
    ),
    Society(
        name="HydroCoin Collective",
        symbol="💧",
        status=SocietyStatus.ACTIVE,
        access_level=AccessLevel.STANDARD,
        description="Universal currency acceptance network",
        infrastructure_tier=3,
    ),
    Society(
        name="Saturnian Signal Corps",
        symbol="🪐",
        status=SocietyStatus.DORMANT,
        access_level=AccessLevel.RESTRICTED,
        description="Long-range coordination protocols",
        infrastructure_tier=2,
    ),
    Society(
        name="Glyph Access Panel",
        symbol="🔐",
        status=SocietyStatus.GUARDED,
        access_level=AccessLevel.CLASSIFIED,
        description="Off-planet intelligence unlock system",
        infrastructure_tier=2,
    ),
    Society(
        name="ENFT Registry",
        symbol="📜",
        status=SocietyStatus.ACTIVE,
        access_level=AccessLevel.STANDARD,
        description="Digital asset and knowledge tracking",
        infrastructure_tier=3,
    ),
]


class HiddenSocietiesAnalyzer:
    """Analyzer for hidden societies data with visualization capabilities."""

    def __init__(self, societies: Optional[List[Society]] = None):
        """Initialize the analyzer with society data.

        Args:
            societies: List of Society objects to analyze.
                      Uses DEFAULT_SOCIETIES if not provided.
        """
        self.societies = societies if societies is not None else DEFAULT_SOCIETIES
        self._dataframe: Optional[Any] = None

    @property
    def dataframe(self) -> Any:
        """Get pandas DataFrame of societies data.

        Returns:
            pandas DataFrame with society information.

        Raises:
            ImportError: If pandas is not installed.
        """
        if not VISUALIZATION_AVAILABLE:
            raise ImportError(
                "pandas is required for DataFrame functionality. "
                "Install with: pip install pandas"
            )

        if self._dataframe is None:
            data = [society.to_dict() for society in self.societies]
            self._dataframe = pd.DataFrame(data)

        return self._dataframe

    def get_societies_table(self) -> List[Dict[str, Any]]:
        """Get societies data as a list of dictionaries.

        Returns:
            List of society dictionaries.
        """
        return [society.to_dict() for society in self.societies]

    def get_status_summary(self) -> Dict[str, int]:
        """Get count of societies by status.

        Returns:
            Dictionary mapping status values to counts.
        """
        status_counts: Dict[str, int] = {}
        for society in self.societies:
            status = society.status.value
            status_counts[status] = status_counts.get(status, 0) + 1
        return status_counts

    def get_access_level_summary(self) -> Dict[str, int]:
        """Get count of societies by access level.

        Returns:
            Dictionary mapping access level values to counts.
        """
        access_counts: Dict[str, int] = {}
        for society in self.societies:
            level = society.access_level.value
            access_counts[level] = access_counts.get(level, 0) + 1
        return access_counts

    def get_infrastructure_summary(self) -> Dict[int, List[str]]:
        """Get societies grouped by infrastructure tier.

        Returns:
            Dictionary mapping tier numbers to lists of society names.
        """
        tier_groups: Dict[int, List[str]] = {}
        for society in self.societies:
            tier = society.infrastructure_tier
            if tier not in tier_groups:
                tier_groups[tier] = []
            tier_groups[tier].append(society.name)
        return tier_groups

    def filter_by_status(self, status: SocietyStatus) -> List[Society]:
        """Filter societies by status.

        Args:
            status: Status to filter by.

        Returns:
            List of societies matching the status.
        """
        return [s for s in self.societies if s.status == status]

    def filter_by_access_level(self, level: AccessLevel) -> List[Society]:
        """Filter societies by access level.

        Args:
            level: Access level to filter by.

        Returns:
            List of societies matching the access level.
        """
        return [s for s in self.societies if s.access_level == level]

    def to_json(self) -> str:
        """Export societies data to JSON string.

        Returns:
            JSON string representation of societies data.
        """
        import json

        return json.dumps(self.get_societies_table(), indent=2)


class HiddenSocietiesVisualizer:
    """Visualizer for hidden societies data using matplotlib and seaborn."""

    # Color palette for different statuses
    STATUS_COLORS = {
        "Previously Contacted": "#9b59b6",
        "Active": "#2ecc71",
        "Dormant": "#95a5a6",
        "Guarded": "#e74c3c",
        "Core Active": "#3498db",
        "Ancestral": "#f39c12",
    }

    # Color palette for access levels
    ACCESS_COLORS = {
        "Root": "#1a1a2e",
        "Ancestral": "#16213e",
        "High": "#0f3460",
        "Standard": "#533483",
        "Restricted": "#e94560",
        "Classified": "#0f0f0f",
    }

    def __init__(self, analyzer: HiddenSocietiesAnalyzer):
        """Initialize visualizer with an analyzer.

        Args:
            analyzer: HiddenSocietiesAnalyzer instance.
        """
        self.analyzer = analyzer
        self._check_dependencies()

    def _check_dependencies(self) -> None:
        """Check if visualization dependencies are available."""
        if not VISUALIZATION_AVAILABLE:
            raise ImportError(
                "matplotlib and seaborn are required for visualization. "
                "Install with: pip install matplotlib seaborn pandas"
            )

    def plot_status_distribution(
        self,
        figsize: tuple = (10, 6),
        save_path: Optional[str] = None,
    ) -> Any:
        """Create a bar chart showing distribution of society statuses.

        Args:
            figsize: Figure size as (width, height) tuple.
            save_path: Optional path to save the figure.

        Returns:
            matplotlib Figure object.
        """
        status_counts = self.analyzer.get_status_summary()

        fig, ax = plt.subplots(figsize=figsize)

        statuses = list(status_counts.keys())
        counts = list(status_counts.values())
        colors = [self.STATUS_COLORS.get(s, "#7f8c8d") for s in statuses]

        bars = ax.bar(statuses, counts, color=colors, edgecolor="white", linewidth=1.5)

        ax.set_xlabel("Status", fontsize=12, fontweight="bold")
        ax.set_ylabel("Number of Societies", fontsize=12, fontweight="bold")
        ax.set_title(
            "Hidden Societies Distribution by Status",
            fontsize=14,
            fontweight="bold",
            pad=20,
        )

        # Add value labels on bars
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax.annotate(
                f"{count}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=11,
            )

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        if save_path:
            fig.savefig(save_path, dpi=150, bbox_inches="tight")

        return fig

    def plot_access_level_distribution(
        self,
        figsize: tuple = (10, 6),
        save_path: Optional[str] = None,
    ) -> Any:
        """Create a bar chart showing distribution of access levels.

        Args:
            figsize: Figure size as (width, height) tuple.
            save_path: Optional path to save the figure.

        Returns:
            matplotlib Figure object.
        """
        access_counts = self.analyzer.get_access_level_summary()

        fig, ax = plt.subplots(figsize=figsize)

        levels = list(access_counts.keys())
        counts = list(access_counts.values())
        colors = [self.ACCESS_COLORS.get(level, "#7f8c8d") for level in levels]

        bars = ax.bar(levels, counts, color=colors, edgecolor="white", linewidth=1.5)

        ax.set_xlabel("Access Level", fontsize=12, fontweight="bold")
        ax.set_ylabel("Number of Societies", fontsize=12, fontweight="bold")
        ax.set_title(
            "Hidden Societies by Access Level",
            fontsize=14,
            fontweight="bold",
            pad=20,
        )

        # Add value labels on bars
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax.annotate(
                f"{count}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=11,
                fontweight="bold",
            )

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        if save_path:
            fig.savefig(save_path, dpi=150, bbox_inches="tight")

        return fig

    def plot_infrastructure_heatmap(
        self,
        figsize: tuple = (12, 8),
        save_path: Optional[str] = None,
    ) -> Any:
        """Create a heatmap showing infrastructure tiers vs status.

        Args:
            figsize: Figure size as (width, height) tuple.
            save_path: Optional path to save the figure.

        Returns:
            matplotlib Figure object.
        """
        df = self.analyzer.dataframe

        # Create pivot table for heatmap
        pivot_data = df.pivot_table(
            index="infrastructure_tier",
            columns="status",
            aggfunc="size",
            fill_value=0,
        )

        fig, ax = plt.subplots(figsize=figsize)

        sns.heatmap(
            pivot_data,
            annot=True,
            fmt="d",
            cmap="YlGnBu",
            ax=ax,
            linewidths=0.5,
            cbar_kws={"label": "Number of Societies"},
        )

        ax.set_xlabel("Status", fontsize=12, fontweight="bold")
        ax.set_ylabel("Infrastructure Tier", fontsize=12, fontweight="bold")
        ax.set_title(
            "Infrastructure Tier vs Status Matrix",
            fontsize=14,
            fontweight="bold",
            pad=20,
        )

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        if save_path:
            fig.savefig(save_path, dpi=150, bbox_inches="tight")

        return fig

    def plot_combined_dashboard(
        self,
        figsize: tuple = (16, 12),
        save_path: Optional[str] = None,
    ) -> Any:
        """Create a combined dashboard with multiple visualizations.

        Args:
            figsize: Figure size as (width, height) tuple.
            save_path: Optional path to save the figure.

        Returns:
            matplotlib Figure object.
        """
        fig = plt.figure(figsize=figsize)

        # Status distribution (top left)
        ax1 = fig.add_subplot(2, 2, 1)
        status_counts = self.analyzer.get_status_summary()
        statuses = list(status_counts.keys())
        counts = list(status_counts.values())
        colors = [self.STATUS_COLORS.get(s, "#7f8c8d") for s in statuses]

        bars = ax1.bar(statuses, counts, color=colors, edgecolor="white")
        ax1.set_title("Status Distribution", fontsize=12, fontweight="bold")
        ax1.set_ylabel("Count")
        plt.sca(ax1)
        plt.xticks(rotation=45, ha="right", fontsize=9)

        # Access level distribution (top right)
        ax2 = fig.add_subplot(2, 2, 2)
        access_counts = self.analyzer.get_access_level_summary()
        levels = list(access_counts.keys())
        access_values = list(access_counts.values())
        ax2.pie(
            access_values,
            labels=levels,
            autopct="%1.1f%%",
            colors=[self.ACCESS_COLORS.get(l, "#7f8c8d") for l in levels],
            textprops={"fontsize": 9},
        )
        ax2.set_title("Access Level Distribution", fontsize=12, fontweight="bold")

        # Infrastructure tier breakdown (bottom left)
        ax3 = fig.add_subplot(2, 2, 3)
        df = self.analyzer.dataframe
        tier_counts = df["infrastructure_tier"].value_counts().sort_index()
        ax3.barh(
            [f"Tier {t}" for t in tier_counts.index],
            tier_counts.values,
            color=sns.color_palette("viridis", len(tier_counts)),
        )
        ax3.set_title("Infrastructure Tier Breakdown", fontsize=12, fontweight="bold")
        ax3.set_xlabel("Number of Societies")

        # Society overview table (bottom right)
        ax4 = fig.add_subplot(2, 2, 4)
        ax4.axis("off")

        table_data = [
            ["Total Societies", len(self.analyzer.societies)],
            ["Active Societies", len(self.analyzer.filter_by_status(SocietyStatus.ACTIVE))],
            ["Core Active", len(self.analyzer.filter_by_status(SocietyStatus.CORE_ACTIVE))],
            ["Highest Tier", max(s.infrastructure_tier for s in self.analyzer.societies)],
            ["Root Access", len(self.analyzer.filter_by_access_level(AccessLevel.ROOT))],
        ]

        table = ax4.table(
            cellText=table_data,
            colLabels=["Metric", "Value"],
            loc="center",
            cellLoc="center",
            colColours=["#3498db", "#3498db"],
        )
        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1.2, 1.8)
        ax4.set_title("Summary Statistics", fontsize=12, fontweight="bold", pad=20)

        plt.suptitle(
            "Hidden Societies Analysis Dashboard",
            fontsize=16,
            fontweight="bold",
            y=0.98,
        )
        plt.tight_layout(rect=[0, 0, 1, 0.96])

        if save_path:
            fig.savefig(save_path, dpi=150, bbox_inches="tight")

        return fig


def display_styled_table(analyzer: HiddenSocietiesAnalyzer) -> None:
    """Display a styled table of societies in the console.

    Args:
        analyzer: HiddenSocietiesAnalyzer instance.
    """
    print("\n" + "=" * 90)
    print("HIDDEN SOCIETIES ANALYSIS")
    print("=" * 90)

    # Header
    header = f"{'Name':<25} {'Symbol':<8} {'Status':<22} {'Access Level':<15} {'Tier':<5}"
    print(header)
    print("-" * 90)

    # Data rows
    for society in analyzer.societies:
        row = (
            f"{society.name:<25} "
            f"{society.symbol:<8} "
            f"{society.status.value:<22} "
            f"{society.access_level.value:<15} "
            f"{society.infrastructure_tier:<5}"
        )
        print(row)

    print("-" * 90)

    # Summary
    print(f"\nTotal Societies: {len(analyzer.societies)}")
    print("\nStatus Summary:")
    for status, count in analyzer.get_status_summary().items():
        print(f"  • {status}: {count}")

    print("\nAccess Level Summary:")
    for level, count in analyzer.get_access_level_summary().items():
        print(f"  • {level}: {count}")

    print("\nInfrastructure Tiers:")
    for tier, societies in sorted(analyzer.get_infrastructure_summary().items(), reverse=True):
        print(f"  Tier {tier}: {', '.join(societies)}")

    print("=" * 90 + "\n")


def main() -> None:
    """Main function to demonstrate the hidden societies analysis."""
    # Initialize analyzer with default societies
    analyzer = HiddenSocietiesAnalyzer()

    # Display styled table
    display_styled_table(analyzer)

    # Check if visualization is available
    if VISUALIZATION_AVAILABLE:
        print("Visualization libraries available. Creating charts...")

        visualizer = HiddenSocietiesVisualizer(analyzer)

        # Use cross-platform temp directory
        output_dir = tempfile.gettempdir()

        # Create and display charts
        status_path = os.path.join(output_dir, "status_distribution.png")
        visualizer.plot_status_distribution(save_path=status_path)
        print(f"  ✓ Status distribution chart saved to {status_path}")

        access_path = os.path.join(output_dir, "access_levels.png")
        visualizer.plot_access_level_distribution(save_path=access_path)
        print(f"  ✓ Access level chart saved to {access_path}")

        heatmap_path = os.path.join(output_dir, "infrastructure_heatmap.png")
        visualizer.plot_infrastructure_heatmap(save_path=heatmap_path)
        print(f"  ✓ Infrastructure heatmap saved to {heatmap_path}")

        dashboard_path = os.path.join(output_dir, "combined_dashboard.png")
        visualizer.plot_combined_dashboard(save_path=dashboard_path)
        print(f"  ✓ Combined dashboard saved to {dashboard_path}")

        print("\nAll visualizations generated successfully!")
    else:
        print("\nNote: Install pandas, matplotlib, and seaborn for visualizations:")
        print("  pip install pandas matplotlib seaborn")

    # Export to JSON
    json_output = analyzer.to_json()
    print("\nJSON Export Preview:")
    print(json_output[:500] + "..." if len(json_output) > 500 else json_output)


if __name__ == "__main__":
    main()


__all__ = [
    "SocietyStatus",
    "AccessLevel",
    "Society",
    "HiddenSocietiesAnalyzer",
    "HiddenSocietiesVisualizer",
    "display_styled_table",
    "DEFAULT_SOCIETIES",
]
