"""Main module for orchestrating financial analysis visualizations."""

from IPython.display import display, HTML
from visualizations import FinancialVisualizer
from config import DEFAULT_AERATOR_DATA
from aerator_comparer import compare_aerators


def create_all_visualizations(aerator_data=None, show_figures=True):
    """Create all financial analysis visualizations."""
    aerator_data = aerator_data or DEFAULT_AERATOR_DATA

    visualizer = FinancialVisualizer(aerator_data)
    figures = []

    # Create all visualizations
    fig1 = visualizer.create_irr_comparison_plot()
    figures.append(("IRR Comparison", fig1))

    fig2 = visualizer.create_npv_analysis_plot()
    figures.append(("NPV Analysis", fig2))

    fig3 = visualizer.create_irr_heatmap()
    figures.append(("IRR Heatmap", fig3))

    # Display results
    _display_financial_insights()

    if show_figures:
        for title, fig in figures:
            print(f"\n--- {title} ---")
            display(fig)

    return figures


def _display_financial_insights():
    """Display financial analysis insights."""
    html_content = """
    <div style="margin: 20px 0; padding: 20px; border-left: 5px solid #2E8B57; 
                background-color: transparent; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h3 style="color: #2E8B57; margin-top: 0;">🚀 Financial Analysis Insights</h3>
        
        <p><strong style="color: #1a472a;">Key Advantages of Adapted Methods:</strong></p>
        <ul style="line-height: 1.6;">
            <li><strong>Comprehensive IRR handling:</strong> Properly manages negative delta investment scenarios</li>
            <li><strong>Realistic NPV modeling:</strong> Incorporates inflation-adjusted savings streams</li>
            <li><strong>Robust calculations:</strong> Multiple fallback methods ensure reliability</li>
            <li><strong>Clear interpretations:</strong> Investment attractiveness clearly categorized</li>
        </ul>

        <p><strong style="color: #1a472a;">💡 Strategic Insights:</strong></p>
        <ul style="line-height: 1.6;">
            <li>Higher SOTR aerators show linear NPV improvement relationships</li>
            <li>Better & cheaper regions indicate dominant investment strategies</li>
            <li>Long-term analysis reveals true economic value of efficiency investments</li>
        </ul>
    </div>
    """
    display(HTML(html_content))


def run_aerator_comparison(
    farm_data=None, financial_data=None, aerators_data=None
):
    """
    Run comprehensive aerator comparison analysis.

    Args:
        farm_data: Dictionary with farm parameters
        financial_data: Dictionary with financial parameters
        aerators_data: List of aerator specifications

    Returns:
        Complete comparison results and visualizations
    """
    # Use default data if not provided
    if not farm_data:
        farm_data = {
            "tod": 5.47,
            "farm_area_ha": 1000,
            "shrimp_price": 5.0,
            "culture_days": 120,
            "shrimp_density_kg_m3": 0.3333333,
            "pond_depth_m": 1.0,
        }

    if not financial_data:
        financial_data = {
            "energy_cost": 0.05,
            "hours_per_night": 8,
            "discount_rate": 0.1,
            "inflation_rate": 0.025,
            "horizon": 10,
            "safety_margin": 0,
            "temperature": 31.5,
        }

    if not aerators_data:
        aerators_data = [
            {
                "name": "Aerator 1",
                "sotr": 1.9,
                "power_hp": 3,
                "cost": 700,
                "durability": 2.0,
                "maintenance": 65,
            },
            {
                "name": "Aerator 2",
                "sotr": 3.5,
                "power_hp": 3,
                "cost": 900,
                "durability": 5.0,
                "maintenance": 50,
            },
            {
                "name": "Aerator 3",
                "sotr": 2.8,
                "power_hp": 2.5,
                "cost": 800,
                "durability": 3.0,
                "maintenance": 55,
            },
        ]

    # Run comparison
    comparison_data = {
        "farm": farm_data,
        "financial": financial_data,
        "aerators": aerators_data,
    }

    results = compare_aerators(comparison_data)

    if "error" in results:
        print(f"Error in comparison: {results['error']}")
        return results

    # Create visualizations
    visualizer = FinancialVisualizer()
    aerator_results = results["aeratorResults"]

    print("=== AERATOR COMPARISON ANALYSIS ===\n")
    print(f"Total Oxygen Demand: {results['tod']:.2f} kg O₂/hour")
    print(f"Annual Revenue: ${results['annual_revenue']:,.2f}")
    print(f"Winner: {results['winnerLabel']}\n")

    # Display key metrics table
    print("Key Financial Metrics:")
    print("-" * 80)
    print(
        f"{'Aerator':<15} {'Total Cost':<12} {'NPV Savings':<12} {'ROI (%)':<8} {'IRR (%)':<8} {'Payback':<10}"
    )
    print("-" * 80)

    for result in aerator_results:
        payback = result["payback_years"]
        payback_str = f"{payback:.1f}" if payback != float("inf") else "∞"
        print(
            f"{result['name']:<15} ${result['total_annual_cost']:<11,.0f} "
            f"${result['npv_savings']:<11,.0f} {result['roi_percent']:<7.1f} "
            f"{result['irr']:<7.1f} {payback_str:<10}"
        )

    print("-" * 80)

    # Create and display visualizations
    figures = []

    # 1. Comprehensive comparison chart
    fig1 = visualizer.create_aerator_comparison_chart(aerator_results)
    figures.append(("Aerator Comparison Overview", fig1))

    # 2. Cost breakdown
    fig2 = visualizer.create_cost_breakdown_chart(aerator_results)
    figures.append(("Annual Cost Breakdown", fig2))

    # 3. Efficiency analysis
    fig3 = visualizer.create_efficiency_scatter(aerator_results)
    figures.append(("Efficiency Analysis", fig3))

    # 4. Financial summary table
    fig4 = visualizer.create_financial_summary_table(aerator_results)
    figures.append(("Financial Summary", fig4))

    # Display all figures
    for title, fig in figures:
        print(f"\n--- {title} ---")
        display(fig)

    return {
        "results": results,
        "figures": figures,
        "summary": {
            "winner": results["winnerLabel"],
            "total_aerators": len(aerator_results),
            "annual_revenue": results["annual_revenue"],
            "equilibrium_prices": results.get("equilibriumPrices", {}),
        },
    }


def create_sample_sensitivity_analysis():
    """Create sample sensitivity analysis for demonstration."""
    # Sample data for sensitivity analysis
    base_results = [
        {"name": "Aerator 1", "npv_savings": 50000, "irr": 15.5},
        {"name": "Aerator 2", "npv_savings": 75000, "irr": 22.3},
    ]

    # Energy cost sensitivity
    energy_costs = [0.03, 0.04, 0.05, 0.06, 0.07, 0.08]

    visualizer = FinancialVisualizer()
    fig = visualizer.create_sensitivity_analysis(
        base_results, "Energy Cost ($/kWh)", energy_costs
    )

    print("\n--- Energy Cost Sensitivity Analysis ---")
    display(fig)

    return fig
