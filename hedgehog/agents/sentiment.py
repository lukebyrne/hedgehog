"""Sentiment analyst agent that analyzes news, social media, and market sentiment."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from pydantic_ai import agent


class NewsAnalysis(BaseModel):
    """Analysis of news sentiment for a company."""

    recent_articles_count: int = Field(..., description="Number of recent news articles analyzed")
    positive_articles: int = Field(..., description="Number of positive news articles")
    negative_articles: int = Field(..., description="Number of negative news articles")
    neutral_articles: int = Field(..., description="Number of neutral news articles")
    news_sentiment_score: float = Field(..., description="Overall news sentiment score (-1 to 1)")
    key_positive_topics: List[str] = Field(..., description="Key positive topics in news")
    key_negative_topics: List[str] = Field(..., description="Key negative topics in news")
    significant_events: List[str] = Field(..., description="Significant recent events")


class SocialMediaAnalysis(BaseModel):
    """Analysis of social media sentiment for a company."""

    platform_distribution: Dict[str, int] = Field(..., description="Distribution of mentions by platform")
    mention_count: int = Field(..., description="Total social media mentions analyzed")
    positive_mentions: int = Field(..., description="Number of positive mentions")
    negative_mentions: int = Field(..., description="Number of negative mentions")
    neutral_mentions: int = Field(..., description="Number of neutral mentions")
    social_sentiment_score: float = Field(..., description="Overall social sentiment score (-1 to 1)")
    trending_hashtags: List[str] = Field(..., description="Trending hashtags related to the company")
    viral_content: List[str] = Field(..., description="Viral content related to the company")


class InsiderActivity(BaseModel):
    """Analysis of insider trading activity."""

    buy_transactions: int = Field(..., description="Number of insider buy transactions")
    sell_transactions: int = Field(..., description="Number of insider sell transactions")
    net_shares_change: int = Field(..., description="Net change in insider-owned shares")
    significant_buyers: List[str] = Field(..., description="Significant insider buyers")
    significant_sellers: List[str] = Field(..., description="Significant insider sellers")
    buys_value: float = Field(..., description="Total value of insider buys ($)")
    sells_value: float = Field(..., description="Total value of insider sells ($)")
    insider_sentiment: str = Field(..., description="Overall insider sentiment assessment")


class SentimentAnalysis(BaseModel):
    """Comprehensive sentiment analysis for a company."""

    ticker: str = Field(..., description="Stock ticker symbol")
    company_name: str = Field(..., description="Full company name")
    news_analysis: NewsAnalysis = Field(..., description="News sentiment analysis")
    social_analysis: SocialMediaAnalysis = Field(..., description="Social media sentiment analysis")
    insider_activity: InsiderActivity = Field(..., description="Insider trading activity analysis")
    overall_sentiment: str = Field(..., description="Overall sentiment assessment (Positive/Neutral/Negative)")
    sentiment_score: float = Field(..., description="Aggregated sentiment score (-1 to 1)")
    sentiment_momentum: str = Field(..., description="Sentiment momentum (Improving/Stable/Deteriorating)")
    market_perception: str = Field(..., description="Overall market perception assessment")
    key_sentiment_drivers: List[str] = Field(..., description="Key drivers of current sentiment")
    contrarian_indicators: List[str] = Field(..., description="Potential contrarian indicators")
    rating: int = Field(..., ge=1, le=10, description="Overall sentiment rating from 1-10")
    recommendation: str = Field(..., description="Sentiment-based recommendation (Buy/Hold/Sell)")
    reasoning: str = Field(..., description="Reasoning behind recommendation")


@agent
async def sentiment_analysis(ticker: str, news_data: Dict[str, Any], social_data: Dict[str, Any], insider_data: Dict[str, Any]) -> SentimentAnalysis:
    """Analyze news, social media, and market sentiment for a company.

    Args:
        ticker: The stock ticker symbol
        news_data: Dictionary containing recent news articles and sentiment
        social_data: Dictionary containing social media mentions and sentiment
        insider_data: Dictionary containing insider trading activity

    Returns:
        SentimentAnalysis: A comprehensive sentiment analysis with recommendation
    """
    # This function will be executed by the AI model, which will provide a sentiment analysis
    # based on the news, social, and insider data
    pass