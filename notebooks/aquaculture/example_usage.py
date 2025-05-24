from main import quick_analysis
from visualizations import FinancialVisualizer

# Quick analysis with default data
figures = quick_analysis()

# Or customize with your own data
custom_aerator_data = {
    "Custom Aerator": {
        "sotr": 2.5,
        "total_investment": 700000,
        "total_annual_cost": 0.12,
    }
}

visualizer = FinancialVisualizer(custom_aerator_data)
irr_plot = visualizer.create_irr_comparison_plot()
npv_plot = visualizer.create_npv_analysis_plot()
