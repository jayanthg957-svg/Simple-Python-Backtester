# Simple Python Backtester

## Overview
This is a miniature quantitative trading backtester built entirely from scratch using core Python (no Pandas or NumPy). It reads 1 year of historical daily stock data and simulates a trading strategy day-by-day to track portfolio growth.

## The Strategy: Moving Average Crossover
The script uses a trend-following momentum strategy:
* **The Indicators:** A 5-day Simple Moving Average (Fast Line) and a 20-day Simple Moving Average (Slow Line).
* **Buy Rule:** When the 5-day average crosses above the 20-day average, short-term momentum is rising, so the algorithm buys 1 share.
* **Sell Rule:** When the 5-day average drops below the 20-day average, momentum is dying, so the algorithm sells 1 share.

## Final Results
* **Starting Capital:** $1,000.00
* **Final Portfolio Value:** $ 1191.77
* **Total Profit/Loss:** $ 191.77

## Technical Learnings
Building this forced me to understand the underlying mechanics of how a backtester actually works line-by-line:
1. Handling historical data extraction using Python's built-in `csv` module.
2. Managing a double-entry virtual ledger (tracking both cash and shares simultaneously).
3. Preventing "look-ahead bias" by reversing the chronological order of CSV datasets before looping through them.
