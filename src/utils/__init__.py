"""Utility functions for data analysis projects."""

from .data_processing import (
    clean_missing_values,
)

from .visualization import (
    plot_correlation_matrix,
)

from .notebook_utils import (
    create_notebook_template,
)

# This allows using the syntax: from src.utils import *
__all__ = [
    "clean_missing_values",
    "plot_correlation_matrix",
    "create_notebook_template",
]
