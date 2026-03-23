
***

## **2. `backtest/backtest_engine.py`**
```python
#!/usr/bin/env python3
"""
Liquidity Trading Architect Backtest Engine v1.0
Tests agent logic across 4.5 years NIFTY data
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import argparse
import os

class LiquidityBacktester:
    def __init__(self, data_path='data/nifty_4yr_daily.csv'):
        self.data = pd.read_csv(data_path)
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.trades = []
        
    def agent_signal(self, row):
        """Simulate agent logic from instructions"""
        spot = row['Close']
        vix = row.get('VIX', 20)
        gift_gap = row.get('Gift_Gap', 0)
        fii_flow = row.get('FII_net_cr', 0)
        
        # RISK OVERRIDES (from agent instructions)
        if abs(gift_gap) > 200:
            return 'PE_BUY'  # Flip bias
        if vix > 25:
            return 'PE_BUY'
        if fii_flow < -2000:
            return 'PE_BUY'
            
        # Liquidity zones logic
        if spot < row['SMA_20']:  # Below structure
            return 'PE_BUY'
        else:
            return 'CE_BUY'
    
    def simulate_trade(self, signal, entry_date, spot):
        """Simulate 1-day hold P&L"""
        next_row = self.data[self.data['Date'] == entry_date + timedelta(days=1)]
        if next_row.empty:
            return 0
            
        exit_spot = next_row.iloc[0]['Close']
        if 'PE' in signal:
            pnl = (entry_spot - exit_spot) / entry_spot * 100
        else:
            pnl = (exit_spot - entry_spot) / entry_spot * 100
            
        return pnl
    
    def run_backtest(self, start_date='2021-10-01', end_date='2026-03-23'):
        """Full backtest execution"""
        test_data = self.data[
            (self.data['Date'] >= start_date) & 
            (self.data['Date'] <= end_date)
        ]
        
        for idx, row in test_data.iterrows():
            signal = self.agent_signal(row)
            pnl = self.simulate_trade(signal, row['Date'], row['Close'])
            
            self.trades.append({
                'Date': row['Date'],
                'Spot': row['Close'],
                'Signal': signal,
                'PnL_%': pnl
            })
        
        results = pd.DataFrame(self.trades)
        return self.calculate_metrics(results)
    
    def calculate_metrics(self, results):
        """Key performance metrics"""
        wins = results[results['PnL_%'] > 0]
        losses = results[results['PnL_%'] < 0]
        
        return {
            'Total Trades': len(results),
            'Win Rate': len(wins)/len(results)*100,
            'Avg Win': wins['PnL_%'].mean(),
            'Avg Loss': losses['PnL_%'].mean(),
            'Profit Factor': abs(wins['PnL_%'].sum() / losses['PnL_%'].sum()),
            'Max DD': (results['PnL_%'].cumsum().expanding().max() - 
                      results['PnL_%'].cumsum()).max(),
            'Sharpe Ratio': results['PnL_%'].mean() / results['PnL_%'].std()
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--period', choices=['6months', 'full'], default='6months')
    args = parser.parse_args()
    
    bt = LiquidityBacktester()
    if args.period == '6months':
        metrics = bt.run_backtest('2025-10-01', '2026-03-23')
    else:
        metrics = bt.run_backtest()
    
    print("\n🎯 BACKTEST RESULTS")
    print(metrics)
    pd.DataFrame(bt.trades).to_csv('results/backtest_results.csv', index=False)
