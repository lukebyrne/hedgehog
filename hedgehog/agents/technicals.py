"""Technical analyst agent that analyzes price action and technical indicators."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from pydantic_ai import agent


class TechnicalIndicators(BaseModel):
    """Key technical indicators for technical analysis."""

    sma_20: float = Field(..., description="20-day Simple Moving Average")
    sma_50: float = Field(..., description="50-day Simple Moving Average")
    sma_200: float = Field(..., description="200-day Simple Moving Average")
    ema_12: float = Field(..., description="12-day Exponential Moving Average")
    ema_26: float = Field(..., description="26-day Exponential Moving Average")
    rsi_14: float = Field(..., description="14-day Relative Strength Index")
    macd: float = Field(..., description="Moving Average Convergence Divergence")
    macd_signal: float = Field(..., description="MACD Signal line")
    macd_histogram: float = Field(..., description="MACD Histogram")
    bollinger_upper: float = Field(..., description="Upper Bollinger Band")
    bollinger_middle: float = Field(..., description="Middle Bollinger Band")
    bollinger_lower: float = Field(..., description="Lower Bollinger Band")
    stochastic_k: float = Field(..., description="Stochastic %K")
    stochastic_d: float = Field(..., description="Stochastic %D")
    atr_14: float = Field(..., description="14-day Average True Range")


class VolumeIndicators(BaseModel):
    """Volume indicators for technical analysis."""

    volume_sma_20: float = Field(..., description="20-day Volume Simple Moving Average")
    obv: float = Field(..., description="On-Balance Volume")
    cmf: float = Field(..., description="Chaikin Money Flow")
    vwap: float = Field(..., description="Volume Weighted Average Price")
    volume_ratio: float = Field(..., description="Current volume to average volume ratio")


class TechnicalsAnalysis(BaseModel):
    """Comprehensive technical analysis of a stock."""

    ticker: str = Field(..., description="Stock ticker symbol")
    current_price: float = Field(..., description="Current price of the stock")
    previous_close: float = Field(..., description="Previous day's closing price")
    indicators: TechnicalIndicators = Field(..., description="Key technical indicators")
    volume_metrics: VolumeIndicators = Field(..., description="Volume indicators")
    trend: str = Field(..., description="Current trend identification (Bullish/Bearish/Neutral)")
    support_levels: List[float] = Field(..., description="Key support price levels")
    resistance_levels: List[float] = Field(..., description="Key resistance price levels")
    patterns: List[str] = Field(..., description="Identified chart patterns")
    signals: List[str] = Field(..., description="Specific technical signals")
    momentum: str = Field(..., description="Momentum assessment")
    volatility: str = Field(..., description="Volatility assessment")
    entry_points: List[float] = Field(..., description="Potential entry price points")
    exit_points: List[float] = Field(..., description="Potential exit price points")
    stop_loss: float = Field(..., description="Recommended stop loss level")
    rating: int = Field(..., ge=1, le=10, description="Overall technical rating from 1-10")
    recommendation: str = Field(..., description="Investment recommendation (Buy/Hold/Sell)")
    reasoning: str = Field(..., description="Reasoning behind recommendation")
    timeframe: str = Field(..., description="Timeframe for the technical analysis")


@agent
async def technical_analysis(ticker: str, price_data: Dict[str, Any]) -> TechnicalsAnalysis:
    """Analyze price action and technical indicators for a stock.

    Args:
        ticker: The stock ticker symbol
        price_data: Dictionary containing historical price and volume data

    Returns:
        TechnicalsAnalysis: A comprehensive technical analysis with recommendation
    """
    # This function will be executed by the AI model, which will provide a technical analysis
    # based on the price data
    pass