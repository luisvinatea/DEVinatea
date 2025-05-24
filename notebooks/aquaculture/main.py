"""Main module for orchestrating financial analysis visualizations."""

from IPython.display import display, HTML
from visualizations import FinancialVisualizer
from config import DEFAULT_AERATOR_DATA


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


# Convenience function for quick analysis
def quick_analysis(aerator_data=None):
    """Run quick financial analysis with default parameters."""
    return create_all_visualizations(aerator_data)
