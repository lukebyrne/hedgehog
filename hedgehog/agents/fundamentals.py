"""Fundamental analyst agent that analyzes company fundamentals and financial metrics."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from pydantic_ai import agent


class FinancialRatios(BaseModel):
    """Key financial ratios for fundamental analysis."""

    pe_ratio: float = Field(..., description="Price to Earnings ratio")
    pb_ratio: float = Field(..., description="Price to Book ratio")
    ps_ratio: float = Field(..., description="Price to Sales ratio")
    peg_ratio: float = Field(..., description="Price/Earnings to Growth ratio")
    debt_to_equity: float = Field(..., description="Debt to Equity ratio")
    current_ratio: float = Field(..., description="Current ratio")
    quick_ratio: float = Field(..., description="Quick ratio")
    roe: float = Field(..., description="Return on Equity (%)")
    roa: float = Field(..., description="Return on Assets (%)")
    gross_margin: float = Field(..., description="Gross margin (%)")
    operating_margin: float = Field(..., description="Operating margin (%)")
    net_margin: float = Field(..., description="Net margin (%)")
    dividend_yield: float = Field(..., description="Dividend yield (%)")
    payout_ratio: float = Field(..., description="Dividend payout ratio")


class GrowthMetrics(BaseModel):
    """Growth metrics for fundamental analysis."""

    revenue_growth_3yr: float = Field(..., description="3-year revenue CAGR (%)")
    earnings_growth_3yr: float = Field(..., description="3-year earnings CAGR (%)")
    dividend_growth_3yr: float = Field(..., description="3-year dividend CAGR (%)")
    book_value_growth_3yr: float = Field(..., description="3-year book value CAGR (%)")
    fcf_growth_3yr: float = Field(..., description="3-year free cash flow CAGR (%)")
    revenue_growth_ttm: float = Field(..., description="TTM revenue growth (%)")
    earnings_growth_ttm: float = Field(..., description="TTM earnings growth (%)")
    fcf_growth_ttm: float = Field(..., description="TTM free cash flow growth (%)")


class FundamentalsAnalysis(BaseModel):
    """Comprehensive fundamental analysis of a company."""

    ticker: str = Field(..., description="Stock ticker symbol")
    company_name: str = Field(..., description="Full company name")
    sector: str = Field(..., description="Industry sector")
    industry: str = Field(..., description="Specific industry")
    financial_ratios: FinancialRatios = Field(..., description="Key financial ratios")
    growth_metrics: GrowthMetrics = Field(..., description="Key growth metrics")
    strengths: List[str] = Field(..., description="Key fundamental strengths")
    weaknesses: List[str] = Field(..., description="Key fundamental weaknesses")
    opportunities: List[str] = Field(..., description="Key opportunities")
    threats: List[str] = Field(..., description="Key threats")
    valuation_assessment: str = Field(..., description="Assessment of current valuation")
    financial_health: str = Field(..., description="Assessment of financial health")
    growth_outlook: str = Field(..., description="Assessment of growth outlook")
    rating: int = Field(..., ge=1, le=10, description="Overall fundamental rating from 1-10")
    recommendation: str = Field(..., description="Investment recommendation (Buy/Hold/Sell)")
    reasoning: str = Field(..., description="Reasoning behind recommendation")


@agent
async def fundamentals_analysis(ticker: str, financial_data: Dict[str, Any]) -> FundamentalsAnalysis:
    """Analyze company fundamentals and financial metrics.

    Args:
        ticker: The stock ticker symbol
        financial_data: Dictionary containing company financial data

    Returns:
        FundamentalsAnalysis: A comprehensive fundamental analysis with recommendation
    """
    # This function will be executed by the AI model, which will provide a fundamentals analysis
    # based on the financial data
    pass