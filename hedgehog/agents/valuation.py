"""Valuation analyst agent that performs various valuation analyses on companies."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from pydantic_ai import agent


class ComparableMultiples(BaseModel):
    """Valuation multiples for comparable companies analysis."""

    pe_ratio: float = Field(..., description="Price to Earnings ratio")
    forward_pe: float = Field(..., description="Forward Price to Earnings ratio")
    pb_ratio: float = Field(..., description="Price to Book ratio")
    ps_ratio: float = Field(..., description="Price to Sales ratio")
    ev_ebitda: float = Field(..., description="Enterprise Value to EBITDA ratio")
    ev_sales: float = Field(..., description="Enterprise Value to Sales ratio")
    peg_ratio: float = Field(..., description="Price/Earnings to Growth ratio")
    dividend_yield: float = Field(..., description="Dividend yield (%)")
    peer_average_pe: float = Field(..., description="Peer average P/E ratio")
    peer_average_pb: float = Field(..., description="Peer average P/B ratio")
    industry_average_pe: float = Field(..., description="Industry average P/E ratio")
    industry_average_pb: float = Field(..., description="Industry average P/B ratio")


class DiscountedCashFlowModel(BaseModel):
    """Discounted Cash Flow (DCF) model results."""

    revenue_growth_rate: float = Field(..., description="Projected revenue growth rate (%)")
    ebitda_margin: float = Field(..., description="Projected EBITDA margin (%)")
    tax_rate: float = Field(..., description="Effective tax rate (%)")
    wacc: float = Field(..., description="Weighted Average Cost of Capital (%)")
    terminal_growth_rate: float = Field(..., description="Terminal growth rate (%)")
    projection_years: int = Field(..., description="Number of years in projection period")
    present_value_fcf: float = Field(..., description="Present value of projected cash flows ($)")
    terminal_value: float = Field(..., description="Terminal value ($)")
    enterprise_value: float = Field(..., description="Total enterprise value ($)")
    equity_value: float = Field(..., description="Total equity value ($)")
    shares_outstanding: float = Field(..., description="Shares outstanding (millions)")
    dcf_value_per_share: float = Field(..., description="DCF value per share ($)")


class ValuationSummary(BaseModel):
    """Summary of various valuation methods and results."""

    current_price: float = Field(..., description="Current stock price ($)")
    comps_implied_value: float = Field(..., description="Implied value from comparable analysis ($)")
    dcf_value: float = Field(..., description="DCF valuation per share ($)")
    peg_value: float = Field(..., description="PEG-based valuation per share ($)")
    graham_value: float = Field(..., description="Graham formula valuation per share ($)")
    dividend_discount_value: float = Field(..., description="Dividend discount model value ($)")
    average_value: float = Field(..., description="Average valuation across methods ($)")
    median_value: float = Field(..., description="Median valuation across methods ($)")
    upside_potential: float = Field(..., description="Upside potential from current price (%)")
    downside_risk: float = Field(..., description="Downside risk from current price (%)")
    margin_of_safety: float = Field(..., description="Margin of safety at current price (%)")


class ValuationAnalysis(BaseModel):
    """Comprehensive valuation analysis of a company."""

    ticker: str = Field(..., description="Stock ticker symbol")
    company_name: str = Field(..., description="Full company name")
    analyst_target_price: float = Field(..., description="Average analyst target price ($)")
    comparable_multiples: ComparableMultiples = Field(..., description="Comparable companies analysis")
    dcf_model: DiscountedCashFlowModel = Field(..., description="Discounted Cash Flow model")
    valuation_summary: ValuationSummary = Field(..., description="Valuation summary across methods")
    strengths: List[str] = Field(..., description="Key valuation strengths")
    concerns: List[str] = Field(..., description="Key valuation concerns")
    catalyst_opportunities: List[str] = Field(..., description="Potential catalysts for valuation improvement")
    intrinsic_value_range: Dict[str, float] = Field(..., description="Range of intrinsic value estimates")
    fair_value_estimate: float = Field(..., description="Fair value estimate per share ($)")
    sensitivity_factors: List[str] = Field(..., description="Key factors affecting valuation")
    rating: int = Field(..., ge=1, le=10, description="Overall valuation rating from 1-10")
    recommendation: str = Field(..., description="Valuation-based recommendation (Buy/Hold/Sell)")
    reasoning: str = Field(..., description="Reasoning behind recommendation")


@agent
async def valuation_analysis(ticker: str, financial_data: Dict[str, Any], market_data: Dict[str, Any], peer_data: Dict[str, Any]) -> ValuationAnalysis:
    """Perform comprehensive valuation analysis on a company.

    Args:
        ticker: The stock ticker symbol
        financial_data: Dictionary containing company financial data
        market_data: Dictionary containing market data for the company
        peer_data: Dictionary containing data for peer companies

    Returns:
        ValuationAnalysis: A comprehensive valuation analysis with recommendation
    """
    # This function will be executed by the AI model, which will provide a valuation analysis
    # based on the financial, market, and peer data
    pass