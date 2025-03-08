"""Ben Graham agent that applies his value investing principles to analyze stocks."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from pydantic_ai import agent


class GrahamCriteria(BaseModel):
    """Ben Graham's key value investing criteria applied to a company."""

    adequate_size: str = Field(..., description="Assessment of company size and financial strength")
    financial_condition: str = Field(..., description="Assessment of current assets to liabilities ratio")
    earnings_stability: str = Field(..., description="Assessment of earnings stability over past decade")
    dividend_record: str = Field(..., description="Assessment of dividend payment history")
    earnings_growth: str = Field(..., description="Assessment of earnings per share growth")
    price_to_earnings: str = Field(..., description="Assessment of moderate P/E ratio")
    price_to_book: str = Field(..., description="Assessment of price to book ratio")
    margin_of_safety: str = Field(..., description="Assessment of margin of safety in current price")


class GrahamAnalysis(BaseModel):
    """Ben Graham-style analysis of a company."""

    ticker: str = Field(..., description="Stock ticker symbol")
    company_name: str = Field(..., description="Full company name")
    criteria: GrahamCriteria = Field(..., description="Graham investing criteria applied")
    strengths: List[str] = Field(..., description="Key strengths from Graham's perspective")
    concerns: List[str] = Field(..., description="Key concerns from Graham's perspective")
    passes_criteria: bool = Field(..., description="Whether company meets Graham's criteria")
    would_invest: bool = Field(..., description="Whether Graham would likely invest")
    rating: int = Field(..., ge=1, le=10, description="Overall Graham rating from 1-10")
    recommendation: str = Field(..., description="Investment recommendation (Buy/Hold/Sell)")
    reasoning: str = Field(..., description="Reasoning behind recommendation")


@agent
async def graham_analysis(ticker: str, company_data: Dict[str, Any]) -> GrahamAnalysis:
    """Analyze a company using Ben Graham's value investing principles.

    Args:
        ticker: The stock ticker symbol
        company_data: Dictionary containing company financial and business data

    Returns:
        GrahamAnalysis: A Ben Graham-style analysis with recommendation
    """
    # This function will be executed by the AI model, which will provide a Graham-style analysis
    # based on the company data
    pass