"""Data processing utilities for cleaning and transforming data."""

import pandas as pd
import numpy as np
from typing import Union, List, Optional, Dict, Any


def clean_missing_values(
    df: pd.DataFrame, strategy: str = "drop", fill_value: Any = None
) -> pd.DataFrame:
    """
    Clean missing values in a pandas DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to clean
    strategy : str, default 'drop'
        Strategy to handle missing values: 'drop', 'mean', 'median', 'mode', 'fill'
    fill_value : Any, default None
        Value to use when strategy='fill'

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame

    Examples
    --------
    >>> df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
    >>> clean_missing_values(df, strategy='mean')
    """
    df_cleaned = df.copy()

    if strategy == "drop":
        df_cleaned = df_cleaned.dropna()
    elif strategy == "mean":
        df_cleaned = df_cleaned.fillna(df_cleaned.mean(numeric_only=True))
    elif strategy == "median":
        df_cleaned = df_cleaned.fillna(df_cleaned.median(numeric_only=True))
    elif strategy == "mode":
        df_cleaned = df_cleaned.fillna(df_cleaned.mode().iloc[0])
    elif strategy == "fill":
        df_cleaned = df_cleaned.fillna(fill_value)
    else:
        raise ValueError(
            f"Unknown strategy: {strategy}. Use 'drop', 'mean', 'median', 'mode', or 'fill'"
        )

    return df_cleaned


def detect_outliers(
    df: pd.DataFrame,
    method: str = "iqr",
    columns: Optional[List[str]] = None,
    threshold: float = 3.0,
) -> pd.DataFrame:
    """
    Detect outliers in DataFrame columns.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to analyze
    method : str, default 'iqr'
        Method to detect outliers: 'iqr' (Interquartile Range) or 'zscore'
    columns : List[str], optional
        List of column names to check. If None, uses all numeric columns.
    threshold : float, default 3.0
        Threshold for z-score method

    Returns
    -------
    pd.DataFrame
        DataFrame with boolean mask indicating outliers
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()

    outlier_mask = pd.DataFrame(False, index=df.index, columns=columns)

    for col in columns:
        if method == "iqr":
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outlier_mask[col] = (df[col] < lower_bound) | (
                df[col] > upper_bound
            )
        elif method == "zscore":
            z_scores = (df[col] - df[col].mean()) / df[col].std()
            outlier_mask[col] = abs(z_scores) > threshold
        else:
            raise ValueError(
                f"Unknown method: {method}. Use 'iqr' or 'zscore'"
            )

    return outlier_mask


def encode_categorical(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    method: str = "onehot",
) -> pd.DataFrame:
    """
    Encode categorical variables.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to process
    columns : List[str], optional
        List of column names to encode. If None, uses all categorical columns.
    method : str, default 'onehot'
        Encoding method: 'onehot', 'label', or 'ordinal'

    Returns
    -------
    pd.DataFrame
        DataFrame with encoded variables
    """
    df_encoded = df.copy()

    if columns is None:
        columns = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

    if method == "onehot":
        df_encoded = pd.get_dummies(
            df_encoded, columns=columns, drop_first=False
        )
    elif method == "label":
        from sklearn.preprocessing import LabelEncoder

        le = LabelEncoder()
        for col in columns:
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
    elif method == "ordinal":
        # For ordinal encoding, we'd need to specify the order of categories
        # This is just a placeholder implementation
        for col in columns:
            categories = df_encoded[col].unique()
            mapping = {category: i for i, category in enumerate(categories)}
            df_encoded[col] = df_encoded[col].map(mapping)
    else:
        raise ValueError(
            f"Unknown method: {method}. Use 'onehot', 'label', or 'ordinal'"
        )

    return df_encoded
