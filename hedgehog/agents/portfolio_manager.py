"""Portfolio manager agent that makes investment decisions based on analyst recommendations."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from pydantic_ai import agent


class PortfolioAllocation(BaseModel):
    """Allocation recommendation for a specific asset."""

    ticker: str = Field(..., description="Stock ticker symbol")
    target_weight: float = Field(..., description="Target weight in the portfolio (%)")
    current_weight: float = Field(..., description="Current weight in the portfolio (%)")
    order_type: str = Field(..., description="Order type (BUY/SELL/HOLD)")
    order_quantity: int = Field(..., description="Number of shares to trade")
    price_limit: float = Field(..., description="Limit price for the order (if applicable)")
    stop_loss: float = Field(..., description="Stop loss level for the position")
    justification: str = Field(..., description="Justification for the allocation decision")


class AssetPerformance(BaseModel):
    """Performance metrics for a specific asset."""

    ticker: str = Field(..., description="Stock ticker symbol")
    return_1d: float = Field(..., description="1-day return (%)")
    return_1w: float = Field(..., description="1-week return (%)")
    return_1m: float = Field(..., description="1-month return (%)")
    return_ytd: float = Field(..., description="Year-to-date return (%)")
    sharpe_ratio: float = Field(..., description="Sharpe ratio")
    max_drawdown: float = Field(..., description="Maximum drawdown (%)")
    volatility: float = Field(..., description="Annualized volatility (%)")


class PortfolioManagementDecision(BaseModel):
    """Comprehensive portfolio management decision."""

    cash_allocation: float = Field(..., description="Recommended cash allocation (%)")
    asset_allocations: List[PortfolioAllocation] = Field(..., description="Asset allocation recommendations")
    top_performers: List[AssetPerformance] = Field(..., description="Top performing assets")
    worst_performers: List[AssetPerformance] = Field(..., description="Worst performing assets")
    portfolio_metrics: Dict[str, float] = Field(..., description="Overall portfolio metrics")
    rebalance_needed: bool = Field(..., description="Whether portfolio rebalancing is needed")
    risk_assessment: str = Field(..., description="Overall portfolio risk assessment")
    market_outlook: str = Field(..., description="Current market outlook")
    rationale: str = Field(..., description="Rationale for the portfolio decisions")


@agent
async def portfolio_management(
    portfolio_data: Dict[str, Any],
    analyst_recommendations: Dict[str, Any],
    risk_assessment: Dict[str, Any],
    market_data: Dict[str, Any],
) -> PortfolioManagementDecision:
    """Make portfolio management decisions based on analyst recommendations and risk assessment.

    Args:
        portfolio_data: Current portfolio holdings and allocations
        analyst_recommendations: Recommendations from various analysts
        risk_assessment: Risk assessment for the portfolio
        market_data: Current market data and conditions

    Returns:
        PortfolioManagementDecision: A comprehensive portfolio management decision
    """
    # This function will be executed by the AI model, which will provide portfolio decisions
    # based on analyst recommendations and risk assessment
    pass