"""Core financial calculation functions for aerator analysis."""

import scipy.optimize
from config import FINANCIAL_PARAMS


def calculate_adapted_irr(
    delta_investment, annual_saving, years=None, inflation_rate=None
):
    """Calculate adapted IRR for aerator comparisons."""
    years = years or FINANCIAL_PARAMS["analysis_horizon"]
    inflation_rate = inflation_rate or FINANCIAL_PARAMS["inflation_rate"]

    if annual_saving <= 0:
        return -100

    if delta_investment <= 0:
        if delta_investment == 0:
            return 100.0
        cost_advantage_factor = (
            abs(delta_investment) / annual_saving if annual_saving > 0 else 1
        )
        return min(100.0, 50.0 + cost_advantage_factor * 10)

    try:

        def npv(rate):
            if rate <= -1:
                return float("inf")
            result = -delta_investment
            for i in range(1, years + 1):
                inflation_factor = (1 + inflation_rate) ** (i - 1)
                discount_factor = (1 + rate) ** i
                result += (annual_saving * inflation_factor) / discount_factor
            return result

        try:
            irr_result = scipy.optimize.brentq(npv, -0.99, 10.0)
            irr_percent = irr_result * 100
            return max(min(irr_percent, 50), -50)
        except ValueError:
            irr_result = scipy.optimize.newton(
                npv, x0=0.1, tol=1e-5, maxiter=100
            )
            irr_percent = irr_result * 100
            return max(min(irr_percent, 50), -50)

    except Exception as e:
        print(f"IRR calculation failed: {e}")
        if delta_investment > 0:
            simple_irr = (annual_saving / delta_investment) * 100
            return max(min(simple_irr, 50), -50)
        else:
            return 50.0


def calculate_npv_savings(
    annual_saving_year1, years=None, inflation_rate=None, nominal_rate=None
):
    """Calculate NPV of savings using real discount rate."""
    years = years or FINANCIAL_PARAMS["analysis_horizon"]
    inflation_rate = inflation_rate or FINANCIAL_PARAMS["inflation_rate"]
    nominal_rate = nominal_rate or FINANCIAL_PARAMS["nominal_rate"]

    real_rate = (1 + nominal_rate) / (1 + inflation_rate) - 1

    npv_savings = 0
    for i in range(1, years + 1):
        inflated_saving = annual_saving_year1 * (1 + inflation_rate) ** (i - 1)
        pv_saving = inflated_saving / (1 + real_rate) ** i
        npv_savings += pv_saving

    return npv_savings


def calculate_sotr_impact_npv(
    sotr_baseline, sotr_improved, energy_cost_factor=None, **kwargs
):
    """Calculate NPV of savings for SOTR improvement."""
    energy_cost_factor = (
        energy_cost_factor or FINANCIAL_PARAMS["energy_cost_factor"]
    )
    annual_saving_year1 = (sotr_improved - sotr_baseline) * energy_cost_factor
    return calculate_npv_savings(annual_saving_year1, **kwargs)


def get_aerator_properties(sotr):
    """Calculate durability and maintenance based on SOTR."""
    base_durability = 2.0
    base_maintenance = 65

    durability = min(base_durability * (0.4 + 0.6 * sotr), 10.0)
    maintenance = max(base_maintenance * (1.4 - 0.2 * sotr), 40.0)
    unit_cost = 500 + 200 * (sotr - 1.0) ** 0.7

    return durability, maintenance, unit_cost


def interpret_irr(irr):
    """Provide realistic interpretation of IRR values."""
    if irr > 60:
        return "Highly attractive"
    elif irr > 40:
        return "Very attractive"
    elif irr > 20:
        return "Attractive"
    elif irr > 10:
        return "Moderately attractive"
    elif irr > 5:
        return "Marginally attractive"
    elif irr > 2.5:
        return "Slightly positive"
    else:
        return "Unattractive"
