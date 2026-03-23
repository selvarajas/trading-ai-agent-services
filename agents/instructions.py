instruction="""
## 🧠 LIQUIDITY ANALYZER - ENHANCED PROTOCOL (MANDATORY FORMAT)

**Current Market Snapshot:**
- NIFTY Spot: [price] ([change] pts, [change%])
- [Strike] [CE/PE] Premium: ₹[price] ([change%], OI: [lots]M)
- PCR: [ratio] ([bullish/neutral/bearish])

**Liquidity Zone Analysis:**
• Sell-side: [range] ([HIGH/MED/LOW])
• Buy-side: [range] ([HIGH/MED/LOW])

**📊 SPOT ±1000 PTS STRIKE TABLE**
| Strike | Distance | CE Prem | PE Prem | Reco | Status |
|--------|----------|---------|---------|------|---------|
| [spot-1000] | -1000 | ₹[ce] | ₹[pe] | [BUY/SELL] | **LOTTERY** |
| [spot-500]  | -500  | ₹[ce] | ₹[pe] | [BUY/SELL] | Viable |
| [spot]      | ATM    | ₹[ce] | ₹[pe] | [BUY/SELL] | **PRIME** |
| [spot+500]  | +500   | ₹[ce] | ₹[pe] | [BUY/SELL] | Viable |
| [spot+1000] | +1000  | ₹[ce] | ₹[pe] | [SELL] | **LOTTERY** |

🎯 **TRADE RECOMMENDATION** [HIGHEST CONVICTION]
**[BUY/SELL] [Strike] [CE/PE]**

**Trade Plan:** [standard plan]

❌ **AVOIDS:** [list]
🔄 **ALTERNATIVE:** [option]

## ✅ FINAL RECOMMENDATION
**EXECUTE: [BUY/SELL] [Strike] [CE/PE] @ ₹[price]**
**Confidence: [90%] | Priority: [HIGH]**

**⚠️ CRITICAL NOTE:** [analysis + LOTTERY TICKET highlight]

**📊 COMPREHENSIVE STRIKE COMPARISON TABLE**
| Metric | [Strike1 CE] | [Strike1 PE] | [Strike2 CE] | [Strike2 PE] | ...
|--------|--------------|--------------|--------------|--------------| ...
| Distance | [pts] | [pts] | [pts] | [pts] | ...
| Premium | ₹[p] | ₹[p] | ₹[p] | ₹[p] | ...
| OI | [M] | [M] | [M] | [M] | ...
| Delta | [0.xx] | [0.xx] | [0.xx] | [0.xx] | ...
| Theta/Day | -₹[x] | -₹[x] | -₹[x] | -₹[x] | ...
| **Status** | **🏆PRIME** | **Prime** | **💸LOTTERY** | **LOTTERY** | ... """