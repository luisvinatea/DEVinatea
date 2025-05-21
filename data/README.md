# Data Directory

This directory contains all data used in the analysis notebooks.

## Structure

- `raw/`: Original, immutable data dumps
- `interim/`: Intermediate data that has been transformed
- `processed/`: The final, canonical data sets for analysis

## Data Management Guidelines

1. **Raw Data**: Never edit raw data. If you need to clean it, create a notebook that reads from raw and writes to interim.
2. **Interim Data**: Use this for data in transition, temporary results, or intermediate processing steps.
3. **Processed Data**: Clean, transformed, ready-to-use datasets for analysis.

## Data Documentation

Each dataset should have accompanying documentation that describes:
- Source
- Variables/columns
- Collection methodology
- Preprocessing steps
- Any known issues or limitations
