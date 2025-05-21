# Source Code Directory

This directory contains reusable Python modules and functions used across notebooks.

## Structure

- `utils/`: Utility functions for data processing, visualization, etc.
- (Additional modules can be added as needed)

## Usage

Import functions in notebooks as follows:

```python
import sys
sys.path.append("..")
from src.utils.visualization import plot_correlation_matrix
from src.utils.data_processing import clean_missing_values
```

## Contributing Guidelines

When adding new functions:

1. Add appropriate docstrings
2. Include type hints
3. Add unit tests where possible
4. Follow PEP 8 style guidelines
