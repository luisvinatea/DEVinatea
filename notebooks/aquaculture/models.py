"""Data models for aerator comparison analysis."""

from typing import NamedTuple


class Aerator(NamedTuple):
    """Aerator specification model."""

    name: str
    sotr: float  # Standard Oxygen Transfer Rate (kg O2/hour)
    power_hp: float  # Power consumption in HP
    cost: float  # Initial cost per unit
    durability: float  # Lifespan in years
    maintenance: float  # Annual maintenance cost per unit


class FarmInput(NamedTuple):
    """Farm parameters model."""

    tod: float  # Total Oxygen Demand (kg O2/hour/ha)
    farm_area_ha: float  # Farm area in hectares
    shrimp_price: float  # Price per kg of shrimp
    culture_days: float  # Days per culture cycle
    shrimp_density_kg_m3: float  # Shrimp density in kg/m³
    pond_depth_m: float  # Average pond depth in meters


class FinancialInput(NamedTuple):
    """Financial parameters model."""

    energy_cost: float  # Cost per kWh
    hours_per_night: float  # Operating hours per day
    discount_rate: float  # Discount rate for NPV calculations
    inflation_rate: float  # Inflation rate
    horizon: int  # Analysis horizon in years
    safety_margin: float  # Safety margin percentage for oxygen requirements
    temperature: float  # Water temperature in Celsius


class AeratorResult(NamedTuple):
    """Complete aerator analysis results."""

    name: str
    num_aerators: float
    total_power_hp: float
    total_initial_cost: float
    annual_energy_cost: float
    annual_maintenance_cost: float
    annual_replacement_cost: float
    total_annual_cost: float
    cost_percent_revenue: float
    npv_savings: float
    payback_years: float
    roi_percent: float
    irr: float
    profitability_k: float
    aerators_per_ha: float
    hp_per_ha: float
    sae: float  # Standard Aeration Efficiency
    cost_per_kg_o2: float
    opportunity_cost: float
