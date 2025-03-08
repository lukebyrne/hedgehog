"""Agents module for the Hedgehog AI Hedge Fund."""

from hedgehog.agents.warren_buffett import buffett_analysis
from hedgehog.agents.charlie_munger import munger_analysis
from hedgehog.agents.bill_ackman import ackman_analysis
from hedgehog.agents.ben_graham import graham_analysis
from hedgehog.agents.cathie_wood import wood_analysis
from hedgehog.agents.fundamentals import fundamentals_analysis
from hedgehog.agents.technicals import technical_analysis
from hedgehog.agents.sentiment import sentiment_analysis
from hedgehog.agents.valuation import valuation_analysis
from hedgehog.agents.portfolio_manager import portfolio_management
from hedgehog.agents.risk_manager import risk_assessment

__all__ = [
    "buffett_analysis",
    "munger_analysis",
    "ackman_analysis",
    "graham_analysis",
    "wood_analysis",
    "fundamentals_analysis",
    "technical_analysis",
    "sentiment_analysis",
    "valuation_analysis",
    "portfolio_management",
    "risk_assessment",
]