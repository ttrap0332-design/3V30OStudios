"""Afro-Sovereign Identity Map Framework for EVOLVERSE.

This module provides data analysis and visualization capabilities for the
Global Afro-Sovereign Identity Map dataset. It integrates with the EV0LVerse
educational module to enable sorting, filtering, and visualization of
Afro-descendant community data across the globe.

Features:
- Pandas DataFrame operations for data analysis
- Bar charts and heat maps for visualization
- Geographic and historical extrapolations
- Blockchain integration readiness metrics
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class AfroIdentityDataLoader:
    """Loads and parses the Afro-Sovereign Identity Map dataset."""

    data_path: Path = field(
        default_factory=lambda: Path(__file__).parent.parent
        / "data"
        / "afro_sovereign_identity_map.json"
    )
    _raw_data: dict = field(default_factory=dict, repr=False)

    def load(self) -> dict:
        """Load the identity map data from JSON file.

        Returns:
            Dictionary containing the full dataset
        """
        with open(self.data_path, encoding="utf-8") as f:
            self._raw_data = json.load(f)
        return self._raw_data

    @property
    def regions(self) -> list[dict]:
        """Get all regions from the dataset."""
        if not self._raw_data:
            self.load()
        return self._raw_data.get("regions", [])

    @property
    def glyphs(self) -> list[dict]:
        """Get all symbolic glyphs from the dataset."""
        if not self._raw_data:
            self.load()
        return self._raw_data.get("symbolic_glyphs", [])

    @property
    def educational_modules(self) -> list[dict]:
        """Get all educational modules from the dataset."""
        if not self._raw_data:
            self.load()
        return self._raw_data.get("educational_modules", [])

    @property
    def historical_anchors(self) -> list[dict]:
        """Get all historical anchors from the dataset."""
        if not self._raw_data:
            self.load()
        return self._raw_data.get("historical_anchors", [])


class AfroIdentityFramework:
    """Framework for analyzing Afro-descendant community data.

    Provides DataFrame operations for sorting, filtering, and visualization
    of the Global Afro-Sovereign Identity Map dataset.
    """

    def __init__(self, data_loader: AfroIdentityDataLoader | None = None):
        """Initialize the framework.

        Args:
            data_loader: Optional data loader instance. If None, creates default.
        """
        self.loader = data_loader or AfroIdentityDataLoader()
        self._communities_df: Any = None
        self._regions_df: Any = None

    def _get_pandas(self) -> Any:
        """Lazy import pandas to avoid import errors if not installed."""
        try:
            import pandas as pd

            return pd
        except ImportError as e:
            msg = "pandas is required for DataFrame operations. Install with: pip install pandas"
            raise ImportError(msg) from e

    def build_communities_dataframe(self) -> Any:
        """Build a pandas DataFrame of all communities.

        Returns:
            DataFrame with community data including metrics
        """
        pd = self._get_pandas()

        communities_list = []
        for region in self.loader.regions:
            region_name = region.get("name", "Unknown")
            region_id = region.get("id", "")
            emoji = region.get("emoji", "")
            coords = region.get("geographic_coordinates", {})

            for community in region.get("communities", []):
                community_data = {
                    "region_id": region_id,
                    "region_name": region_name,
                    "region_emoji": emoji,
                    "region_latitude": coords.get("latitude"),
                    "region_longitude": coords.get("longitude"),
                    "community_id": community.get("id", ""),
                    "community_name": community.get("name", ""),
                    "population_estimate": community.get("population_estimate", 0),
                    "historical_significance": community.get(
                        "historical_significance", ""
                    ),
                    "modern_relevance_score": community.get(
                        "modern_relevance_score", 0.0
                    ),
                    "tourism_potential": community.get("economic_indicators", {}).get(
                        "tourism_potential", 0.0
                    ),
                    "cultural_preservation_index": community.get(
                        "economic_indicators", {}
                    ).get("cultural_preservation_index", 0.0),
                    "blockchain_readiness": community.get(
                        "economic_indicators", {}
                    ).get("blockchain_integration_readiness", 0.0),
                    "enft_template": community.get("enft_template", ""),
                    "cultural_practices": ", ".join(
                        community.get("cultural_practices", [])
                    ),
                    "symbolic_elements": ", ".join(
                        community.get("symbolic_elements", [])
                    ),
                }
                communities_list.append(community_data)

        self._communities_df = pd.DataFrame(communities_list)
        return self._communities_df

    def build_regions_dataframe(self) -> Any:
        """Build a pandas DataFrame of regions with aggregated metrics.

        Returns:
            DataFrame with region-level aggregated data
        """
        pd = self._get_pandas()

        if self._communities_df is None:
            self.build_communities_dataframe()

        regions_agg = (
            self._communities_df.groupby(["region_id", "region_name", "region_emoji"])
            .agg(
                {
                    "population_estimate": "sum",
                    "modern_relevance_score": "mean",
                    "tourism_potential": "mean",
                    "cultural_preservation_index": "mean",
                    "blockchain_readiness": "mean",
                    "community_id": "count",
                }
            )
            .reset_index()
        )
        regions_agg = regions_agg.rename(columns={"community_id": "community_count"})
        self._regions_df = regions_agg
        return self._regions_df

    def filter_by_relevance(self, min_score: float = 0.9) -> Any:
        """Filter communities by modern relevance score.

        Args:
            min_score: Minimum relevance score threshold

        Returns:
            Filtered DataFrame
        """
        if self._communities_df is None:
            self.build_communities_dataframe()
        return self._communities_df[
            self._communities_df["modern_relevance_score"] >= min_score
        ]

    def filter_by_blockchain_readiness(self, min_readiness: float = 0.7) -> Any:
        """Filter communities by blockchain integration readiness.

        Args:
            min_readiness: Minimum blockchain readiness threshold

        Returns:
            Filtered DataFrame
        """
        if self._communities_df is None:
            self.build_communities_dataframe()
        return self._communities_df[
            self._communities_df["blockchain_readiness"] >= min_readiness
        ]

    def filter_by_region(self, region_name: str) -> Any:
        """Filter communities by region name.

        Args:
            region_name: Name of region to filter by

        Returns:
            Filtered DataFrame
        """
        if self._communities_df is None:
            self.build_communities_dataframe()
        return self._communities_df[
            self._communities_df["region_name"].str.contains(region_name, case=False)
        ]

    def sort_by_population(self, ascending: bool = False) -> Any:
        """Sort communities by population estimate.

        Args:
            ascending: Sort order (default: descending)

        Returns:
            Sorted DataFrame
        """
        if self._communities_df is None:
            self.build_communities_dataframe()
        return self._communities_df.sort_values(
            "population_estimate", ascending=ascending
        )

    def get_top_communities(self, metric: str, n: int = 10) -> Any:
        """Get top N communities by specified metric.

        Args:
            metric: Column name to rank by
            n: Number of top results to return

        Returns:
            Top N communities DataFrame
        """
        if self._communities_df is None:
            self.build_communities_dataframe()
        return self._communities_df.nlargest(n, metric)

    def get_summary_statistics(self) -> dict:
        """Get summary statistics for the dataset.

        Returns:
            Dictionary with summary statistics
        """
        if self._communities_df is None:
            self.build_communities_dataframe()

        df = self._communities_df
        return {
            "total_communities": len(df),
            "total_regions": df["region_name"].nunique(),
            "total_population_estimate": int(df["population_estimate"].sum()),
            "avg_relevance_score": round(df["modern_relevance_score"].mean(), 3),
            "avg_preservation_index": round(
                df["cultural_preservation_index"].mean(), 3
            ),
            "avg_blockchain_readiness": round(df["blockchain_readiness"].mean(), 3),
            "highest_relevance_community": df.loc[
                df["modern_relevance_score"].idxmax(), "community_name"
            ],
            "highest_preservation_community": df.loc[
                df["cultural_preservation_index"].idxmax(), "community_name"
            ],
        }


class AfroIdentityVisualizer:
    """Visualization tools for Afro-Sovereign Identity Map data.

    Provides bar charts, heat maps, and other visualizations for
    analyzing community metrics and geographic distributions.
    """

    # Default color palette matching dataset configuration
    COLORS = {
        "primary": "#1A1A2E",
        "secondary": "#16213E",
        "accent": "#E94560",
        "gold": "#FFD700",
        "earth": "#8B4513",
    }

    def __init__(self, framework: AfroIdentityFramework | None = None):
        """Initialize the visualizer.

        Args:
            framework: Optional framework instance. If None, creates default.
        """
        self.framework = framework or AfroIdentityFramework()

    def _get_matplotlib(self) -> Any:
        """Lazy import matplotlib to avoid import errors if not installed."""
        try:
            import matplotlib.pyplot as plt

            return plt
        except ImportError as e:
            msg = "matplotlib is required for visualization. Install with: pip install matplotlib"
            raise ImportError(msg) from e

    def plot_population_by_region(
        self, output_path: str | None = None, show: bool = False
    ) -> Any:
        """Create a bar chart of population by region.

        Args:
            output_path: Optional path to save the figure
            show: Whether to display the plot

        Returns:
            Matplotlib figure object
        """
        plt = self._get_matplotlib()

        df = self.framework.build_regions_dataframe()

        fig, ax = plt.subplots(figsize=(12, 6))

        regions = df["region_name"] + " " + df["region_emoji"]
        populations = df["population_estimate"] / 1_000_000  # Convert to millions

        bars = ax.bar(
            regions, populations, color=self.COLORS["accent"], edgecolor="white"
        )

        ax.set_xlabel("Region", fontsize=12)
        ax.set_ylabel("Population (Millions)", fontsize=12)
        ax.set_title(
            "Afro-Descendant Population by Region\n(Global Afro-Sovereign Identity Map)",
            fontsize=14,
            fontweight="bold",
        )

        ax.tick_params(axis="x", rotation=45)
        ax.grid(axis="y", alpha=0.3)

        # Add value labels on bars
        for bar, pop in zip(bars, populations):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.05,
                f"{pop:.2f}M",
                ha="center",
                va="bottom",
                fontsize=9,
            )

        plt.tight_layout()

        if output_path:
            plt.savefig(output_path, dpi=150, bbox_inches="tight")

        if show:
            plt.show()

        return fig

    def plot_relevance_scores(
        self, output_path: str | None = None, show: bool = False
    ) -> Any:
        """Create a horizontal bar chart of community relevance scores.

        Args:
            output_path: Optional path to save the figure
            show: Whether to display the plot

        Returns:
            Matplotlib figure object
        """
        plt = self._get_matplotlib()

        df = self.framework.build_communities_dataframe()
        df_sorted = df.sort_values("modern_relevance_score", ascending=True)

        fig, ax = plt.subplots(figsize=(10, 12))

        communities = df_sorted["community_name"]
        scores = df_sorted["modern_relevance_score"]

        colors = [
            self.COLORS["gold"] if s >= 0.95 else self.COLORS["accent"] for s in scores
        ]

        bars = ax.barh(communities, scores, color=colors, edgecolor="white")

        ax.set_xlabel("Modern Relevance Score", fontsize=12)
        ax.set_ylabel("Community", fontsize=10)
        ax.set_title(
            "Community Modern Relevance Scores\n(Afro-Sovereign Identity Map)",
            fontsize=14,
            fontweight="bold",
        )

        ax.set_xlim(0, 1.0)
        ax.grid(axis="x", alpha=0.3)

        # Add value labels
        for bar, score in zip(bars, scores):
            ax.text(
                score + 0.01,
                bar.get_y() + bar.get_height() / 2,
                f"{score:.2f}",
                ha="left",
                va="center",
                fontsize=8,
            )

        plt.tight_layout()

        if output_path:
            plt.savefig(output_path, dpi=150, bbox_inches="tight")

        if show:
            plt.show()

        return fig

    def plot_metrics_heatmap(
        self, output_path: str | None = None, show: bool = False
    ) -> Any:
        """Create a heat map of key metrics by community.

        Args:
            output_path: Optional path to save the figure
            show: Whether to display the plot

        Returns:
            Matplotlib figure object
        """
        plt = self._get_matplotlib()

        try:
            import numpy as np
        except ImportError as e:
            msg = "numpy is required for heatmap. Install with: pip install numpy"
            raise ImportError(msg) from e

        df = self.framework.build_communities_dataframe()

        metrics = [
            "modern_relevance_score",
            "cultural_preservation_index",
            "blockchain_readiness",
            "tourism_potential",
        ]

        data = df[metrics].values
        communities = df["community_name"].values

        fig, ax = plt.subplots(figsize=(10, 14))

        im = ax.imshow(data, cmap="YlOrRd", aspect="auto", vmin=0, vmax=1)

        ax.set_xticks(np.arange(len(metrics)))
        ax.set_yticks(np.arange(len(communities)))
        ax.set_xticklabels(
            ["Relevance", "Preservation", "Blockchain", "Tourism"], fontsize=10
        )
        ax.set_yticklabels(communities, fontsize=8)

        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

        # Add colorbar
        cbar = ax.figure.colorbar(im, ax=ax, shrink=0.5)
        cbar.ax.set_ylabel("Score (0-1)", rotation=-90, va="bottom", fontsize=10)

        # Add text annotations
        for i in range(len(communities)):
            for j in range(len(metrics)):
                val = data[i, j]
                color = "white" if val > 0.7 else "black"
                ax.text(
                    j,
                    i,
                    f"{val:.2f}",
                    ha="center",
                    va="center",
                    color=color,
                    fontsize=7,
                )

        ax.set_title(
            "Community Metrics Heatmap\n(Global Afro-Sovereign Identity Map)",
            fontsize=14,
            fontweight="bold",
        )

        plt.tight_layout()

        if output_path:
            plt.savefig(output_path, dpi=150, bbox_inches="tight")

        if show:
            plt.show()

        return fig

    def plot_blockchain_readiness_comparison(
        self, output_path: str | None = None, show: bool = False
    ) -> Any:
        """Create a comparison chart of blockchain readiness by region.

        Args:
            output_path: Optional path to save the figure
            show: Whether to display the plot

        Returns:
            Matplotlib figure object
        """
        plt = self._get_matplotlib()

        df = self.framework.build_regions_dataframe()
        df_sorted = df.sort_values("blockchain_readiness", ascending=False)

        fig, ax = plt.subplots(figsize=(10, 6))

        regions = df_sorted["region_name"] + " " + df_sorted["region_emoji"]
        readiness = df_sorted["blockchain_readiness"]

        bars = ax.bar(
            regions,
            readiness,
            color=self.COLORS["gold"],
            edgecolor=self.COLORS["primary"],
        )

        ax.set_xlabel("Region", fontsize=12)
        ax.set_ylabel("Blockchain Integration Readiness", fontsize=12)
        ax.set_title(
            "Blockchain Integration Readiness by Region\n(History-Global DEX Trade Anchor)",
            fontsize=14,
            fontweight="bold",
        )

        ax.set_ylim(0, 1.0)
        ax.tick_params(axis="x", rotation=45)
        ax.grid(axis="y", alpha=0.3)

        # Add threshold line
        ax.axhline(
            y=0.7,
            color=self.COLORS["accent"],
            linestyle="--",
            label="Integration Threshold",
        )
        ax.legend(loc="upper right")

        # Add value labels
        for bar, val in zip(bars, readiness):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.02,
                f"{val:.2f}",
                ha="center",
                va="bottom",
                fontsize=9,
            )

        plt.tight_layout()

        if output_path:
            plt.savefig(output_path, dpi=150, bbox_inches="tight")

        if show:
            plt.show()

        return fig


def generate_all_visualizations(output_dir: str = "visualizations") -> list[str]:
    """Generate all visualizations and save to output directory.

    Args:
        output_dir: Directory to save visualizations

    Returns:
        List of generated file paths
    """
    from pathlib import Path

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    visualizer = AfroIdentityVisualizer()
    generated_files = []

    # Generate population chart
    pop_path = output_path / "population_by_region.png"
    visualizer.plot_population_by_region(str(pop_path))
    generated_files.append(str(pop_path))

    # Generate relevance scores chart
    rel_path = output_path / "relevance_scores.png"
    visualizer.plot_relevance_scores(str(rel_path))
    generated_files.append(str(rel_path))

    # Generate metrics heatmap
    heat_path = output_path / "metrics_heatmap.png"
    visualizer.plot_metrics_heatmap(str(heat_path))
    generated_files.append(str(heat_path))

    # Generate blockchain readiness chart
    bc_path = output_path / "blockchain_readiness.png"
    visualizer.plot_blockchain_readiness_comparison(str(bc_path))
    generated_files.append(str(bc_path))

    return generated_files


__all__ = [
    "AfroIdentityDataLoader",
    "AfroIdentityFramework",
    "AfroIdentityVisualizer",
    "generate_all_visualizations",
]
