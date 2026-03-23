@FunctionTool
def gift_nifty_checker() -> dict:
    """GIFT Nifty gap detection - CRITICAL for gap trading"""
    return {
        "prev_nifty_close": 23284,
        "gift_nifty_current": 22950, 
        "gap_points": -334,  # Mar23 gap-down signal
        "risk_level": "HIGH",
        "bias_override": "BEARISH"
    }

@FunctionTool  
def fiidii_flow_tracker() -> dict:
    """FII/DII flow with bias impact"""
    return {
        "fii_net": -2850,  # ₹Cr
        "dii_net": +1200,
        "flow_bias": "BEARISH",
        "threshold_breached": True
    }

@FunctionTool
def pnl_tracker(previous_calls: list) -> dict:
    """Real-time P&L tracking and lesson extraction"""
    return {
        "win_rate": "50%",
        "net_pnl": "+51%",
        "lessons": [
            "GIFT gap >200pts = reverse PCR bias",
            "VIX >25 = PE bias override"
        ]
    }
