"""Financial Analysis Package for Aerator Comparison."""

from .main import create_all_visualizations, quick_analysis
from .visualizations import FinancialVisualizer
from .calculations import (
    calculate_adapted_irr,
    calculate_npv_savings,
    calculate_sotr_impact_npv,
    interpret_irr,
)
from .config import DEFAULT_AERATOR_DATA, FINANCIAL_PARAMS

__version__ = "1.0.0"
__all__ = [
    "create_all_visualizations",
    "quick_analysis",
    "FinancialVisualizer",
    "calculate_adapted_irr",
    "calculate_npv_savings",
    "calculate_sotr_impact_npv",
    "interpret_irr",
    "DEFAULT_AERATOR_DATA",
    "FINANCIAL_PARAMS",
]
