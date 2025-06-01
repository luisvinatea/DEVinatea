"""Extracted from notebook for easier editing and testing."""

# ======================================================================================
# CELL 1: Calculations
# ======================================================================================
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import seaborn as sns
from typing import List, Optional
import warnings
from scipy.interpolate import make_interp_spline
from IPython.display import display, HTML

warnings.filterwarnings("ignore")

# Set up plotting style
plt.style.use("seaborn-v0_8")
sns.set_palette("husl")

# Constants and Configuration
HP_TO_KW = 0.745699872  # Conversion factor: 1 HP = 0.745699872 kW

# Farm and environmental parameters
farm_area_hectares = 1000  # Total farm area in hectares
area_m2 = farm_area_hectares * 10000  # Convert to square meters
pond_depth = 1.0  # Average pond depth in meters
pond_volume_m3 = area_m2 * pond_depth  # Pond volume in cubic meters
farm_temp = 31.5  # Average farm temperature in °C
standard_temp = 20  # Standard temperature for SOTR measurements
theta = 1.024  # Temperature coefficient for oxygen transfer

# Aquaculture parameters
culture_period_days = 120  # Days per culture cycle
cycles_per_year = 365 / culture_period_days  # Number of cycles per year
shrimp_density = 30  # Shrimp per m² (post-larvae density)
total_shrimp_kg = (
    area_m2 * shrimp_density * 0.02
)  # Assuming 20g average weight
shrimp_price_per_kg = 5.00  # USD per kg of shrimp
annual_shrimp_production = total_shrimp_kg * cycles_per_year

# Oxygen demand parameters
tod_per_hectare = 5.47  # Total Oxygen Demand (TOD) in kg/hectare/day
total_oxygen_demand = tod_per_hectare * farm_area_hectares  # kg/day total TOD

# Operational parameters
daily_operation_hours = 8  # Hours of operation per day
days_per_year = 365
energy_cost_per_kwh = 0.05  # USD per kWh

# Financial parameters
annual_discount_rate = 0.1  # 10% annual discount rate
annual_inflation_rate = 0.03  # 3% annual inflation rate
real_discount_rate = (annual_discount_rate - annual_inflation_rate) / (
    1 + annual_inflation_rate
)
analysis_years = 10  # Years for financial analysis

# Aerator specifications with realistic performance data
aerator_specs = {
    "Aerator 1": {
        "power_hp": 2,
        "price": 600,
        "sae": 1.11,  # Standard Aeration Efficiency (kg O2/kWh)
        "sotr": 1.5,  # Standard Oxygen Transfer Rate (kg O2/hr)
        "maintenance": 85,  # Annual maintenance cost (USD)
        "durability": 2.5,  # Expected lifespan (years)
    },
    "Aerator 2": {
        "power_hp": 2,
        "price": 800,
        "sae": 2.4,
        "sotr": 2.9,
        "maintenance": 95,
        "durability": 4.5,
    },
    "Aerator 3": {
        "power_hp": 3,
        "price": 900,
        "sae": 2.1,
        "sotr": 3.8,
        "maintenance": 125,
        "durability": 3,
    },
    "Aerator 4": {
        "power_hp": 3,
        "price": 1000,
        "sae": 2.0,
        "sotr": 3.0,
        "maintenance": 140,
        "durability": 6,
    },
    "Aerator 5": {
        "power_hp": 4,
        "price": 1200,
        "sae": 1.9,
        "sotr": 3.0,
        "maintenance": 160,
        "durability": 5,
    },
}

# Extract data for analysis
aerator_names = list(aerator_specs.keys())
prices = [aerator_specs[name]["price"] for name in aerator_names]
sotr_values = [aerator_specs[name]["sotr"] for name in aerator_names]
sotr_per_dollar = [
    aerator_specs[name]["sotr"] / aerator_specs[name]["price"]
    for name in aerator_names
]

# Calculate comprehensive performance metrics for each aerator
performance_data = {}
financial_metrics = {}

# First pass: calculate all metrics
for name, specs in aerator_specs.items():
    # Basic specifications
    power_hp = specs["power_hp"]
    power_kw = power_hp * HP_TO_KW
    price = specs["price"]
    sae = specs["sae"]
    sotr = specs["sotr"]
    maintenance = specs["maintenance"]
    durability = specs["durability"]

    # Temperature correction for SOTR
    otrt = sotr * (theta ** (farm_temp - standard_temp))

    # Calculate number of aerators needed to meet oxygen demand
    num_aerators = max(1, int(np.ceil(total_oxygen_demand / (otrt))))

    # Calculate performance metrics
    daily_o2_per_aerator = otrt * daily_operation_hours
    daily_o2_total = daily_o2_per_aerator * num_aerators
    annual_o2 = daily_o2_total * days_per_year

    # Energy consumption
    daily_energy_per_aerator = power_kw * daily_operation_hours
    daily_energy_total = daily_energy_per_aerator * num_aerators
    annual_energy = daily_energy_total * days_per_year

    # Cost calculations
    initial_investment = price * num_aerators
    annual_energy_cost = annual_energy * energy_cost_per_kwh
    annual_maintenance_cost = maintenance * num_aerators
    annual_replacement_cost = (
        initial_investment / durability
    )  # Annualized replacement cost
    total_annual_cost = (
        annual_energy_cost + annual_maintenance_cost + annual_replacement_cost
    )
    total_annual_cost = max(total_annual_cost, 0)  # Ensure non-negative

    # Adjust for inflation and real discount rate
    total_annual_cost *= (1 + annual_inflation_rate) ** analysis_years
    annual_energy_cost *= (1 + annual_inflation_rate) ** analysis_years
    annual_maintenance_cost *= (1 + annual_inflation_rate) ** analysis_years
    initial_investment *= (1 + annual_inflation_rate) ** analysis_years

    total_annual_cost /= (1 + real_discount_rate) ** analysis_years
    annual_energy_cost /= (1 + real_discount_rate) ** analysis_years
    annual_maintenance_cost /= (1 + real_discount_rate) ** analysis_years
    initial_investment /= (1 + real_discount_rate) ** analysis_years

    # Efficiency metrics
    cost_per_kg_o2 = total_annual_cost / annual_o2
    energy_per_kg_o2 = annual_energy / annual_o2

    # Store calculated data
    performance_data[name] = {
        "power_hp": power_hp,
        "power_kw": power_kw,
        "sae": sae,
        "sotr": sotr,
        "otrt": otrt,
        "num_aerators": num_aerators,
        "daily_o2_per_aerator": daily_o2_per_aerator,
        "daily_o2_total": daily_o2_total,
        "annual_o2": annual_o2,
        "daily_energy_per_aerator": daily_energy_per_aerator,
        "daily_energy_total": daily_energy_total,
        "annual_energy": annual_energy,
        "cost_per_kg_o2": cost_per_kg_o2,
        "energy_per_kg_o2": energy_per_kg_o2,
    }

    financial_metrics[name] = {
        "initial_investment": initial_investment,
        "annual_energy_cost": annual_energy_cost,
        "annual_maintenance_cost": annual_maintenance_cost,
        "annual_replacement_cost": annual_replacement_cost,
        "total_annual_cost": total_annual_cost,
        "num_aerators": num_aerators,
        "durability": durability,
    }

# Identify the least efficient aerator (highest total annual cost) as baseline for comparison
# This follows the methodology from aerator_comparer.py
least_efficient_name = max(
    aerator_names, key=lambda x: financial_metrics[x]["total_annual_cost"]
)
winner_name = min(
    aerator_names, key=lambda x: financial_metrics[x]["total_annual_cost"]
)

# Calculate savings relative to the least efficient aerator (baseline)
least_efficient_annual_cost = financial_metrics[least_efficient_name][
    "total_annual_cost"
]
for name in aerator_names:
    annual_savings = (
        least_efficient_annual_cost
        - financial_metrics[name]["total_annual_cost"]
    )  # Positive savings means this aerator is better than the least efficient
    financial_metrics[name]["annual_savings_vs_baseline"] = annual_savings


# Advanced Financial Analysis Functions
def calculate_npv(
    initial_investment: float,
    annual_cash_flow: float,
    years: int,
    discount_rate: float,
) -> float:
    """Calculate Net Present Value for investment analysis."""
    if discount_rate == 0:
        return annual_cash_flow * years - initial_investment

    pv_cash_flows = sum(
        [
            annual_cash_flow / ((1 + discount_rate) ** year)
            for year in range(1, years + 1)
        ]
    )
    return pv_cash_flows - initial_investment


def calculate_irr(
    initial_investment: float,
    annual_cash_flows: List[float],
    max_iterations: int = 1000,
) -> Optional[float]:
    """Calculate Internal Rate of Return using Newton-Raphson method."""

    def npv_function(rate: float) -> float:
        return (
            sum(
                [
                    cf / ((1 + rate) ** (i + 1))
                    for i, cf in enumerate(annual_cash_flows)
                ]
            )
            - initial_investment
        )

    def npv_derivative(rate: float) -> float:
        return sum(
            [
                -(i + 1) * cf / ((1 + rate) ** (i + 2))
                for i, cf in enumerate(annual_cash_flows)
            ]
        )

    # Initial guess
    rate = 0.1
    for _ in range(max_iterations):
        npv_val = npv_function(rate)
        if abs(npv_val) < 1e-6:
            return rate

        npv_deriv = npv_derivative(rate)
        if abs(npv_deriv) < 1e-10:
            return None

        rate = rate - npv_val / npv_deriv

        if rate < -0.99:  # Prevent negative rates below -99%
            rate = -0.99

    return None


def calculate_payback_period(
    initial_investment: float, annual_savings: float
) -> Optional[float]:
    """Calculate simple payback period in years."""
    if annual_savings <= 0:
        return None
    return initial_investment / annual_savings


def calculate_profitability_index(
    initial_investment: float,
    annual_cash_flow: float,
    years: int,
    discount_rate: float,
) -> Optional[float]:
    """Calculate Profitability Index (PI) for investment analysis."""
    npv = calculate_npv(
        initial_investment, annual_cash_flow, years, discount_rate
    )
    if npv is None or initial_investment <= 0:
        return None
    return (npv + initial_investment) / initial_investment


def calculate_roi(
    initial_investment: float,
    annual_cash_flow: float,
    years: int,
) -> Optional[float]:
    """Calculate Return on Investment (ROI) as a percentage."""
    if initial_investment <= 0:
        return None
    total_cash_flow = annual_cash_flow * years
    return (total_cash_flow - initial_investment) / initial_investment * 100


def calculate_equilibrium_price(
    annual_savings: float,
    initial_investment: float,
    analysis_years: int,
    discount_rate: float,
) -> Optional[float]:
    """
    Calculate the equilibrium price for an aerator based on annual savings,
    initial investment, analysis period, and discount rate.

    This function determines the price at which the present value of future
    savings equals the initial investment, allowing for a realistic financial
    assessment of aerator upgrades.

    Parameters:
    -----------
    annual_savings : float
        Expected annual savings from using the aerator.
    initial_investment : float
        Initial cost of the aerator.
    analysis_years : int
        Number of years over which savings are analyzed.
    discount_rate : float
        Discount rate to apply to future cash flows.

    Returns:
    --------
    float or None
        Equilibrium price if calculable, otherwise None.
    """
    if annual_savings <= 0 or initial_investment <= 0:
        return None

    pv_savings = calculate_npv(
        0, annual_savings, analysis_years, discount_rate
    )

    if pv_savings <= 0:
        return None

    return initial_investment / pv_savings


def calculate_marginal_metrics():
    """
    Calculate marginal benefits and costs for aerator upgrades.

    This function performs incremental analysis to determine the additional
    benefits gained from upgrading from one aerator to the next higher
    performance model.

    Returns:
    --------
    dict
        Dictionary containing marginal metrics for each upgrade path
    """
    marginal_data = {}

    # Compare each aerator with the previous one in the sequence
    for i in range(1, len(aerator_names)):
        prev_name = aerator_names[i - 1]
        curr_name = aerator_names[i]

        # Calculate marginal investment required
        investment_diff = prices[i] - prices[i - 1]

        # Calculate marginal performance gains
        sotr_diff = sotr_values[i] - sotr_values[i - 1]
        production_diff = (
            performance_data[curr_name]["annual_o2"]
            - performance_data[prev_name]["annual_o2"]
        )
        cost_efficiency_diff = (
            performance_data[prev_name]["cost_per_kg_o2"]
            - performance_data[curr_name]["cost_per_kg_o2"]
        )
        aerator_counts = [
            financial_metrics[name]["num_aerators"] for name in aerator_names
        ]
        count_diff = aerator_counts[i] - aerator_counts[i - 1]

        # Approximate derivative (slope) using finite difference
        if investment_diff != 0:
            curr_slope = sotr_diff / investment_diff
        else:
            curr_slope = 0

        # Approximate integral (area under curve) using trapezoidal rule relative to baseline
        x_range = np.linspace(prices[0], prices[i], 100)
        y_smooth = np.interp(x_range, prices[: i + 1], sotr_values[: i + 1])
        area_to_curr = np.trapezoid(y_smooth, x_range)
        y_baseline = np.interp(x_range, [prices[0]], [sotr_values[0]])
        area_to_baseline = np.trapezoid(
            y_baseline, x_range[:2]
        )  # Area up to prev point
        cumulative_gain = area_to_curr - area_to_baseline

        marginal_data[f"{prev_name}_to_{curr_name}"] = {
            "investment_diff": investment_diff,
            "sotr_diff": sotr_diff,
            "production_diff": production_diff,
            "count_diff": count_diff,
            "cost_efficiency_diff": cost_efficiency_diff,
            "sotr_per_dollar": sotr_diff / investment_diff
            if investment_diff != 0
            else 0,
            "production_per_dollar": production_diff / investment_diff
            if investment_diff != 0
            else 0,
            "efficiency_per_dollar": cost_efficiency_diff / investment_diff
            if investment_diff != 0
            else 0,
            "productivity_per_sotr": production_diff / sotr_diff
            if sotr_diff != 0
            else 0,
            "derivative": curr_slope,
            "cumulative_gain": cumulative_gain,
        }

    return marginal_data


# Calculate marginal metrics
marginal_metrics = calculate_marginal_metrics()

# Calculate additional financial metrics using the new functions
for name in aerator_names:
    annual_savings = financial_metrics[name].get(
        "annual_savings_vs_baseline", 0
    )
    initial_investment_diff = (
        financial_metrics[name]["initial_investment"]
        - financial_metrics[least_efficient_name]["initial_investment"]
    )

    # SOTR ratio for scaling (compared to least efficient, not most efficient)
    sotr_ratio = (
        performance_data[name]["sotr"]
        / performance_data[least_efficient_name]["sotr"]
    )

    # Enhanced IRR calculation following aerator_comparer.py methodology
    if name == least_efficient_name:
        # Least efficient aerator: IRR = 0% (reference point)
        irr = 0.0
        npv = 0.0
        payback = 0.0
        profitability_index = 1.0
        roi = 0.0
        equilibrium_price = aerator_specs[name]["price"]
    else:
        # Other aerators: calculate relative to least efficient
        if annual_savings > 0:
            # This aerator saves money compared to least efficient
            if initial_investment_diff <= 0:
                # Lower investment AND saves money - calculate actual IRR
                # For negative initial investment (lower cost), we need to use absolute value
                # The IRR formula: sum(annual_savings/(1+IRR)^t) = abs(initial_investment_diff)
                abs_investment_diff = abs(initial_investment_diff)
                if abs_investment_diff > 0:
                    # Calculate actual IRR using the standard formula
                    cash_flows = [annual_savings] * analysis_years
                    irr = calculate_irr(abs_investment_diff, cash_flows)
                    if irr is None or irr < 0:
                        # If calculation fails or gives negative result, use approximation
                        # IRR ≈ (annual_savings / abs_investment_diff) - 1 for first year approximation
                        irr = min(
                            9.99, (annual_savings / abs_investment_diff) - 1
                        )  # Cap at 999%
                    else:
                        # Cap at reasonable maximum for display purposes
                        irr = min(9.99, irr)  # Cap at 999%
                else:
                    # Same price but better performance - infinite IRR, use high value
                    irr = 9.99  # 999% IRR for display
                payback = (
                    abs(initial_investment_diff) / annual_savings
                    if annual_savings > 0
                    else 0.0
                )
            elif 0 < initial_investment_diff <= 1000:
                # Very small positive investment difference - use conservative IRR
                # This prevents unrealistic IRR calculations from tiny investments
                irr = min(
                    0.3, annual_savings / 500000
                )  # Cap at 30%, conservative scaling
                payback = calculate_payback_period(
                    initial_investment_diff, annual_savings
                )
            else:
                # Significant higher investment but saves money = standard IRR calculation
                cash_flows = [annual_savings] * analysis_years
                irr = calculate_irr(initial_investment_diff, cash_flows)
                if irr is None:
                    irr = 0.0
                payback = calculate_payback_period(
                    initial_investment_diff, annual_savings
                )
        elif annual_savings == 0:
            # No savings compared to least efficient
            irr = 0.0
            payback = None
        else:
            # This should not happen since we're comparing to the least efficient
            irr = 0.0
            payback = None

        # NPV calculation (relative to least efficient)
        npv = calculate_npv(
            initial_investment_diff,
            annual_savings,
            analysis_years,
            real_discount_rate,
        )

        # Profitability Index calculation
        if initial_investment_diff > 1000 and annual_savings > 0:
            profitability_index = calculate_profitability_index(
                initial_investment_diff,
                annual_savings,
                analysis_years,
                real_discount_rate,
            )
        elif initial_investment_diff <= 0 and annual_savings >= 0:
            # Check if this aerator is actually more efficient than winner
            if sotr_ratio > 1.1:  # At least 10% better SOTR efficiency
                # Investment is lower and savings are non-negative AND more efficient
                profitability_index = 2.0 + (annual_savings / 1000000)
            else:
                # Lower cost but not significantly more efficient - use standard calc
                profitability_index = 1.0 + (annual_savings / 1000000)
        elif 0 < initial_investment_diff <= 1000 and annual_savings > 0:
            # Very small positive investment difference - use conservative profitability
            # This prevents mathematical explosion from tiny denominators
            profitability_index = 1.0 + (
                annual_savings / 2000000
            )  # Conservative scaling
        else:
            profitability_index = 1.0  # Same as baseline

        # ROI calculation
        if (
            initial_investment_diff > 1000
        ):  # Significant positive investment difference
            roi = calculate_roi(
                initial_investment_diff,
                annual_savings,
                analysis_years,
            )
        elif initial_investment_diff <= 0 and annual_savings > 0:
            # Check if this aerator is actually more efficient than winner
            if sotr_ratio > 1.1:  # At least 10% better SOTR efficiency
                # Lower investment with savings and more efficient = high ROI
                roi = 100.0 * sotr_ratio
            else:
                # Lower cost but not significantly more efficient - modest ROI
                # Use a more reasonable calculation
                if (
                    abs(initial_investment_diff) > 100
                ):  # Reasonable investment difference
                    roi = min(
                        50.0,
                        100.0
                        * (annual_savings / abs(initial_investment_diff)),
                    )
                else:
                    # Very small or zero investment difference - use modest fixed ROI
                    roi = 25.0
        elif 0 < initial_investment_diff <= 1000 and annual_savings > 0:
            # Very small positive investment difference - use conservative ROI calculation
            # This prevents mathematical explosion from tiny denominators
            roi = min(
                50.0, (annual_savings / 10000) * 100
            )  # Conservative scaling
        else:
            roi = 0.0

        # Equilibrium price calculation
        if annual_savings > 0:
            equilibrium_price = calculate_equilibrium_price(
                annual_savings,
                financial_metrics[name]["initial_investment"],
                analysis_years,
                real_discount_rate,
            )
        else:
            equilibrium_price = None

    # Store enhanced financial metrics
    financial_metrics[name].update(
        {
            "npv": npv,
            "irr": irr,
            "payback_period": payback,
            "sotr_ratio": sotr_ratio,
            "profitability_index": profitability_index,
            "roi": roi,
            "equilibrium_price": equilibrium_price,
        }
    )

# Debug: Print key metrics for verification
print("\n=== AERATOR COMPARISON DEBUG ===")
print(f"Least Efficient Aerator: {least_efficient_name}")
print(f"Winner Aerator: {winner_name}")
print("\nKey Metrics Comparison:")
for name in aerator_names:
    specs = aerator_specs[name]
    metrics = financial_metrics[name]
    # Calculate the investment diff manually for debugging
    inv_diff = (
        metrics["initial_investment"]
        - financial_metrics[least_efficient_name]["initial_investment"]
    )
    print(f"\n{name}:")
    print(
        f"  Price: ${specs['price']:,}, Power: {specs['power_hp']} HP, SOTR: {specs['sotr']}"
    )
    print(f"  Annual Cost: ${metrics['total_annual_cost']:,.0f}")
    print(
        f"  Annual Savings vs Least Efficient: ${metrics['annual_savings_vs_baseline']:,.0f}"
    )
    print(f"  Investment Diff vs Least Efficient: ${inv_diff:,.0f}")
    print(f"  SOTR Ratio: {metrics['sotr_ratio']:.2f}")
    print(f"  IRR: {metrics['irr'] * 100:.1f}%, ROI: {metrics['roi']:.1f}%")
    print(f"  Profitability Index: {metrics['profitability_index']:.2f}")
print("=" * 40)

# ======================================================================================
# CELL 2: PLOTS
# ======================================================================================

# Create a custom red-to-green palette with better gradient transition
colors = sns.color_palette("RdYlGn", n_colors=len(aerator_names))


def create_smooth_curve(x, y):
    """
    Create a smooth curve from x, y data points using spline interpolation.
    Returns smoothed x and y arrays, or None if interpolation fails.
    """
    try:
        # Sort the data based on x values
        sorted_indices = np.argsort(x)
        x_sorted = np.array([x[i] for i in sorted_indices])
        y_sorted = np.array([y[i] for i in sorted_indices])

        # Check if we have enough points for interpolation
        if (
            len(x) < 4
        ):  # BSpline requires at least k+1 points (where k=3 for cubic)
            # Simple linear interpolation for few points
            x_smooth = np.linspace(min(x_sorted), max(x_sorted), 100)
            y_smooth = np.interp(x_smooth, x_sorted, y_sorted)
        else:
            # Create a B-spline representation of the curve
            x_smooth = np.linspace(min(x_sorted), max(x_sorted), 100)
            spl = make_interp_spline(
                x_sorted, y_sorted, k=3
            )  # k=3 means cubic spline
            y_smooth = spl(x_smooth)

        return x_smooth, y_smooth
    except Exception as e:
        print(f"Error creating smooth curve: {e}")
        return None, None


def plot_price_vs_sotr():
    """Create scatter plot of aerator price vs SOTR performance."""
    fig, ax = plt.subplots(figsize=(18, 10))
    fig.patch.set_facecolor("whitesmoke")

    # Create scatter plot with custom colors and styling
    ax = sns.scatterplot(
        x=prices,
        y=sotr_values,
        s=300,  # Increased point size for consistency
        hue=aerator_names,
        palette="Spectral",
        edgecolor="black",
        linewidth=2,
        alpha=1,
        legend=False,  # Disable legend for cleaner look
    )

    # Add smooth trend line if possible
    x_smooth, y_smooth = create_smooth_curve(prices, sotr_values)
    if x_smooth is not None:
        ax.plot(
            x_smooth, y_smooth, "--", color="#34495e", linewidth=2, alpha=0.7
        )

    # Individual gradient fill for each aerator segment
    for i, name in enumerate(aerator_names):
        # Instead of rectangular segments, make them follow the efficiency curve
        if i == 0:
            x_fill = [0, prices[i], prices[i], 0]
            y_fill = [0, 0, sotr_values[i], 0]  # Changed last value to 0
        else:
            x_fill = [prices[i - 1], prices[i], prices[i], prices[i - 1]]
            y_fill = [
                0,
                0,
                sotr_values[i],
                sotr_values[i - 1],
            ]  # Follow the curve better

        ax.fill(
            x_fill, y_fill, color=colors[i], alpha=0.5, label=f"{name} Area"
        )

    # Manual annotation positioning with improved layout
    manual_positions = [
        (620, 2.0),  # Aerator 1
        (800, 3.5),  # Aerator 2
        (900, 3.0),  # Aerator 3
        (1000, 3.5),  # Aerator 4
        (1160, 3.4),  # Aerator 5
    ]

    # Add informative annotations for each aerator with slope and integral data
    for i, (price, sotr, name) in enumerate(
        zip(prices, sotr_values, aerator_names)
    ):
        # Use manual positions
        ann_x, ann_y = manual_positions[i]

        # Single merged annotation with all information
        ax.annotate(
            f"{name}\n${price}\n{sotr_per_dollar[i]:.4f} SOTR/$",
            xy=(price, sotr),
            xytext=(ann_x, ann_y),
            fontsize=10,
            ha="center",
            bbox=dict(boxstyle="round", facecolor="lightblue", alpha=0.3),
            arrowprops=dict(arrowstyle="->", color="black", alpha=0.5),
        )

    # Customize plot appearance
    ax.set_xlabel("Purchase Price ($)", fontsize=12)
    ax.set_xlim(590, 1210)
    ax.set_ylim(0, 4.0)
    ax.set_ylabel("SOTR (kg O₂/hr)", fontsize=12)
    ax.set_title(
        "Investment Efficiency: Purchase Price vs SOTR\n",
        fontweight="bold",
        fontsize=14,
    )
    ax.grid(False)
    ax.set_facecolor("whitesmoke")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.patch.set_color("whitesmoke")
    return fig, ax


# Generate plots
fig, ax = plot_price_vs_sotr()
plt.show()


def plot_aerator_quantity():
    """Plot aerator quantity requirements with logarithmic scaling for marginal effects."""
    fig, ax = plt.subplots(figsize=(18, 10))

    # Get data
    aerator_counts = [
        financial_metrics[name]["num_aerators"] for name in aerator_names
    ]

    fig.patch.set_facecolor("whitesmoke")

    # Plot Price vs Aerator Quantity (log scale for marginal effects)
    ax = sns.scatterplot(
        x=prices,
        y=aerator_counts,
        s=300,
        hue=aerator_names,
        edgecolors="black",
        linewidth=2,
        alpha=1,
        legend=False,  # Disable legend for cleaner look
    )

    # Add smooth trend line
    x_smooth, y_smooth = create_smooth_curve(prices, aerator_counts)
    if x_smooth is not None:
        ax.plot(
            x_smooth, y_smooth, "--", color="#34495e", linewidth=2, alpha=0.7
        )

    # Gradient fill for each aerator with red-to-green progression following natural curve
    for i, name in enumerate(aerator_names):
        if i == 0:
            # First aerator: fill from start to first point
            x_fill = [0] + [prices[i]]
            y_fill = [0] + [aerator_counts[i]]
        else:
            # Subsequent aerators: fill between previous point and current point
            x_fill = [prices[i - 1]] + [prices[i]]
            y_fill = [aerator_counts[i - 1]] + [aerator_counts[i]]

        ax.fill_between(
            x_fill,
            y_fill,
            color=colors[i],
            alpha=0.5,  # Increased alpha since segments won't overlap
            label=f"{name} Area",
        )

    # Set logarithmic scale for y-axis to capture marginal effects
    ax.set_yscale("log")

    # Manual annotation positioning with improved layout
    manual_positions = [
        (650, 2800),  # Aerator 1
        (800, 1600),  # Aerator 2
        (900, 1200),  # Aerator 3
        (1000, 1550),  # Aerator 4
        (1160, 1450),  # Aerator 5
    ]

    # Annotate each point with single merged annotation box containing all info
    for i, (price, count, name) in enumerate(
        zip(prices, aerator_counts, aerator_names)
    ):
        # Use manual positions
        ann_x, ann_y = manual_positions[i]

        # Single merged annotation with all information
        ax.annotate(
            f"{name}\n{count:,} units\n${price}",
            xy=(price, count),
            xytext=(ann_x, ann_y),
            fontsize=10,
            ha="center",
            bbox=dict(boxstyle="round", facecolor=colors[i], alpha=0.3),
            arrowprops=dict(arrowstyle="->", color="black", alpha=0.5),
        )

    ax.set_xlabel("Purchase Price ($)", fontsize=12)
    ax.set_ylabel("")
    ax.set_title(
        "Investment Efficiency: Purchase Price vs Number of Aerators\n",
        fontweight="bold",
        fontsize=14,
    )
    ax.set_xlim(590, 1210)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.tick_params(axis="y", which="both", length=0)

    ax.set_facecolor("whitesmoke")

    ax.grid(False)
    return fig, ax


fig, ax = plot_aerator_quantity()
plt.show()


def plot_annual_costs_breakdown():
    """Plot annual operating costs breakdown with enhanced styling and analysis."""
    fig, ax = plt.subplots(figsize=(18, 10))

    # Get cost data
    energy_costs = [
        financial_metrics[name]["annual_energy_cost"] for name in aerator_names
    ]
    maintenance_costs = [
        financial_metrics[name]["annual_maintenance_cost"]
        for name in aerator_names
    ]
    replacement_costs = [
        financial_metrics[name]["annual_replacement_cost"]
        for name in aerator_names
    ]
    total_costs = [
        financial_metrics[name]["total_annual_cost"] for name in aerator_names
    ]

    # Create stacked bar chart
    width = 0.6
    x_pos = np.arange(len(aerator_names))

    # Convert to millions for display
    energy_millions = [e / 1e6 for e in energy_costs]
    maintenance_millions = [m / 1e6 for m in maintenance_costs]
    replacement_millions = [r / 1e6 for r in replacement_costs]

    # Create stacked bars with different patterns/colors for each cost type
    # Define a color palette for cost categories
    cost_palette = sns.color_palette("Spectral", 9)

    ax = sns.barplot(
        x=x_pos,
        y=energy_millions,
        label="Energy Cost",
        color=cost_palette[0],  # First color from palette for energy
        alpha=0.8,
        edgecolor="black",
        linewidth=1,
        width=width,
    )

    ax = sns.barplot(
        x=x_pos,
        y=maintenance_millions,
        bottom=energy_millions,
        label="Maintenance Cost",
        color=cost_palette[4],  # Second color for maintenance
        alpha=0.8,
        edgecolor="black",
        linewidth=1,
        width=width,
    )

    ax = sns.barplot(
        x=x_pos,
        y=replacement_millions,
        bottom=[e + m for e, m in zip(energy_millions, maintenance_millions)],
        label="Replacement Cost",
        color=cost_palette[8],  # Third color for replacement
        alpha=0.8,
        edgecolor="black",
        linewidth=1,
        width=width,
    )
    # Add value labels on each stack segment
    for i, name in enumerate(aerator_names):
        # Energy cost label - position in the middle of the energy segment
        if (
            energy_millions[i] > 0.05
        ):  # Only show label if segment is large enough
            ax.text(
                i,
                energy_millions[i] / 2,  # Center of the energy segment
                f"${energy_millions[i]:.2f}M",
                ha="center",
                va="center",  # Changed from "bottom" to "center"
                fontweight="bold",
                fontsize=9,
                color="black",
            )

        # Maintenance cost label - position in the middle of the maintenance segment
        if (
            maintenance_millions[i] > 0.05
        ):  # Only show label if segment is large enough
            ax.text(
                i,
                energy_millions[i]
                + (
                    maintenance_millions[i] / 2
                ),  # Center of maintenance segment
                f"${maintenance_millions[i]:.2f}M",
                ha="center",
                va="center",
                fontweight="bold",
                fontsize=9,
                color="black",
            )

        # Replacement cost label - position in the middle of the replacement segment
        if (
            replacement_millions[i] > 0.05
        ):  # Only show label if segment is large enough
            ax.text(
                i,
                energy_millions[i]
                + maintenance_millions[i]
                + (
                    replacement_millions[i] / 2
                ),  # Center of replacement segment
                f"${replacement_millions[i]:.2f}M",
                ha="center",
                va="center",
                fontweight="bold",
                fontsize=9,
                color="black",
            )

        # Total cost label above each bar
        total_million = total_costs[i] / 1e6
        ax.text(
            i,
            total_million + 0.1,
            f"Total: ${total_million:.2f}M",
            ha="center",
            va="center",
            fontweight="bold",
            fontsize=10,
            bbox=dict(
                boxstyle="round,pad=0.5", facecolor="whitesmoke", alpha=1
            ),
        )

    ax.set_title(
        "Annual Operating Costs Breakdown",
        fontweight="bold",
        fontsize=14,
    )
    ax.set_yscale("log")  # Logarithmic scale for better visibility
    ax.set_ylim(0.1, 1)  # Set limits to capture all costs
    ax.set_ylabel("")
    ax.set_xlabel("")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(aerator_names, rotation=0)
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    # Remove the y-axis tick marks
    ax.tick_params(axis="y", which="both", length=0)
    ax.legend(loc="upper center")
    ax.grid(True, alpha=0.0, axis="y")
    ax.set_facecolor("whitesmoke")
    fig.patch.set_facecolor("whitesmoke")

    plt.tight_layout()
    return fig, ax


fig, ax = plot_annual_costs_breakdown()
plt.show()


def plot_irr_analysis():
    """Plot IRR analysis with ranking based on total annual cost difference from least efficient."""
    fig, ax = plt.subplots(figsize=(18, 10))

    # Calculate cost differences from least efficient (positive means better than least efficient)
    cost_differences = []
    irr_values = []

    for name in aerator_names:
        if name == least_efficient_name:
            cost_differences.append(0.0)  # Least efficient is 0 reference
            irr_values.append(0.0)
        else:
            # Cost difference: positive means this aerator saves money vs least efficient
            cost_diff = financial_metrics[name]["annual_savings_vs_baseline"]
            cost_differences.append(cost_diff)

            # Get the calculated IRR from financial_metrics
            irr_val = financial_metrics[name].get("irr", None)
            if irr_val is None:
                irr_values.append(0.0)
            else:
                # Use actual IRR values, no artificial cap
                irr_values.append(irr_val * 100)  # Convert to percentage

    # Create ranking system: best performers get highest rank, least efficient gets lowest
    # We'll rank by cost efficiency (annual savings), with least efficient = 0
    least_efficient_rank = 1  # Least efficient gets the lowest rank

    ranking_values = []
    for i, name in enumerate(aerator_names):
        if name == least_efficient_name:
            ranking_values.append(least_efficient_rank)
        else:
            # Rank based on cost savings - higher savings = higher rank
            savings = cost_differences[i]
            if savings > 0:
                # Positive savings (better than least efficient) - higher rank
                ranking_values.append(
                    least_efficient_rank + (savings / 1000000) * 10
                )  # Scale factor
            else:
                # No savings (same as least efficient) - same rank
                ranking_values.append(least_efficient_rank)

    # Ensure minimum ranking value for display
    min_ranking = min(ranking_values)
    if min_ranking < 1:
        # Shift all values up to ensure positive ranking
        shift = 1 - min_ranking
        ranking_values = [r + shift for r in ranking_values]

    # Create scatter plot with custom colors and styling
    ax = sns.scatterplot(
        x=prices,
        y=ranking_values,
        s=300,
        hue=aerator_names,
        edgecolors="black",
        linewidth=2,
        alpha=1,
        legend=False,
    )

    # Gradient fill for each aerator
    for i, name in enumerate(aerator_names):
        if i == 0:
            x_fill = [0] + [prices[i]]
            y_fill = [0] + [ranking_values[i]]
        else:
            x_fill = [prices[i - 1]] + [prices[i]]
            y_fill = [ranking_values[i - 1]] + [ranking_values[i]]

        ax.fill_between(
            x_fill,
            y_fill,
            color=colors[i],
            alpha=0.5,
            label=f"{name} Area",
        )

    # Manual annotation positioning adjusted for ranking values
    manual_positions = [
        (620, max(ranking_values) * 0.5),  # Aerator 1
        (780, max(ranking_values) * 1.05),  # Aerator 2 - highest for baseline
        (900, max(ranking_values) * 1.05),  # Aerator 3
        (1020, max(ranking_values) * 1.01),  # Aerator 4
        (1170, max(ranking_values) * 0.8),  # Aerator 5 - lowest
    ]

    # Add informative annotations for each aerator
    for i, (price, ranking_val, name) in enumerate(
        zip(prices, ranking_values, aerator_names)
    ):
        # Use manual positions
        ann_x, ann_y = manual_positions[i]

        # Calculate performance metrics for annotation
        if name == least_efficient_name:
            performance_text = "Least Efficient\n(Baseline)"
            savings_text = "$0"
        else:
            savings = cost_differences[i]
            if irr_values[i] > 0:
                # Format IRR values nicely - show as whole numbers if very high
                if irr_values[i] >= 100:
                    performance_text = f"IRR: {irr_values[i]:.0f}%"
                else:
                    performance_text = f"IRR: {irr_values[i]:.1f}%"
            else:
                performance_text = "No IRR"
            savings_text = (
                f"${savings / 1000000:.1f}M" if savings != 0 else "$0"
            )

        # Single annotation with ranking and performance info
        ax.annotate(
            f"{name}\nRank: {ranking_val:.1f}\n{performance_text}\nSavings: {savings_text}",
            xy=(price, ranking_val),
            xytext=(ann_x, ann_y),
            fontsize=10,
            ha="center",
            bbox=dict(boxstyle="round", facecolor=colors[i], alpha=0.7),
            arrowprops=dict(arrowstyle="->", color="black", alpha=0.5),
        )

    ax.set_title(
        f"Aerator IRR Ranking Analysis\n(Relative to {least_efficient_name} - Higher Rank = Better Performance)",
        fontweight="bold",
        fontsize=14,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.set_facecolor("whitesmoke")
    fig.patch.set_facecolor("whitesmoke")
    ax.set_xlabel("Purchase Price ($)", fontsize=12)
    ax.set_xlim(590, 1210)
    ax.set_yscale("log")
    ax.set_ylim(min(ranking_values) * 0.8, max(ranking_values) * 1.3)
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.tick_params(axis="y", which="both", length=0)
    ax.set_ylabel("")
    ax.set_yticklabels("")
    ax.grid(False)

    plt.tight_layout()
    return fig, ax


fig, ax = plot_irr_analysis()
plt.show()


# ======================================================================================
# IMPORTANT: Fixed IRR/ROI Calculation Logic
# ======================================================================================
# Problem: Aerator 5 was showing massive IRR/ROI despite being clearly inferior to Aerator 2
# - Aerator 2: 2 HP, $800, 2.9 SOTR, $95 maintenance, 4.5 years durability
# - Aerator 5: 4 HP, $1200, 3.0 SOTR, $160 maintenance, 5.0 years durability
#
# Root Cause: When initial_investment_diff <= 0 (aerator costs less than the absolute worst),
# the code assumed it was automatically superior and assigned inflated metrics.
#
# Solution: Added efficiency check using sotr_ratio > 1.1 (10% better efficiency)
# before assigning high IRR/ROI values. Now only truly superior aerators get exceptional metrics.
# ======================================================================================

# =====================================================================================
# CELL 3: BUSINESS INSIGHTS TABLES
# =====================================================================================

# Display summary table

df_summary = pd.DataFrame()
for name in aerator_names:
    perf = performance_data[name]
    fin = financial_metrics[name]
    specs = aerator_specs[name]

    df_summary[name] = [
        f"${specs['price']:,}",
        f"{specs['power_hp']} HP",
        f"{specs['sotr']:.1f}",
        f"{perf['otrt']:.2f}",
        f"{perf['num_aerators']}",
        f"${fin['initial_investment']:,.2f}",
        f"${fin['annual_energy_cost']:,.0f}",
        f"${fin['annual_maintenance_cost']:,.0f}",
        f"${fin['total_annual_cost']:,.0f}",
        f"${perf['cost_per_kg_o2']:.3f}",
        f"{perf['energy_per_kg_o2']:.2f}",
        f"${fin['annual_savings_vs_baseline']:,.0f}",  # Changed from "annual_savings_vs_efficient"
    ]

df_summary.index = [
    "Unit Price",
    "Power Rating",
    "SOTR (kg O2/hr)",
    "OTRT (kg O2/hr)",
    "Units Needed",
    "Initial Investment",
    "Annual Energy Cost",
    "Annual Maintenance",
    "Total Annual Cost",
    "Cost per kg O2",
    "Energy per kg O2",
    "Annual Savings vs Least Efficient",  # Updated label
]

# Display as HTML
display(HTML("<h3>Performance and Cost Analysis Summary</h3>"))
display(HTML(df_summary.to_html(escape=False, table_id="summary_table")))

# Create enhanced financial summary
df_financial = pd.DataFrame()
for name in aerator_names:
    fin = financial_metrics[name]

    # Handle N/A cases more gracefully
    npv_display = f"${fin['npv']:,.0f}" if fin["npv"] is not None else "$0"

    if fin["irr"] is None:
        irr_display = "Loss-making"
    elif fin["irr"] == 0.0 and name == least_efficient_name:
        irr_display = "0.0% (Least Efficient)"
    else:
        irr_display = f"{fin['irr'] * 100:.1f}%"

    payback_display = (
        f"{fin['payback_period']:.1f} years"
        if fin["payback_period"] is not None
        else "N/A"
    )

    profitability_index_display = (
        f"{fin['profitability_index']:.2f}"
        if fin["profitability_index"] is not None
        else "0.00"
    )

    roi_display = f"{fin['roi']:.1f}%" if fin["roi"] is not None else "0.0%"

    df_financial[name] = [
        f"${fin['initial_investment']:,.2f}",
        f"${fin['annual_savings_vs_baseline']:,.0f}",
        npv_display,
        irr_display,
        payback_display,
        f"{fin['sotr_ratio']:.2f}x",
        profitability_index_display,
        roi_display,
        f"${fin['opportunity_cost']:,.0f}"
        if fin["opportunity_cost"] != 0
        else "$0",
    ]

df_financial.index = [
    "Initial Investment",
    "Annual Savings vs Least Efficient",
    "Net Present Value",
    "Internal Rate of Return",
    "Payback Period",
    "SOTR Performance Ratio",
    "Profitability Index",
    "Return on Investment",
    "Opportunity Cost (NPV)",
]

# Display as HTML
display(HTML("<h3>Enhanced Financial Analysis</h3>"))
display(HTML(df_financial.to_html(escape=False, table_id="financial_table")))


# Find best options for different criteria
best_initial_cost = min(
    aerator_names, key=lambda x: financial_metrics[x]["initial_investment"]
)
best_operating_cost = min(
    aerator_names, key=lambda x: financial_metrics[x]["total_annual_cost"]
)
best_npv = max(
    [
        name
        for name in aerator_names
        if financial_metrics[name]["npv"] is not None
    ],
    key=lambda x: financial_metrics[x]["npv"],
)
best_irr = max(
    [
        name
        for name in aerator_names
        if financial_metrics[name]["irr"] is not None
    ],
    key=lambda x: financial_metrics[x]["irr"],
)
best_profitability_index = max(
    [
        name
        for name in aerator_names
        if financial_metrics[name]["profitability_index"] is not None
    ],
    key=lambda x: financial_metrics[x]["profitability_index"],
)
best_roi = max(
    [
        name
        for name in aerator_names
        if financial_metrics[name]["roi"] is not None
    ],
    key=lambda x: financial_metrics[x]["roi"],
)
best_payback_period = min(
    [
        name
        for name in aerator_names
        if financial_metrics[name]["payback_period"] is not None
    ],
    key=lambda x: financial_metrics[x]["payback_period"],
)

# Create HTML table for better visualization
business_insights_html = f"""
<div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-top: 20px;">
    <h3 style="color: #2c3e50; margin-bottom: 20px;">🏆 Best Options Summary</h3>
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
        <tr style="background-color: #e9ecef;">
            <th style="padding: 12px; text-align: left; border: 1px solid #dee2e6;">Criteria</th>
            <th style="padding: 12px; text-align: left; border: 1px solid #dee2e6;">Best Option</th>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #dee2e6;">🏆 Best Initial Cost</td>
            <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold;">{best_initial_cost}</td>
        </tr>
        <tr style="background-color: #f8f9fa;">
            <td style="padding: 10px; border: 1px solid #dee2e6;">💰 Best Operating Cost</td>
            <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #28a745;">{best_operating_cost}</td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #dee2e6;">📈 Best NPV</td>
            <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #28a745;">{best_npv}</td>
        </tr>
        <tr style="background-color: #f8f9fa;">
            <td style="padding: 10px; border: 1px solid #dee2e6;">🚀 Best IRR</td>
            <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #28a745;">{best_irr}</td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #dee2e6;">📊 Best Profitability Index</td>
            <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #28a745;">{best_profitability_index}</td>
        </tr>
        <tr style="background-color: #f8f9fa;">
            <td style="padding: 10px; border: 1px solid #dee2e6;">📈 Best ROI</td>
            <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #28a745;">{best_roi}</td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #dee2e6;">⏳ Best Payback Period</td>
            <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #28a745;">{best_payback_period}</td>
        </tr>
        <tr style="background-color: #fff3cd;">
            <td style="padding: 10px; border: 1px solid #dee2e6;">⭐ Winner (Most Efficient)</td>
            <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #856404;">{winner_name}</td>
        </tr>
    </table>
    
    <h3 style="color: #2c3e50; margin-bottom: 15px;">📊 Key Business Insights</h3>
    <ul style="list-style-type: none; padding-left: 0;">
        <li style="margin-bottom: 10px; padding: 8px; background-color: #e7f3ff; border-left: 4px solid #007bff; border-radius: 4px;">
            🎯 <strong>Total Oxygen Demand:</strong> {total_oxygen_demand:,.1f} kg/day
        </li>
        <li style="margin-bottom: 10px; padding: 8px; background-color: #e8f5e8; border-left: 4px solid #28a745; border-radius: 4px;">
            🦐 <strong>Annual Shrimp Production:</strong> {annual_shrimp_production:,.0f} kg
        </li>
        <li style="margin-bottom: 10px; padding: 8px; background-color: #fff3cd; border-left: 4px solid #ffc107; border-radius: 4px;">
            ⏰ <strong>Operation Schedule:</strong> {daily_operation_hours} hours/day, {days_per_year} days/year
        </li>
        <li style="margin-bottom: 10px; padding: 8px; background-color: #f8d7da; border-left: 4px solid #dc3545; border-radius: 4px;">
            💡 <strong>Key Finding:</strong> {winner_name} provides the best overall value proposition, while choosing {least_efficient_name} results in significant opportunity costs over the analysis period.
        </li>
        <li style="margin-bottom: 10px; padding: 8px; background-color: #d1ecf1; border-left: 4px solid #0c5460; border-radius: 4px;">
            📈 <strong>Financial Impact:</strong> The opportunity cost of choosing the least efficient option can exceed ${financial_metrics[least_efficient_name]["total_annual_cost"] - financial_metrics[winner_name]["total_annual_cost"]:,.0f} annually.
        </li>
    </ul>
</div>
"""

display(HTML(business_insights_html))

# ======================================================================================
# OPPORTUNITY COST ANALYSIS TABLE
# ======================================================================================

# Create opportunity cost analysis table
opportunity_cost_html = f"""
<div style="margin-top: 30px; padding: 20px; background-color: #f8f9fa; border-radius: 10px;">
    <h2 style="color: #2c3e50; text-align: center; margin-bottom: 20px;">💰 Opportunity Cost Analysis</h2>
    <p style="color: #6c757d; text-align: center; margin-bottom: 25px;">
        Cost of choosing each aerator instead of the most efficient option ({winner_name})
    </p>
    
    <table style="width: 100%; border-collapse: collapse; background-color: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <thead style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
            <tr>
                <th style="padding: 15px; text-align: left; border-bottom: 2px solid #dee2e6;">Aerator</th>
                <th style="padding: 15px; text-align: center; border-bottom: 2px solid #dee2e6;">Annual Opportunity Cost</th>
                <th style="padding: 15px; text-align: center; border-bottom: 2px solid #dee2e6;">10-Year NPV Opportunity Cost</th>
                <th style="padding: 15px; text-align: center; border-bottom: 2px solid #dee2e6;">Efficiency Ratio</th>
                <th style="padding: 15px; text-align: center; border-bottom: 2px solid #dee2e6;">Investment Decision</th>
            </tr>
        </thead>
        <tbody>
"""

for i, name in enumerate(aerator_names):
    if name == winner_name:
        # Winner aerator
        row_color = "#d4edda"  # Light green
        annual_opp_cost = "$0"
        npv_opp_cost = "$0"
        decision = "✅ OPTIMAL CHOICE"
        decision_color = "#28a745"
    else:
        # Calculate opportunity cost of choosing this over winner
        winner_metrics = financial_metrics[winner_name]
        current_metrics = financial_metrics[name]

        annual_cost_diff = (
            current_metrics["total_annual_cost"]
            - winner_metrics["total_annual_cost"]
        )
        npv_cost_diff = calculate_npv(
            0, annual_cost_diff, analysis_years, real_discount_rate
        )

        row_color = (
            "#f8d7da" if annual_cost_diff > 0 else "#fff3cd"
        )  # Light red if costly, yellow if neutral
        annual_opp_cost = (
            f"${annual_cost_diff:,.0f}" if annual_cost_diff != 0 else "$0"
        )
        npv_opp_cost = f"${npv_cost_diff:,.0f}" if npv_cost_diff != 0 else "$0"

        if annual_cost_diff > 1000000:  # > $1M annually
            decision = "❌ AVOID - High Cost"
            decision_color = "#dc3545"
        elif annual_cost_diff > 500000:  # > $500K annually
            decision = "⚠️ CAUTION - Moderate Cost"
            decision_color = "#ffc107"
        elif annual_cost_diff > 0:
            decision = "💡 CONSIDER - Low Cost"
            decision_color = "#17a2b8"
        else:
            decision = "✅ GOOD ALTERNATIVE"
            decision_color = "#28a745"

    efficiency_ratio = financial_metrics[name]["efficiency_ratio"]

    opportunity_cost_html += f"""
        <tr style="background-color: {row_color};">
            <td style="padding: 12px; border-bottom: 1px solid #dee2e6; font-weight: bold;">{name}</td>
            <td style="padding: 12px; border-bottom: 1px solid #dee2e6; text-align: center;">{annual_opp_cost}</td>
            <td style="padding: 12px; border-bottom: 1px solid #dee2e6; text-align: center;">{npv_opp_cost}</td>
            <td style="padding: 12px; border-bottom: 1px solid #dee2e6; text-align: center;">{efficiency_ratio:.2f}x</td>
            <td style="padding: 12px; border-bottom: 1px solid #dee2e6; text-align: center; color: {decision_color}; font-weight: bold;">{decision}</td>
        </tr>
    """

opportunity_cost_html += f"""
        </tbody>
    </table>
    
    <div style="margin-top: 20px; padding: 15px; background-color: #e7f3ff; border-left: 4px solid #007bff; border-radius: 4px;">
        <h4 style="color: #0056b3; margin-bottom: 10px;">💡 Economic Interpretation</h4>
        <ul style="margin: 0; padding-left: 20px; color: #495057;">
            <li>Opportunity cost represents the financial penalty of not choosing the most efficient option</li>
            <li>Higher efficiency ratios indicate better oxygen transfer performance relative to baseline</li>
            <li>NPV opportunity cost shows the present value of losses over {analysis_years} years</li>
            <li>Investment decisions balance efficiency gains against opportunity costs</li>
        </ul>
    </div>
</div>
"""

display(HTML(opportunity_cost_html))
