# BLOCK 1: main.py
#!/usr/bin/env python3
"""
Liquidity Trading Architect - Google ADK Agent
NIFTY/BANKNIFTY Options Liquidity Zone Detector
"""
from google.adk.agents import SequentialAgent
from agents.liquidity_analyzer import LiquidityAnalyzerAgent
from agents.risk_manager import RiskManagerAgent
import asyncio

async def main():
    # Main Sequential Agent Pipeline
    root_agent = SequentialAgent(
        name="liquidity_trading_architect",
        model="gemini-2.5-flash",
        sub_agents=[LiquidityAnalyzerAgent(), RiskManagerAgent()],
        instruction="""
        You are the Liquidity Trading Architect. Analyze NIFTY options using SMC/ICT:
        1. Identify buy/sell liquidity zones in underlying
        2. Calculate option Greeks impact
        3. Provide entry/exit levels with R:R ratios
        """
    )
    
    # Test run
    print("🧠 Analyzing NIFTY 23100 CE...")
    result = await root_agent.run("Analyze NIFTY 23100 CE for liquidity zones")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())

# BLOCK 2: agents/liquidity_analyzer.py
from google.adk.agents import LlmAgent
from tools.nse_data import get_nse_data, analyze_liquidity_zones

class LiquidityAnalyzerAgent(LlmAgent):
    def __init__(self):
        super().__init__(
            name="liquidity_analyzer",
            model="gemini-2.5-flash",
            tools=[get_nse_data, analyze_liquidity_zones],
            instruction="""
            LIQUIDITY ZONE ANALYSIS (SMC/ICT):
            
            SELL-SIDE (below swing lows): Long stops → Down raid → Up reversal
            BUY-SIDE (above swing highs): Short stops → Up raid → Potential pullback
            
            OUTPUT FORMAT:
            **NIFTY [STRIKE] CE Analysis**
            • Sell-side: [range] (HIGH/MED/LOW)
            • Buy-side: [range] (HIGH/MED/LOW)  
            • Bias: BULLISH above [level]
            """
        )
# BLOCK 3: tools/nse_data.py
python
from google.adk.tools import FunctionTool
import pandas as pd
from datetime import datetime

@FunctionTool
def get_nse_data(symbol: str, timeframe: str = "15min") -> dict:
    """Fetch NIFTY/BANKNIFTY OHLCV data"""
    # Real-time mock data (replace with KiteConnect)
    nifty_data = {
        "NIFTY": {
            "spot": 23114.5,
            "high": 23185,
            "low": 23050,
            "oi_call_23100": 2500000,
            "oi_put_23100": 1800000,
            "candles": [
                {"t": "15:45", "o": 23120, "h": 23150, "l": 23100, "c": 23114, "v": 1200000},
                {"t": "16:00", "o": 23114, "h": 23135, "l": 23095, "c": 23108, "v": 1500000}
            ]
        }
    }
    return nifty_data.get(symbol.upper(), {"error": "Symbol not found"})

@FunctionTool
def analyze_liquidity_zones(symbol: str) -> dict:
    """Detect liquidity pools"""
    data = get_nse_data(symbol)
    lows = [c["l"] for c in data["candles"]]
    highs = [c["h"] for c in data["candles"]]
    
    return {
        "sell_side": f"{min(lows)-50}-{min(lows)+10}",
        "buy_side": f"{max(highs)-10}-{max(highs)+50}",
        "key_level": round((data["spot"] + 50), -2)
    }
# BLOCK 4: tools/volume_profile.py
python
from google.adk.tools import FunctionTool

@FunctionTool
def get_volume_profile(symbol: str, range_price: float) -> dict:
    """Volume profile analysis"""
    return {
        "high_volume_nodes": [23100, 23150, 23200],
        "poc": 23125,  # Point of Control
        "value_area_high": 23175,
        "value_area_low": 23075
    }
# BLOCK 5: config.py
python
# KiteConnect API Config (Add your keys)
KITE_API_KEY = "your_api_key"
KITE_ACCESS_TOKEN = "your_access_token"

# Trading Parameters
RISK_PER_TRADE = 0.02  # 2% risk
MAX_RR_RATIO = 1.5
TIMEFRAME = "15min"
BLOCK 6: requirements.txt
text
google-adk
kiteconnect==4.0.1
pandas==2.1.4
numpy==1.26.4
plotly==5.22.0
python-dateutil
BLOCK 7: README.md
text
# 🏦 Liquidity Trading Agent (Google ADK)

**NIFTY/BANKNIFTY Options Liquidity Zone Detector**

## 🚀 Quick Start
```bash
pip install -r requirements.txt
python main.py
Sample Output
text
**NIFTY 23100 CE Analysis**
-  Sell-side: 23,050-23,100 (HIGH)
-  Buy-side: 23,300-23,350 (MEDIUM)  
-  Bias: BULLISH above 23,150
Run on Replit

text

***

## **BLOCK 8: `deploy.sh`**
```bash
#!/bin/bash
echo "🚀 Deploying Liquidity Trading Agent..."
pip install -r requirements.txt
adk install
python main.py
echo "✅ Agent ready! Test with: python main.py"
🎯

# Test Command:
bash
unzip liquidity-trading-agent.zip
cd liquidity-trading-agent
chmod +x deploy.sh
./deploy.sh