from google.adk.agents import Agent, SequentialAgent
from agents.liquidity_analyzer import LiquidityAnalyzerAgent
from agents.market_data import MarketDataAgent
from agents.risk_manager import RiskManagerAgent
from tools.nse_data import NSEDataTool
from tools.volume_profile import VolumeProfileTool

# Market Data Agent - Fetches OHLCV data
market_data_agent = MarketDataAgent()

# Liquidity Analysis Agent - Main expert
liquidity_agent = LiquidityAnalyzerAgent(
    tools=[NSEDataTool(), VolumeProfileTool()]
)

# Risk Manager Agent
risk_agent = RiskManagerAgent()

# Root Sequential Agent
root_agent = SequentialAgent(
    name="liquidity_trading_architect",
    model="gemini-2.5-flash",
    description="Identifies buy/sell liquidity zones for NIFTY/BANKNIFTY",
    sub_agents=[
        market_data_agent,
        liquidity_agent,
        risk_agent
    ],
    instruction="""
    You are the Liquidity Trading Architect. Analyze NIFTY/BANKNIFTY charts to identify:
    1. Sell-side liquidity (below swing lows - stop clusters)
    2. Buy-side liquidity (above swing highs - stop clusters)
    3. Entry bias and risk levels
    
    Always provide price ranges, strength rating, and trade direction.
    """
)

if __name__ == "__main__":
    from google.adk.runner import InMemoryRunner
    runner = InMemoryRunner(root_agent, "liquidity-agent")
    session = runner.session_service().create_session("liquidity-agent", "trader")
    runner.run("Analyze NIFTY 1H for liquidity zones")
