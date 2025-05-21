"""
Notebook utilities for easily creating and managing analysis notebooks.
"""

import os
import json
from datetime import datetime


def create_notebook_template(output_path: str, title: str, author: str = "Luis Paulo Vinatea Barberena") -> None:
    """
    Create a template Jupyter notebook for data analysis.
    
    Parameters
    ----------
    output_path : str
        Path where the notebook should be saved
    title : str
        Title of the analysis
    author : str, default "Luis Paulo Vinatea Barberena"
        Author name
        
    Returns
    -------
    None
        Writes notebook to disk
    """
    # Get current date
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Create cells
    cells = [
        # Title and overview
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# {title}\n",
                f"\n",
                f"**Author:** {author}  \n",
                f"**Date:** {today}  \n",
                f"\n",
                f"## Overview\n",
                f"\n",
                f"[Brief description of the analysis, objectives, and research questions]"
            ]
        },
        
        # Setup cell
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Setup and Environment"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Import standard libraries\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "\n",
                "# Import project utilities\n",
                "import sys\n",
                "sys.path.append('../')\n",
                "from src.utils.data_processing import *\n",
                "from src.utils.visualization import *\n",
                "\n",
                "# Visualization settings\n",
                "plt.style.use('seaborn-v0_8-whitegrid')\n",
                "%matplotlib inline\n",
                "sns.set_palette('viridis')\n",
                "plt.rcParams['figure.figsize'] = (12, 8)\n",
                "pd.set_option('display.max_columns', None)\n",
                "\n",
                "# For reproducibility\n",
                "np.random.seed(42)"
            ]
        },
        
        # Data loading
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Data Loading and Inspection"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Data paths\n",
                "DATA_DIR = '../data/'\n",
                "RAW_DATA_PATH = DATA_DIR + 'raw/dataset.csv'  # Update with actual filename\n",
                "\n",
                "# Load data\n",
                "try:\n",
                "    df = pd.read_csv(RAW_DATA_PATH)\n",
                "    print(f\"Data loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.\")\n",
                "except Exception as e:\n",
                "    print(f\"Error loading data: {e}\")"
            ]
        }
    ]
    
    # Create notebook JSON
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)
    
    print(f"Notebook template created successfully at {output_path}")


if __name__ == "__main__":
    # Example usage
    create_notebook_template(
        "new_analysis.ipynb",
        "Customer Churn Analysis"
    )
