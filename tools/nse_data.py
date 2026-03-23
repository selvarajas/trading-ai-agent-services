from google.adk.tools import FunctionTool
from kiteconnect import KiteConnect  # For Indian markets

@FunctionTool
def get_nse_data(symbol: str, timeframe: str = "1hour") -> dict:
    """Fetches OHLCV data for NSE symbols (NIFTY, BANKNIFTY)"""
    # Mock implementation - replace with real KiteConnect
    if symbol.upper() == "NIFTY":
        return {
            "symbol": "NIFTY",
            "timeframe": timeframe,
            "data": [
                {"timestamp": "2026-03-22 15:00", "open": 24250, "high": 24300, "low": 24200, "close": 24280, "volume": 1500000},
                {"timestamp": "2026-03-22 16:00", "open": 24280, "high": 24350, "low": 24210, "close": 24320, "volume": 1800000}
            ],
            "swing_high": 24350,
            "swing_low": 24200
        }
    return {"error": "Symbol not supported"}

@FunctionTool  
def analyze_liquidity_zones(ohlcv_data: list, symbol: str) -> dict:
    """Identifies buy/sell liquidity zones from OHLCV"""
    lows = [candle["low"] for candle in ohlcv_data]
    highs = [candle["high"] for candle in ohlcv_data]
    
    sell_side = f"{min(lows)-50}-{min(lows)+10}"
    buy_side = f"{max(highs)-10}-{max(highs)+50}"
    
    return {
        "sell_side_liquidity": sell_side,
        "buy_side_liquidity": buy_side,
        "structure_break": sum(1 for h, l in zip(highs, lows) if h > highs[0] and l > lows[0])
    }
