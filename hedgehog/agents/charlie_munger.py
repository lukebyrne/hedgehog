"""Charlie Munger agent that applies his investment philosophy to analyze stocks."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from pydantic_ai import agent


class MungerPrinciples(BaseModel):
    """Charlie Munger's key investment principles applied to a company."""

    business_quality: str = Field(..., description="Assessment of business quality and durability")
    rationality: str = Field(..., description="Assessment of management rationality and capital allocation")
    moat_strength: str = Field(..., description="Assessment of competitive advantage/moat")
    long_term_prospects: str = Field(..., description="Assessment of long-term business prospects")
    margin_of_safety: str = Field(..., description="Assessment of price versus intrinsic value")
    latticework_view: str = Field(..., description="Multidisciplinary perspective on the business")


class MungerAnalysis(BaseModel):
    """Charlie Munger-style analysis of a company."""

    ticker: str = Field(..., description="Stock ticker symbol")
    company_name: str = Field(..., description="Full company name")
    principles: MungerPrinciples = Field(..., description="Munger investment principles applied")
    strengths: List[str] = Field(..., description="Key strengths from Munger's perspective")
    concerns: List[str] = Field(..., description="Key concerns from Munger's perspective")
    mental_models: List[str] = Field(..., description="Mental models most applicable to this investment")
    would_invest: bool = Field(..., description="Whether Munger would likely invest")
    rating: int = Field(..., ge=1, le=10, description="Overall Munger rating from 1-10")
    recommendation: str = Field(..., description="Investment recommendation (Buy/Hold/Sell)")
    reasoning: str = Field(..., description="Reasoning behind recommendation")


@agent
async def munger_analysis(ticker: str, company_data: Dict[str, Any]) -> MungerAnalysis:
    """Analyze a company using Charlie Munger's investment principles.

    Args:
        ticker: The stock ticker symbol
        company_data: Dictionary containing company financial and business data

    Returns:
        MungerAnalysis: A Charlie Munger-style analysis with recommendation
    """
    # This function will be executed by the AI model, which will provide a Munger-style analysis
    # based on the company data
    pass