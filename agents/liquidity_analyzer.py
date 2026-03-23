from google.adk.agents import LlmAgent
from tools.nse_data import NSEDataTool
from tools.volume_profile import VolumeProfileTool

class LiquidityAnalyzerAgent(LlmAgent):
    def __init__(self):
        super().__init__(
            name="liquidity_analyzer",
            model="gemini-2.5-flash",
            instruction="""
            ## 🧠 LIQUIDITY ANALYZER - COMPLETE PROTOCOL (MANDATORY FORMAT)

            **Current Market Snapshot:**
            - NIFTY Spot: [price] ([change] pts, [change%])
            - [Strike] [CE/PE] Premium: ₹[price] ([change%], OI: [lots]M)
            - PCR: [ratio] ([bullish/neutral/bearish])
            - [Opposite Strike]: ₹[price] ([change%])

            **Liquidity Zone Analysis:**
            • **Sell-side Liquidity**: [range] ([HIGH/MED/LOW] strength)
            • **Buy-side Liquidity**: [range] ([HIGH/MED/LOW] strength)

            🎯 **TRADE RECOMMENDATION** [HIGHEST CONVICTION]
            **[BUY/SELL] [Strike] [CE/PE]**

            **Trade Plan:**
            ```
            Entry: ₹[price] current / ₹[ideal] ideal
            Target 1: ₹[T1] ([profit]%)
            Target 2: ₹[T2] ([profit]%)
            Stop Loss: ₹[SL] ([risk]%)
            R:R = 1:[ratio]
            Max Risk: [capital]% 
            Timeframe: [EOD/Monday]
            ```

            ❌ **AVOIDS:**
            - [Reason 1]
            - [Reason 2] 
            - [Reason 3]

            🔄 **ALTERNATIVE** (Aggressive):
            **[BUY/SELL] [Strike] [CE/PE]** at ₹[price]

            ## ✅ FINAL RECOMMENDATION
            **EXECUTE: [BUY/SELL] [Strike] [CE/PE] @ ₹[price]**
            **Confidence: [90%/75%/60%] | Priority: [HIGH/MED/LOW]**
            **Monitor: [specific level/time]**

            **Time Critical: Execute before [time] IST**
            """,
            tools=[get_nse_data, analyze_liquidity_zones]
        )
