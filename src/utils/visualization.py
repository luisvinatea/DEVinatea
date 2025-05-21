"""Visualization utilities for data analysis projects."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List, Tuple, Union


def plot_correlation_matrix(df: pd.DataFrame, figsize: Tuple[int, int] = (10, 8), 
                          method: str = 'pearson', cmap: str = 'coolwarm',
                          mask_upper: bool = True, annotate: bool = True) -> None:
    """
    Plot correlation matrix for a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to analyze
    figsize : Tuple[int, int], default (10, 8)
        Figure size
    method : str, default 'pearson'
        Correlation method: 'pearson', 'kendall', or 'spearman'
    cmap : str, default 'coolwarm'
        Colormap for the heatmap
    mask_upper : bool, default True
        Whether to mask the upper triangle
    annotate : bool, default True
        Whether to annotate the cells with correlation values
    """
    corr = df.corr(method=method)
    
    # Create mask for upper triangle
    mask = None
    if mask_upper:
        mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Create figure
    plt.figure(figsize=figsize)
    
    # Generate heatmap
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
                annot=annotate, fmt='.2f', square=True, linewidths=.5)
    
    plt.title(f'Correlation Matrix ({method.capitalize()})', fontsize=16)
    plt.tight_layout()
    plt.show()


def plot_distribution(df: pd.DataFrame, column: str, bins: int = 30, kde: bool = True,
                    figsize: Tuple[int, int] = (10, 6)) -> None:
    """
    Plot distribution of a numeric column.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to analyze
    column : str
        Column name to plot
    bins : int, default 30
        Number of bins for histogram
    kde : bool, default True
        Whether to overlay a Kernel Density Estimate
    figsize : Tuple[int, int], default (10, 6)
        Figure size
    """
    plt.figure(figsize=figsize)
    
    sns.histplot(df[column], bins=bins, kde=kde)
    
    plt.title(f'Distribution of {column}', fontsize=16)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Display descriptive statistics
    desc_stats = df[column].describe()
    print(f"Descriptive Statistics for {column}:")
    print(desc_stats)
    
    # Check for skewness and kurtosis
    from scipy import stats
    skewness = stats.skew(df[column].dropna())
    kurtosis = stats.kurtosis(df[column].dropna())
    print(f"Skewness: {skewness:.4f}")
    print(f"Kurtosis: {kurtosis:.4f}")


def plot_missing_values(df: pd.DataFrame, figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Visualize missing values in a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to analyze
    figsize : Tuple[int, int], default (12, 6)
        Figure size
    """
    plt.figure(figsize=figsize)
    
    # Calculate missing values percentage
    missing = (df.isnull().sum() / len(df)) * 100
    missing = missing[missing > 0].sort_values(ascending=False)
    
    if missing.empty:
        print("No missing values found in the DataFrame.")
        return
    
    # Plot
    sns.barplot(x=missing.index, y=missing.values)
    
    plt.title('Percentage of Missing Values by Column', fontsize=16)
    plt.xlabel('Columns')
    plt.ylabel('Missing Values (%)')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Print summary
    print("Missing Values Summary:")
    print(pd.DataFrame({
        'Column': missing.index,
        'Missing Values (%)': missing.values,
        'Missing Count': df[missing.index].isnull().sum().values
    }))


def plot_categorical_counts(df: pd.DataFrame, column: str, top_n: Optional[int] = None,
                          figsize: Tuple[int, int] = (10, 6), sort: bool = True,
                          horizontal: bool = False) -> None:
    """
    Plot counts of categorical variables.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to analyze
    column : str
        Column name to plot
    top_n : int, optional
        Plot only the top N categories
    figsize : Tuple[int, int], default (10, 6)
        Figure size
    sort : bool, default True
        Whether to sort categories by count
    horizontal : bool, default False
        Whether to use a horizontal bar plot
    """
    plt.figure(figsize=figsize)
    
    # Calculate value counts
    value_counts = df[column].value_counts()
    
    # Sort if requested
    if not sort:
        value_counts = value_counts.sort_index()
    
    # Filter to top N if requested
    if top_n is not None and top_n < len(value_counts):
        if sort:
            value_counts = value_counts.head(top_n)
        else:
            value_counts = value_counts.sort_values(ascending=False).head(top_n).sort_index()
    
    # Create plot
    if horizontal:
        sns.barplot(x=value_counts.values, y=value_counts.index)
        plt.xlabel('Count')
        plt.ylabel(column)
    else:
        sns.barplot(x=value_counts.index, y=value_counts.values)
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
    
    plt.title(f'Distribution of {column}', fontsize=16)
    plt.grid(axis='both' if horizontal else 'y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Print percentage distribution
    percentage = value_counts / value_counts.sum() * 100
    print(f"Distribution of {column}:")
    for i, (val, count) in enumerate(value_counts.items()):
        print(f"{val}: {count} ({percentage.iloc[i]:.2f}%)")
