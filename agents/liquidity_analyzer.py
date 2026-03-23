from google.adk.agents import LlmAgent
from tools.nse_data import NSEDataTool
from tools.volume_profile import VolumeProfileTool

class LiquidityAnalyzerAgent(LlmAgent):
    def __init__(self):
        super().__init__(
            name="liquidity_analyzer",
            model="gemini-2.5-flash",
            description="Identifies liquidity zones using SMC/ICT concepts",
            instruction="""
            LIQUIDITY ZONE ANALYSIS PROTOCOL:
            
            1. **Swing Structure**: Mark higher highs/lows, equal highs/lows
            2. **Sell-side Liquidity**: Below swing lows (24,200-24,250 type)
               - Long stops cluster here
               - Expect downside raid → upside reversal
            3. **Buy-side Liquidity**: Above swing highs (24,500-24,550 type)
               - Short stops cluster here  
               - Expect upside raid → potential downside
            4. **Zone Strength**: High/Medium/Low (volume + reactions)
            5. **Bias**: Bullish above structure break, Bearish below
            
            OUTPUT FORMAT:
            **NIFTY 1H Analysis**
            - Sell-side: [range] (strength) - Upside raid expected
            - Buy-side: [range] (strength) - Downside target
            - Bias: [direction] above [key level]
            """,
            tools=[NSEDataTool(), VolumeProfileTool()]
        )
