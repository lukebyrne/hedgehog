from __future__ import annotations as _annotations

import asyncio
from dataclasses import dataclass, field
from typing import Any, List, Optional, Dict, Union

from pydantic_ai import Agent
from pydantic_graph import BaseNode, End, Graph, GraphRunContext


# Data Models
@dataclass
class APIResponse:
    """Base class for API responses"""
    data: Dict[str, Any]


@dataclass
class APIOneResponse(APIResponse):
    """Response from API One"""
    pass


@dataclass
class APITwoResponse(APIResponse):
    """Response from API Two"""
    pass


@dataclass
class AggregatedData:
    """Data aggregated from multiple sources"""
    api_one_data: Dict[str, Any]
    api_two_data: Dict[str, Any]
    combined_data: Dict[str, Any]


@dataclass
class AnalysisResult:
    """Analysis result from an agent"""
    recommendations: List[str]
    confidence: float
    metadata: Dict[str, Any]


@dataclass
class InvestmentDecision:
    """Final investment decision"""
    buy_assets: List[str]
    sell_assets: List[str]
    hold_assets: List[str]
    rationale: str


@dataclass
class GraphState:
    """State maintained throughout the graph execution"""
    api_one_response: Optional[APIOneResponse] = None
    api_two_response: Optional[APITwoResponse] = None
    aggregated_data: Optional[AggregatedData] = None
    analysis_results: List[AnalysisResult] = field(default_factory=list)
    investment_decision: Optional[InvestmentDecision] = None
    # Track which analyses have been completed to ensure all are done
    analysis_completed: Dict[str, bool] = field(default_factory=lambda: {
        "one": False, "two": False, "three": False, "four": False
    })


# Mock Agents (replace with actual implementations later)
api_one_agent = Agent(
    "openai:gpt-4o",  # This would be replaced with your actual model
    result_type=APIOneResponse,
    system_prompt="Make API call to fetch market data.",
)

api_two_agent = Agent(
    "openai:gpt-4o",  # This would be replaced with your actual model
    result_type=APITwoResponse,
    system_prompt="Make API call to fetch additional market data.",
)

data_aggregator_agent = Agent(
    "openai:gpt-4o",  # This would be replaced with your actual model
    result_type=AggregatedData,
    system_prompt="Aggregate data from multiple sources into a unified format.",
)

analysis_agent = Agent(
    "openai:gpt-4o",  # This would be replaced with your actual model
    result_type=AnalysisResult,
    system_prompt="Analyze market data and provide investment recommendations.",
)

portfolio_manager_agent = Agent(
    "openai:gpt-4o",  # This would be replaced with your actual model
    result_type=InvestmentDecision,
    system_prompt="Make investment decisions based on analysis from multiple sources.",
)


# Graph Nodes
@dataclass
class Start(BaseNode[GraphState]):
    """Starting point of the investment workflow"""

    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> Union['APICallOne', 'APICallTwo']:
        print("Starting the investment workflow")

        # For a true implementation with actual parallel execution, you would:
        # 1. Start both API calls concurrently using asyncio.gather
        # 2. Select one to return for the graph traversal

        # For diagram clarity, we'll return APICallOne, but the actual implementation
        # would need to handle both paths
        return APICallOne()


@dataclass
class APICallOne(BaseNode[GraphState]):
    """Make API call to fetch primary market data"""

    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> 'DataAggregation':
        print("Making API Call One...")
        # Mock API call
        mock_data = {"stocks": {"AAPL": 180.5, "GOOGL": 140.2}, "timestamp": "2023-07-01T12:00:00Z"}
        # In a real implementation, you would make an actual API call
        # result = await api_one_agent.run("Fetch latest market data")

        # For mock purposes
        ctx.state.api_one_response = APIOneResponse(data=mock_data)

        # In an actual parallel implementation, we would:
        # 1. Check if the other API call is complete
        # 2. Only proceed to aggregation when both are done

        # For this mock sequential version:
        # Mock the second API call directly here to simulate it happening in parallel
        print("Simulating API Call Two running in parallel...")
        ctx.state.api_two_response = APITwoResponse(data={
            "bonds": {"US10Y": 3.8, "US30Y": 4.2},
            "commodities": {"GOLD": 2000.5},
            "timestamp": "2023-07-01T12:05:00Z"
        })

        # Move directly to data aggregation
        return DataAggregation()


@dataclass
class APICallTwo(BaseNode[GraphState]):
    """Make API call to fetch secondary market data"""

    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> 'DataAggregation':
        print("Making API Call Two...")
        # Mock API call
        mock_data = {"bonds": {"US10Y": 3.8, "US30Y": 4.2}, "commodities": {"GOLD": 2000.5}, "timestamp": "2023-07-01T12:05:00Z"}
        # In a real implementation, you would make an actual API call
        # result = await api_two_agent.run("Fetch latest bond and commodity data")

        # For mock purposes
        ctx.state.api_two_response = APITwoResponse(data=mock_data)

        # In an actual parallel implementation, we would:
        # 1. Check if the other API call is complete
        # 2. Only proceed to aggregation when both are done

        # For this mock sequential version:
        # Mock the first API call directly here to simulate it happening in parallel
        print("Simulating API Call One running in parallel...")
        ctx.state.api_one_response = APIOneResponse(data={
            "stocks": {"AAPL": 180.5, "GOOGL": 140.2},
            "timestamp": "2023-07-01T12:00:00Z"
        })

        # Move directly to data aggregation
        return DataAggregation()


@dataclass
class DataAggregation(BaseNode[GraphState]):
    """Aggregate data from all API sources"""

    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> Union['AgentAnalysisOne', 'AgentAnalysisTwo', 'AgentAnalysisThree', 'AgentAnalysisFour']:
        print("Aggregating data...")

        if not ctx.state.api_one_response or not ctx.state.api_two_response:
            raise ValueError("API responses not available for aggregation")

        # Combine data from both APIs
        combined_data = {
            **ctx.state.api_one_response.data,
            **ctx.state.api_two_response.data,
            "meta": {
                "aggregated_at": "2023-07-01T12:10:00Z"
            }
        }

        # In a real implementation, you might use a more sophisticated method
        # result = await data_aggregator_agent.run(format_as_xml({
        #     "api_one_data": ctx.state.api_one_response.data,
        #     "api_two_data": ctx.state.api_two_response.data
        # }))

        # For mock purposes
        ctx.state.aggregated_data = AggregatedData(
            api_one_data=ctx.state.api_one_response.data,
            api_two_data=ctx.state.api_two_response.data,
            combined_data=combined_data
        )

        # For a true parallel implementation, you would launch all analyses concurrently with asyncio.gather

        # In this mock implementation, start by launching Analysis One
        # but also simulate the other analyses happening in parallel

        # Simulate running all other analyses in parallel
        print("Simulating all agent analyses running in parallel...")
        ctx.state.analysis_results.append(AnalysisResult(
            recommendations=["Buy US10Y bonds", "Sell GOLD"],
            confidence=0.78,
            metadata={"focus": "fixed income and commodities", "timeframe": "medium-term"}
        ))
        ctx.state.analysis_completed["two"] = True

        ctx.state.analysis_results.append(AnalysisResult(
            recommendations=["Buy defensive stocks", "Hold cash"],
            confidence=0.92,
            metadata={"focus": "market risk assessment", "timeframe": "long-term"}
        ))
        ctx.state.analysis_completed["three"] = True

        ctx.state.analysis_results.append(AnalysisResult(
            recommendations=["Diversify portfolio", "Reduce exposure to tech"],
            confidence=0.81,
            metadata={"focus": "portfolio allocation", "timeframe": "medium-term"}
        ))
        ctx.state.analysis_completed["four"] = True

        # For the graph traversal, start with Analysis One
        return AgentAnalysisOne()


@dataclass
class AgentAnalysisOne(BaseNode[GraphState]):
    """First agent analysis of aggregated data"""

    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> 'PortfolioManagerDecision':
        print("Performing Agent Analysis One...")

        if not ctx.state.aggregated_data:
            raise ValueError("Aggregated data not available for analysis")

        # Mock analysis
        mock_result = AnalysisResult(
            recommendations=["Buy AAPL", "Hold GOOGL"],
            confidence=0.85,
            metadata={"focus": "tech stocks", "timeframe": "short-term"}
        )

        # In a real implementation, you would use the agent
        # result = await analysis_agent.run(format_as_xml({
        #     "data": ctx.state.aggregated_data.combined_data,
        #     "focus": "tech stocks"
        # }))

        ctx.state.analysis_results.append(mock_result)
        ctx.state.analysis_completed["one"] = True

        # Go directly to portfolio decision as all analyses are running in parallel
        return PortfolioManagerDecision()


@dataclass
class AgentAnalysisTwo(BaseNode[GraphState]):
    """Second agent analysis of aggregated data"""

    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> 'PortfolioManagerDecision':
        print("Performing Agent Analysis Two...")

        if not ctx.state.aggregated_data:
            raise ValueError("Aggregated data not available for analysis")

        # Mock analysis
        mock_result = AnalysisResult(
            recommendations=["Buy US10Y bonds", "Sell GOLD"],
            confidence=0.78,
            metadata={"focus": "fixed income and commodities", "timeframe": "medium-term"}
        )

        # In a real implementation, you would use the agent
        # result = await analysis_agent.run(format_as_xml({
        #     "data": ctx.state.aggregated_data.combined_data,
        #     "focus": "fixed income and commodities"
        # }))

        ctx.state.analysis_results.append(mock_result)
        ctx.state.analysis_completed["two"] = True

        # Go directly to portfolio decision as all analyses are running in parallel
        return PortfolioManagerDecision()


@dataclass
class AgentAnalysisThree(BaseNode[GraphState]):
    """Third agent analysis of aggregated data"""

    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> 'PortfolioManagerDecision':
        print("Performing Agent Analysis Three...")

        if not ctx.state.aggregated_data:
            raise ValueError("Aggregated data not available for analysis")

        # Mock analysis
        mock_result = AnalysisResult(
            recommendations=["Buy defensive stocks", "Hold cash"],
            confidence=0.92,
            metadata={"focus": "market risk assessment", "timeframe": "long-term"}
        )

        # In a real implementation, you would use the agent
        # result = await analysis_agent.run(format_as_xml({
        #     "data": ctx.state.aggregated_data.combined_data,
        #     "focus": "market risk assessment"
        # }))

        ctx.state.analysis_results.append(mock_result)
        ctx.state.analysis_completed["three"] = True

        # Go directly to portfolio decision as all analyses are running in parallel
        return PortfolioManagerDecision()


@dataclass
class AgentAnalysisFour(BaseNode[GraphState]):
    """Fourth agent analysis of aggregated data"""

    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> 'PortfolioManagerDecision':
        print("Performing Agent Analysis Four...")

        if not ctx.state.aggregated_data:
            raise ValueError("Aggregated data not available for analysis")

        # Mock analysis
        mock_result = AnalysisResult(
            recommendations=["Diversify portfolio", "Reduce exposure to tech"],
            confidence=0.81,
            metadata={"focus": "portfolio allocation", "timeframe": "medium-term"}
        )

        # In a real implementation, you would use the agent
        # result = await analysis_agent.run(format_as_xml({
        #     "data": ctx.state.aggregated_data.combined_data,
        #     "focus": "portfolio allocation"
        # }))

        ctx.state.analysis_results.append(mock_result)
        ctx.state.analysis_completed["four"] = True

        # Go directly to portfolio decision
        return PortfolioManagerDecision()


@dataclass
class PortfolioManagerDecision(BaseNode[GraphState]):
    """Make final investment decision based on all analyses"""

    async def run(
        self, ctx: GraphRunContext[GraphState]
    ) -> End[InvestmentDecision]:
        print("Making Portfolio Manager Decision...")

        # Ensure all analyses have been completed
        if not all(ctx.state.analysis_completed.values()):
            raise ValueError("All analysis tasks must be completed before making investment decisions")

        # Mock decision
        mock_decision = InvestmentDecision(
            buy_assets=["AAPL", "US10Y bonds", "Defensive ETFs"],
            sell_assets=["GOLD", "High-risk tech stocks"],
            hold_assets=["GOOGL", "Cash reserves"],
            rationale="Based on analysis from multiple agents, a balanced approach with reduced tech exposure is recommended."
        )

        # In a real implementation, you would use the agent
        # result = await portfolio_manager_agent.run(format_as_xml({
        #     "analyses": ctx.state.analysis_results,
        #     "market_data": ctx.state.aggregated_data.combined_data
        # }))

        ctx.state.investment_decision = mock_decision
        return End(mock_decision)


# Create the graph
investment_graph = Graph(nodes=[
    Start,
    APICallOne,
    APICallTwo,
    DataAggregation,
    AgentAnalysisOne,
    AgentAnalysisTwo,
    AgentAnalysisThree,
    AgentAnalysisFour,
    PortfolioManagerDecision
])


async def main():
    """Run the investment decision graph"""
    state = GraphState()
    start_node = Start()

    # Generate a mermaid diagram of the graph
    print("Graph Diagram (Mermaid format):")
    print(investment_graph.mermaid_code(start_node=Start))

    # Run the graph
    print("\nRunning investment graph:")
    run_result = await investment_graph.run(start_node, state=state)

    # Use the correct attributes from GraphRunResult
    result = run_result.output
    history = run_result.history

    print("\nInvestment Decision:")
    print(f"Buy: {result.buy_assets}")
    print(f"Sell: {result.sell_assets}")
    print(f"Hold: {result.hold_assets}")
    print(f"Rationale: {result.rationale}")

    # Print the history steps
    print("\nGraph Execution History:")
    for step in history:
        # Different step types might have different attributes
        if hasattr(step, 'node'):
            print(f"- {step.node.__class__.__name__}")
        elif hasattr(step, 'node_id'):
            print(f"- {step.node_id}")
        else:
            print(f"- {step.__class__.__name__}")


if __name__ == "__main__":
    asyncio.run(main())