"""Financial utilities for data analysis projects."""

import pandas as pd
import numpy as np
from typing import Union, List, Dict, Tuple, Optional


def calculate_npv(cash_flows: List[float], discount_rate: float, 
                initial_investment: Optional[float] = None) -> float:
    """
    Calculate Net Present Value (NPV) of a series of cash flows.
    
    Parameters
    ----------
    cash_flows : List[float]
        List of cash flows (can include initial investment as negative value)
    discount_rate : float
        Discount rate as decimal (e.g., 0.1 for 10%)
    initial_investment : float, optional
        Initial investment (if not included in cash flows)
        
    Returns
    -------
    float
        Net Present Value
        
    Examples
    --------
    >>> calculate_npv([-1000, 200, 300, 400, 500], 0.1)
    180.67
    """
    if initial_investment is not None:
        cash_flows = [-abs(initial_investment)] + cash_flows
    
    return sum(cf / (1 + discount_rate) ** t for t, cf in enumerate(cash_flows))


def calculate_irr(cash_flows: List[float], guess: float = 0.1, 
                tolerance: float = 1e-6, max_iterations: int = 100) -> float:
    """
    Calculate Internal Rate of Return (IRR) using the Newton-Raphson method.
    
    Parameters
    ----------
    cash_flows : List[float]
        List of cash flows (first value should be negative, representing initial investment)
    guess : float, default 0.1
        Initial guess for IRR
    tolerance : float, default 1e-6
        Tolerance for convergence
    max_iterations : int, default 100
        Maximum number of iterations
        
    Returns
    -------
    float
        Internal Rate of Return as decimal
        
    Examples
    --------
    >>> calculate_irr([-1000, 300, 400, 500])
    0.1859
    """
    from scipy import optimize
    
    def npv_equation(rate):
        return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))
    
    try:
        irr = optimize.newton(npv_equation, guess, tol=tolerance, maxiter=max_iterations)
        return irr
    except RuntimeError:
        # If Newton-Raphson fails, try bisection method
        try:
            irr = optimize.brentq(npv_equation, -0.999, 1000)
            return irr
        except ValueError:
            return np.nan


def calculate_payback_period(cash_flows: List[float], cumulative: bool = True) -> float:
    """
    Calculate the payback period for an investment.
    
    Parameters
    ----------
    cash_flows : List[float]
        List of cash flows (first value should be negative, representing initial investment)
    cumulative : bool, default True
        If True, uses cumulative cash flows for a more accurate calculation
        
    Returns
    -------
    float
        Payback period in periods
        
    Examples
    --------
    >>> calculate_payback_period([-1000, 300, 400, 500])
    2.6
    """
    if cash_flows[0] >= 0:
        raise ValueError("First cash flow should be negative (initial investment)")
    
    investment = abs(cash_flows[0])
    cash_flows = cash_flows[1:]  # Remove initial investment
    
    if cumulative:
        cum_cash_flows = np.cumsum(cash_flows)
        for i, cf in enumerate(cum_cash_flows):
            if cf >= investment:
                # If exact period found
                if cf == investment:
                    return i + 1
                # Interpolate between periods
                if i > 0:
                    prev_cf = cum_cash_flows[i-1]
                    fraction = (investment - prev_cf) / (cf - prev_cf)
                    return i + fraction
                else:
                    fraction = investment / cf
                    return fraction
        # If investment not recovered within given periods
        return float('inf')
    else:
        # Simple payback calculation
        recovered = 0
        for i, cf in enumerate(cash_flows):
            recovered += cf
            if recovered >= investment:
                return i + 1 - (recovered - investment) / cf
        # If investment not recovered within given periods
        return float('inf')


def calculate_roi(cash_flows: List[float], investment: Optional[float] = None, 
                annualized: bool = False, periods: Optional[int] = None) -> float:
    """
    Calculate Return on Investment (ROI).
    
    Parameters
    ----------
    cash_flows : List[float]
        List of cash flows (can include initial investment as first negative value)
    investment : float, optional
        Initial investment amount (if not included in cash_flows)
    annualized : bool, default False
        Whether to calculate annualized ROI
    periods : int, optional
        Number of periods for annualized calculation (required if annualized=True)
        
    Returns
    -------
    float
        ROI as decimal
        
    Examples
    --------
    >>> calculate_roi([-1000, 300, 400, 500])
    0.20
    >>> calculate_roi([-1000, 300, 400, 500], annualized=True, periods=3)
    0.0626
    """
    if investment is None:
        if cash_flows[0] < 0:
            investment = abs(cash_flows[0])
            cash_flows = cash_flows[1:]  # Remove initial investment
        else:
            raise ValueError("Initial investment not provided and first cash flow is positive")
    
    total_return = sum(cash_flows)
    roi = (total_return - investment) / investment
    
    if annualized and periods:
        # Convert to annualized ROI
        annualized_roi = (1 + roi) ** (1 / periods) - 1
        return annualized_roi
    
    return roi


def create_loan_amortization_schedule(principal: float, annual_interest_rate: float, 
                                    years: int, payments_per_year: int = 12) -> pd.DataFrame:
    """
    Create a loan amortization schedule.
    
    Parameters
    ----------
    principal : float
        Loan amount
    annual_interest_rate : float
        Annual interest rate as decimal (e.g., 0.05 for 5%)
    years : int
        Loan term in years
    payments_per_year : int, default 12
        Number of payments per year
        
    Returns
    -------
    pd.DataFrame
        Amortization schedule with columns for payment, principal, interest, and balance
        
    Examples
    --------
    >>> schedule = create_loan_amortization_schedule(100000, 0.05, 5)
    >>> schedule.head()
    """
    # Calculate periodic interest rate and number of payments
    rate_per_period = annual_interest_rate / payments_per_year
    num_payments = years * payments_per_year
    
    # Calculate payment amount
    payment = principal * (rate_per_period * (1 + rate_per_period) ** num_payments) / \
              ((1 + rate_per_period) ** num_payments - 1)
    
    # Initialize amortization schedule
    schedule = []
    balance = principal
    
    for period in range(1, num_payments + 1):
        interest_payment = balance * rate_per_period
        principal_payment = payment - interest_payment
        balance -= principal_payment
        
        schedule.append({
            'Period': period,
            'Payment': payment,
            'Principal': principal_payment,
            'Interest': interest_payment,
            'Balance': max(0, balance)  # Avoid negative balance due to rounding
        })
    
    return pd.DataFrame(schedule)


def calculate_depreciation(cost: float, salvage_value: float, useful_life: int, 
                         method: str = 'straight_line', double_declining_factor: float = 2.0) -> pd.DataFrame:
    """
    Calculate depreciation schedule using various methods.
    
    Parameters
    ----------
    cost : float
        Initial cost of the asset
    salvage_value : float
        Estimated salvage value at the end of useful life
    useful_life : int
        Useful life of the asset in years
    method : str, default 'straight_line'
        Depreciation method: 'straight_line', 'declining_balance', 'double_declining', or 'sum_of_years'
    double_declining_factor : float, default 2.0
        Factor for double declining balance method
        
    Returns
    -------
    pd.DataFrame
        Depreciation schedule
        
    Examples
    --------
    >>> schedule = calculate_depreciation(10000, 1000, 5, method='straight_line')
    >>> schedule
    """
    depreciable_amount = cost - salvage_value
    schedule = []
    
    if method == 'straight_line':
        annual_depreciation = depreciable_amount / useful_life
        book_value = cost
        
        for year in range(1, useful_life + 1):
            book_value -= annual_depreciation
            schedule.append({
                'Year': year,
                'Depreciation': annual_depreciation,
                'Book Value': max(book_value, salvage_value)
            })
    
    elif method in ['declining_balance', 'double_declining']:
        if method == 'double_declining':
            depreciation_rate = double_declining_factor / useful_life
        else:
            depreciation_rate = 1 / useful_life
        
        book_value = cost
        
        for year in range(1, useful_life + 1):
            # Switch to straight-line if it gives higher depreciation
            remaining_years = useful_life - year + 1
            straight_line_amount = (book_value - salvage_value) / remaining_years if remaining_years > 0 else 0
            
            declining_amount = book_value * depreciation_rate
            
            # Use the higher of declining balance or straight-line
            if straight_line_amount > declining_amount and book_value > salvage_value:
                depreciation = straight_line_amount
            else:
                depreciation = min(declining_amount, book_value - salvage_value)
            
            book_value -= depreciation
            
            schedule.append({
                'Year': year,
                'Depreciation': depreciation,
                'Book Value': max(book_value, salvage_value)
            })
    
    elif method == 'sum_of_years':
        sum_of_years = sum(range(1, useful_life + 1))
        book_value = cost
        
        for year in range(1, useful_life + 1):
            depreciation_rate = (useful_life - year + 1) / sum_of_years
            depreciation = depreciable_amount * depreciation_rate
            book_value -= depreciation
            
            schedule.append({
                'Year': year,
                'Depreciation': depreciation,
                'Book Value': max(book_value, salvage_value)
            })
    
    else:
        raise ValueError(f"Unknown method: {method}. Use 'straight_line', 'declining_balance', 'double_declining', or 'sum_of_years'")
    
    return pd.DataFrame(schedule)
