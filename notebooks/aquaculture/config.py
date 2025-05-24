"""Configuration constants for financial analysis visualizations."""

# Physical constants
THETA = 1.024
HP_TO_KW = 0.745699872

# Default aerator specifications (enhanced with comprehensive data)
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

# Sample aerator specifications for comparison
SAMPLE_AERATORS = [
    {
        "name": "Standard Paddle Wheel",
        "sotr": 1.9,
        "power_hp": 3.0,
        "cost": 700,
        "durability": 2.0,
        "maintenance": 65,
    },
    {
        "name": "High-Efficiency Aerator",
        "sotr": 3.5,
        "power_hp": 3.0,
        "cost": 900,
        "durability": 5.0,
        "maintenance": 50,
    },
    {
        "name": "Mid-Range Aerator",
        "sotr": 2.8,
        "power_hp": 2.5,
        "cost": 800,
        "durability": 3.0,
        "maintenance": 55,
    },
    {
        "name": "Economy Aerator",
        "sotr": 1.5,
        "power_hp": 2.8,
        "cost": 600,
        "durability": 1.5,
        "maintenance": 70,
    },
]

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

# Farm parameters (enhanced with comprehensive aquaculture data)
FARM_PARAMS = {
    "tod": 5443.76,  # Total Oxygen Demand (kg O₂/hour)
    "farm_size_ha": 1000,
    "temp": 31.5,
    "aeration_hours_per_day": 8,
    "shrimp_price": 5.0,  # $/kg
    "culture_days": 120,
    "shrimp_density_kg_m3": 0.333,
    "pond_depth_m": 1.0,
}

# Sample farm configurations for testing
SAMPLE_FARMS = {
    "small_intensive": {
        "tod": 2.73,
        "farm_area_ha": 50,
        "shrimp_price": 6.0,
        "culture_days": 110,
        "shrimp_density_kg_m3": 0.5,
        "pond_depth_m": 1.2,
    },
    "large_extensive": {
        "tod": 1.82,
        "farm_area_ha": 2000,
        "shrimp_price": 4.5,
        "culture_days": 130,
        "shrimp_density_kg_m3": 0.2,
        "pond_depth_m": 0.8,
    },
    "medium_semi_intensive": {
        "tod": 5.47,
        "farm_area_ha": 500,
        "shrimp_price": 5.5,
        "culture_days": 120,
        "shrimp_density_kg_m3": 0.35,
        "pond_depth_m": 1.0,
    },
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
