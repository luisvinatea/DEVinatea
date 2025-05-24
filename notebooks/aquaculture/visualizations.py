"""Visualization components for financial analysis."""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

from config import (
    VIZ_PARAMS,
    COLOR_SCHEMES,
    DEFAULT_AERATOR_DATA,
)
from calculations import (
    calculate_adapted_irr,
    calculate_sotr_impact_npv,
)


class FinancialVisualizer:
    """Main class for creating financial analysis visualizations."""

    def __init__(self, aerator_data=None):
        self.aerator_data = aerator_data or DEFAULT_AERATOR_DATA
        self._setup_style()
        self.colors_primary = sns.color_palette(COLOR_SCHEMES["primary"], 8)

    def _setup_style(self):
        """Configure matplotlib and seaborn styling."""
        sns.set_style(VIZ_PARAMS["style"])
        sns.set_context(
            VIZ_PARAMS["context"], font_scale=VIZ_PARAMS["font_scale"]
        )
        plt.rcParams["figure.dpi"] = VIZ_PARAMS["figure_dpi"]
        plt.rcParams["savefig.dpi"] = VIZ_PARAMS["savefig_dpi"]

    def create_irr_comparison_plot(self, figsize=(12, 8)):
        """Create Traditional vs Adapted IRR comparison plot."""
        fig, ax = plt.subplots(1, 1, figsize=figsize)

        delta_investments = np.linspace(-1000000, 1000000, 100)
        annual_saving = 200000

        # Calculate IRR values
        adapted_irrs = [
            calculate_adapted_irr(delta_i, annual_saving)
            for delta_i in delta_investments
        ]
        traditional_irrs = [
            min((annual_saving / delta_i) * 100, 100) if delta_i > 0 else None
            for delta_i in delta_investments
        ]

        # Create DataFrames
        df_adapted = pd.DataFrame(
            {
                "Delta Investment": delta_investments,
                "IRR": adapted_irrs,
                "Type": "Adapted IRR",
            }
        )

        valid_indices = [
            i for i, irr in enumerate(traditional_irrs) if irr is not None
        ]
        df_traditional = pd.DataFrame(
            {
                "Delta Investment": [
                    delta_investments[i] for i in valid_indices
                ],
                "IRR": [traditional_irrs[i] for i in valid_indices],
                "Type": "Traditional IRR",
            }
        )

        # Plot lines
        sns.lineplot(
            data=df_adapted,
            x="Delta Investment",
            y="IRR",
            linewidth=3,
            color=self.colors_primary[0],
            label="Adapted IRR",
            ax=ax,
        )
        sns.lineplot(
            data=df_traditional,
            x="Delta Investment",
            y="IRR",
            linewidth=2,
            linestyle="--",
            color=self.colors_primary[3],
            label="Traditional IRR",
            ax=ax,
        )

        # Styling
        self._style_irr_plot(ax, delta_investments)
        return fig

    def create_npv_analysis_plot(self, figsize=(16, 8)):
        """Create NPV analysis with two subplots."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

        # Subplot 1: NPV vs Time Horizon
        self._create_npv_time_plot(ax1)

        # Subplot 2: NPV vs SOTR Improvement
        self._create_npv_sotr_plot(ax2)

        sns.despine(fig=fig)
        plt.tight_layout()
        return fig

    def create_irr_heatmap(self, figsize=(14, 10)):
        """Create IRR heatmap visualization."""
        fig, ax = plt.subplots(1, 1, figsize=figsize)

        # Generate grid data
        delta_inv_range = np.linspace(-1000000, 1000000, 25)
        annual_savings_range = np.linspace(50000, 500000, 25)
        irr_grid = np.zeros((len(annual_savings_range), len(delta_inv_range)))

        for i, saving in enumerate(annual_savings_range):
            for j, delta_inv in enumerate(delta_inv_range):
                irr_grid[i, j] = calculate_adapted_irr(delta_inv, saving)

        irr_grid = np.clip(irr_grid, -20, 100)

        # Create heatmap
        self._create_heatmap(
            ax, irr_grid, delta_inv_range, annual_savings_range
        )
        return fig

    def create_aerator_comparison_chart(
        self, aerator_results, figsize=(14, 10)
    ):
        """Create comprehensive aerator comparison chart."""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=figsize)

        # Extract data for plotting
        names = [result["name"] for result in aerator_results]
        total_costs = [
            result["total_annual_cost"] for result in aerator_results
        ]
        initial_costs = [
            result["total_initial_cost"] for result in aerator_results
        ]
        sae_values = [result["sae"] for result in aerator_results]
        roi_values = [result["roi_percent"] for result in aerator_results]

        # 1. Total Annual Cost Comparison
        bars1 = ax1.bar(names, total_costs, color=self.colors_primary)
        ax1.set_title("Total Annual Cost Comparison", fontweight="bold")
        ax1.set_ylabel("Annual Cost ($)")
        ax1.tick_params(axis="x", rotation=45)

        # Add value labels on bars
        for bar, cost in zip(bars1, total_costs):
            height = bar.get_height()
            ax1.text(
                bar.get_x() + bar.get_width() / 2.0,
                height,
                f"${cost:,.0f}",
                ha="center",
                va="bottom",
            )

        # 2. Initial Investment vs SAE
        ax2.scatter(
            sae_values,
            initial_costs,
            s=100,
            c=range(len(names)),
            cmap="viridis",
            alpha=0.7,
        )
        ax2.set_xlabel("Standard Aeration Efficiency (SAE)")
        ax2.set_ylabel("Initial Investment ($)")
        ax2.set_title("Efficiency vs Investment", fontweight="bold")

        # Add labels for each point
        for i, name in enumerate(names):
            ax2.annotate(
                name,
                (sae_values[i], initial_costs[i]),
                xytext=(5, 5),
                textcoords="offset points",
            )

        # 3. ROI Comparison
        bars3 = ax3.bar(names, roi_values, color=self.colors_primary)
        ax3.set_title("Return on Investment (ROI)", fontweight="bold")
        ax3.set_ylabel("ROI (%)")
        ax3.tick_params(axis="x", rotation=45)
        ax3.axhline(y=0, color="red", linestyle="--", alpha=0.5)

        # Add value labels on bars
        for bar, roi in zip(bars3, roi_values):
            height = bar.get_height()
            ax3.text(
                bar.get_x() + bar.get_width() / 2.0,
                height,
                f"{roi:.1f}%",
                ha="center",
                va="bottom" if roi >= 0 else "top",
            )

        # 4. Payback Period
        payback_values = [
            result["payback_years"] for result in aerator_results
        ]
        # Handle infinite payback periods
        payback_display = [
            min(p, 20) if p != float("inf") else 20 for p in payback_values
        ]

        bars4 = ax4.bar(names, payback_display, color=self.colors_primary)
        ax4.set_title("Payback Period", fontweight="bold")
        ax4.set_ylabel("Years")
        ax4.tick_params(axis="x", rotation=45)

        # Add value labels on bars
        for bar, payback in zip(bars4, payback_values):
            height = bar.get_height()
            label = f"{payback:.1f}" if payback != float("inf") else "∞"
            ax4.text(
                bar.get_x() + bar.get_width() / 2.0,
                height,
                label,
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        return fig

    def create_cost_breakdown_chart(self, aerator_results, figsize=(12, 8)):
        """Create stacked bar chart showing cost breakdown."""
        fig, ax = plt.subplots(figsize=figsize)

        names = [result["name"] for result in aerator_results]
        energy_costs = [
            result["annual_energy_cost"] for result in aerator_results
        ]
        maintenance_costs = [
            result["annual_maintenance_cost"] for result in aerator_results
        ]
        replacement_costs = [
            result["annual_replacement_cost"] for result in aerator_results
        ]

        # Create stacked bar chart
        width = 0.6
        x = np.arange(len(names))

        ax.bar(x, energy_costs, width, label="Energy Cost", color="#FF6B6B")
        ax.bar(
            x,
            maintenance_costs,
            width,
            bottom=energy_costs,
            label="Maintenance Cost",
            color="#4ECDC4",
        )
        ax.bar(
            x,
            replacement_costs,
            width,
            bottom=np.array(energy_costs) + np.array(maintenance_costs),
            label="Replacement Cost",
            color="#45B7D1",
        )

        ax.set_title("Annual Cost Breakdown by Aerator", fontweight="bold")
        ax.set_ylabel("Annual Cost ($)")
        ax.set_xticks(x)
        ax.set_xticklabels(names, rotation=45)
        ax.legend()

        plt.tight_layout()
        return fig

    def create_efficiency_scatter(self, aerator_results, figsize=(10, 8)):
        """Create scatter plot of efficiency metrics."""
        fig, ax = plt.subplots(figsize=figsize)

        sae_values = [result["sae"] for result in aerator_results]
        cost_per_kg_o2 = [
            result["cost_per_kg_o2"] for result in aerator_results
        ]
        total_costs = [
            result["total_annual_cost"] for result in aerator_results
        ]
        names = [result["name"] for result in aerator_results]

        # Create scatter plot with bubble size based on total cost
        # Normalize bubble sizes
        max_cost = max(total_costs)
        min_cost = min(total_costs)
        bubble_sizes = [
            100 + 400 * (cost - min_cost) / (max_cost - min_cost)
            for cost in total_costs
        ]

        ax.scatter(
            sae_values,
            cost_per_kg_o2,
            s=bubble_sizes,
            alpha=0.6,
            c=range(len(names)),
            cmap="viridis",
        )

        ax.set_xlabel("Standard Aeration Efficiency (SAE)")
        ax.set_ylabel("Cost per kg O₂ ($/kg)")
        ax.set_title(
            "Aeration Efficiency vs Operating Cost", fontweight="bold"
        )

        # Add labels for each point
        for i, name in enumerate(names):
            ax.annotate(
                name,
                (sae_values[i], cost_per_kg_o2[i]),
                xytext=(5, 5),
                textcoords="offset points",
            )

        # Add size legend
        ax.text(
            0.02,
            0.98,
            "Bubble size = Total Annual Cost",
            transform=ax.transAxes,
            verticalalignment="top",
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
        )

        return fig

    def create_sensitivity_analysis(
        self, base_results, parameter_name, parameter_range, figsize=(12, 8)
    ):
        """Create sensitivity analysis chart for a given parameter."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

        # This is a simplified version - in practice, you'd recalculate
        # results for each parameter value
        base_npv = [result["npv_savings"] for result in base_results]
        base_irr = [result["irr"] for result in base_results]
        names = [result["name"] for result in base_results]

        # Simulate sensitivity (this would be replaced with actual recalculation)
        for i, name in enumerate(names):
            npv_sensitivity = [
                base_npv[i]
                * (
                    1
                    + 0.1
                    * (p - parameter_range[len(parameter_range) // 2])
                    / parameter_range[len(parameter_range) // 2]
                )
                for p in parameter_range
            ]
            irr_sensitivity = [
                base_irr[i]
                * (
                    1
                    + 0.05
                    * (p - parameter_range[len(parameter_range) // 2])
                    / parameter_range[len(parameter_range) // 2]
                )
                for p in parameter_range
            ]

            ax1.plot(parameter_range, npv_sensitivity, label=name, marker="o")
            ax2.plot(parameter_range, irr_sensitivity, label=name, marker="s")

        ax1.set_xlabel(f"{parameter_name}")
        ax1.set_ylabel("NPV Savings ($)")
        ax1.set_title(f"NPV Sensitivity to {parameter_name}")
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        ax2.set_xlabel(f"{parameter_name}")
        ax2.set_ylabel("IRR (%)")
        ax2.set_title(f"IRR Sensitivity to {parameter_name}")
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        return fig

    def create_financial_summary_table(self, aerator_results, figsize=(14, 8)):
        """Create a comprehensive financial summary table."""
        fig, ax = plt.subplots(figsize=figsize)
        ax.axis("tight")
        ax.axis("off")

        # Prepare data for table
        headers = [
            "Aerator",
            "Total Cost\n($)",
            "NPV Savings\n($)",
            "ROI\n(%)",
            "IRR\n(%)",
            "Payback\n(years)",
            "SAE",
        ]

        table_data = []
        for result in aerator_results:
            payback = result["payback_years"]
            payback_str = f"{payback:.1f}" if payback != float("inf") else "∞"

            row = [
                result["name"],
                f"${result['total_annual_cost']:,.0f}",
                f"${result['npv_savings']:,.0f}",
                f"{result['roi_percent']:.1f}%",
                f"{result['irr']:.1f}%",
                payback_str,
                f"{result['sae']:.2f}",
            ]
            table_data.append(row)

        # Create table
        table = ax.table(
            cellText=table_data,
            colLabels=headers,
            cellLoc="center",
            loc="center",
        )

        # Style the table
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.5)

        # Color header row
        for i in range(len(headers)):
            table[(0, i)].set_facecolor("#4ECDC4")
            table[(0, i)].set_text_props(weight="bold", color="white")

        # Color rows alternately
        for i in range(1, len(table_data) + 1):
            for j in range(len(headers)):
                if i % 2 == 0:
                    table[(i, j)].set_facecolor("#F0F0F0")

        ax.set_title("Financial Analysis Summary", fontweight="bold", pad=20)

        return fig

    def _create_npv_time_plot(self, ax):
        """Create NPV vs time horizon subplot."""
        years_range = np.arange(1, 21)
        npv_data = []

        # Get SOTR values - use defaults if specific keys don't exist
        if "SOTR = 1.0" in self.aerator_data:
            sotr_baseline = self.aerator_data["SOTR = 1.0"]["sotr"]
        else:
            sotr_baseline = DEFAULT_AERATOR_DATA["SOTR = 1.0"]["sotr"]

        if "Aerator 2 (SOTR = 3.0)" in self.aerator_data:
            sotr_aerator2 = self.aerator_data["Aerator 2 (SOTR = 3.0)"]["sotr"]
        else:
            sotr_aerator2 = DEFAULT_AERATOR_DATA["Aerator 2 (SOTR = 3.0)"][
                "sotr"
            ]

        if "Aerator 1 (SOTR = 1.5)" in self.aerator_data:
            sotr_aerator1 = self.aerator_data["Aerator 1 (SOTR = 1.5)"]["sotr"]
        else:
            sotr_aerator1 = DEFAULT_AERATOR_DATA["Aerator 1 (SOTR = 1.5)"][
                "sotr"
            ]

        for years in years_range:
            # Aerator 2 vs Baseline
            npv_vs_baseline = calculate_sotr_impact_npv(
                sotr_baseline, sotr_aerator2, years=years
            )
            npv_data.append(
                {
                    "Years": years,
                    "NPV ($)": npv_vs_baseline,
                    "Comparison": "Aerator 2 vs Baseline",
                    "SOTR_Diff": sotr_aerator2 - sotr_baseline,
                }
            )

            # Aerator 2 vs Aerator 1
            npv_vs_aerator1 = calculate_sotr_impact_npv(
                sotr_aerator1, sotr_aerator2, years=years
            )
            npv_data.append(
                {
                    "Years": years,
                    "NPV ($)": npv_vs_aerator1,
                    "Comparison": "Aerator 2 vs Aerator 1",
                    "SOTR_Diff": sotr_aerator2 - sotr_aerator1,
                }
            )

        npv_df = pd.DataFrame(npv_data)

        sns.lineplot(
            data=npv_df,
            x="Years",
            y="NPV ($)",
            hue="Comparison",
            linewidth=3,
            ax=ax,
            palette=[self.colors_primary[0], self.colors_primary[2]],
        )

        self._style_npv_time_plot(ax, npv_df)

    def _create_npv_sotr_plot(self, ax):
        """Create NPV vs SOTR improvement subplot."""
        sotr_improvements = np.linspace(0.1, 3.0, 30)
        baseline_sotr = 1.0

        npv_data = []
        for sotr_improvement in sotr_improvements:
            improved_sotr = baseline_sotr + sotr_improvement
            npv_10yr = calculate_sotr_impact_npv(baseline_sotr, improved_sotr)
            npv_data.append(
                {"SOTR_Improvement": sotr_improvement, "NPV_10yr": npv_10yr}
            )

        npv_sotr_df = pd.DataFrame(npv_data)

        sns.lineplot(
            data=npv_sotr_df,
            x="SOTR_Improvement",
            y="NPV_10yr",
            linewidth=4,
            color=self.colors_primary[4],
            ax=ax,
        )

        self._style_npv_sotr_plot(ax, baseline_sotr)

    def _style_irr_plot(self, ax, delta_investments):
        """Apply styling to IRR comparison plot."""
        ax.axvline(x=0, color="gray", linestyle="-", alpha=0.5, linewidth=1)
        ax.axhline(y=0, color="gray", linestyle="-", alpha=0.5, linewidth=1)

        ax.fill_between(
            delta_investments,
            0,
            100,
            where=(delta_investments < 0),
            color=self.colors_primary[2],
            alpha=0.2,
            label="Better & Cheaper Region",
        )

        ax.set_title(
            "Traditional vs Adapted IRR Analysis",
            fontsize=18,
            pad=20,
            fontweight="bold",
        )
        ax.set_xlabel(
            "Delta Investment ($)", fontsize=14, fontweight="semibold"
        )
        ax.set_ylabel("IRR (%)", fontsize=14, fontweight="semibold")
        ax.set_ylim(-25, 115)

        ax.xaxis.set_major_formatter(
            plt.FuncFormatter(lambda x, p: f"${x / 1e6:.1f}M")
        )
        ax.legend(frameon=True, fancybox=True, shadow=True, fontsize=12)

        # Add annotation
        ax.annotate(
            "Traditional IRR undefined\nfor negative delta investment",
            xy=(-500000, 50),
            xytext=(-700000, 80),
            arrowprops=dict(
                arrowstyle="->", color=self.colors_primary[3], lw=2
            ),
            fontsize=11,
            ha="center",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.9),
        )

    def _style_npv_time_plot(self, ax, npv_df):
        """Apply styling to NPV time plot."""
        ax.set_title(
            "NPV of Savings: SOTR Impact Over Time",
            fontsize=16,
            pad=20,
            fontweight="bold",
        )
        ax.set_xlabel(
            "Analysis Horizon (Years)", fontsize=14, fontweight="semibold"
        )
        ax.set_ylabel("NPV of Savings ($)", fontsize=14, fontweight="semibold")
        ax.yaxis.set_major_formatter(
            plt.FuncFormatter(lambda x, p: f"${x / 1000:.0f}K")
        )
        ax.legend(frameon=True, fancybox=True, shadow=True, fontsize=11)
        ax.grid(True, alpha=0.3)

    def _style_npv_sotr_plot(self, ax, baseline_sotr):
        """Apply styling to NPV SOTR plot."""
        ax.set_title(
            "NPV Sensitivity to SOTR Improvement\n(10-Year Analysis)",
            fontsize=16,
            pad=20,
            fontweight="bold",
        )
        ax.set_xlabel(
            "SOTR Improvement (vs Baseline)",
            fontsize=14,
            fontweight="semibold",
        )
        ax.set_ylabel("NPV of Savings ($)", fontsize=14, fontweight="semibold")
        ax.yaxis.set_major_formatter(
            plt.FuncFormatter(lambda x, p: f"${x / 1000:.0f}K")
        )

        ax.text(
            0.05,
            0.95,
            "Linear relationship:\nNPV ∝ SOTR improvement",
            transform=ax.transAxes,
            fontsize=11,
            fontweight="bold",
            verticalalignment="top",
            bbox=dict(
                boxstyle="round,pad=0.4", facecolor="lightblue", alpha=0.8
            ),
        )
        ax.grid(True, alpha=0.3)

    def _create_heatmap(
        self, ax, irr_grid, delta_inv_range, annual_savings_range
    ):
        """Create and style IRR heatmap."""
        cmap = LinearSegmentedColormap.from_list(
            "irr_cmap", COLOR_SCHEMES["heatmap"]
        )

        heatmap_data = pd.DataFrame(
            irr_grid,
            index=annual_savings_range / 1000,
            columns=delta_inv_range / 1000,
        )

        sns.heatmap(
            heatmap_data,
            cmap=cmap,
            center=25,
            cbar_kws={"label": "IRR (%)", "shrink": 0.8},
            ax=ax,
            fmt=".0f",
        )

        # Add contour lines
        contour_levels = [0, 10, 25, 50, 75]
        CS = ax.contour(
            np.arange(len(delta_inv_range)),
            np.arange(len(annual_savings_range)),
            irr_grid,
            levels=contour_levels,
            colors="black",
            alpha=0.8,
            linewidths=1.5,
        )
        ax.clabel(CS, inline=True, fontsize=10, fmt="%d%%", colors="black")

        # Add vertical line at delta_investment = 0
        zero_index = np.argmin(np.abs(delta_inv_range))
        ax.axvline(x=zero_index, color="black", linestyle="-", linewidth=3)

        ax.set_title(
            "IRR Landscape: Investment vs Annual Savings",
            fontsize=18,
            pad=20,
            fontweight="bold",
        )
        ax.set_xlabel(
            "Delta Investment ($K)", fontsize=14, fontweight="semibold"
        )
        ax.set_ylabel(
            "Annual Savings ($K)", fontsize=14, fontweight="semibold"
        )

        # Customize tick labels
        x_ticks = np.arange(0, len(delta_inv_range), 6)
        y_ticks = np.arange(0, len(annual_savings_range), 6)
        ax.set_xticks(x_ticks)
        ax.set_yticks(y_ticks)
        ax.set_xticklabels(
            [f"{delta_inv_range[i] / 1000:.0f}" for i in x_ticks], rotation=0
        )
        ax.set_yticklabels(
            [f"{annual_savings_range[i] / 1000:.0f}" for i in y_ticks]
        )
