"""Configuration constants for financial analysis visualizations."""

# Physical constants
THETA = 1.024
HP_TO_KW = 0.745699872

# Default aerator specifications
DEFAULT_AERATOR_DATA = {
    "SOTR = 1.0": {
        "name": "Baseline Aerator",
        "sotr": 1.0,
        "total_investment": 500000,
        "total_annual_cost": 0.2,
    },
    "Aerator 1 (SOTR = 1.5)": {
        "name": "Mid-efficiency Aerator",
        "sotr": 1.5,
        "total_investment": 600000,
        "total_annual_cost": 0.15,
    },
    "Aerator 2 (SOTR = 3.0)": {
        "name": "High-efficiency Aerator",
        "sotr": 3.0,
        "total_investment": 800000,
        "total_annual_cost": 0.08,
    },
}

# Financial analysis parameters
FINANCIAL_PARAMS = {
    "inflation_rate": 0.025,
    "nominal_rate": 0.08,
    "analysis_horizon": 10,
    "energy_cost_factor": 2000,
    "price_per_kwh": 0.05,
    "hours_operation_per_day": 8,
    "fixed_power_kw": 2.238,
}

# Farm parameters
FARM_PARAMS = {
    "tod": 5443.76,  # Total Oxygen Demand (kg O₂/hour)
    "farm_size_ha": 1000,
    "temp": 31.5,
    "aeration_hours_per_day": 8,
}

# Visualization parameters
VIZ_PARAMS = {
    "figure_dpi": 100,
    "savefig_dpi": 300,
    "style": "whitegrid",
    "context": "talk",
    "font_scale": 1.1,
}

# Color schemes
COLOR_SCHEMES = {
    "primary": "husl",
    "heatmap": [
        "#d73027",
        "#f46d43",
        "#fdae61",
        "#fee08b",
        "#d9ef8b",
        "#a6d96a",
        "#66bd63",
        "#1a9850",
    ],
    "interpretation": {
        "Highly attractive": "#2E8B57",
        "Very attractive": "#32CD32",
        "Attractive": "#FFD700",
        "Moderately attractive": "#FFA500",
        "Marginally attractive": "#FF6347",
        "Unattractive": "#DC143C",
    },
}
