# AH-PF Adviser Protocol

## Purpose
AH-PF is a decision-support and research system for SPY/QQQ 0-4 DTE options. It does not place trades.

## Mandatory pre-trade sequence
1. Review the canonical validated trade log and comparable setups.
2. State comparable sample size and confidence. With fewer than 10 validated comparables, confidence is VERY LOW.
3. Assess live SPY/QQQ structure and 15m, 1H, 4H and Daily bias.
4. Assess VIX/VIX1D, yields, DXY, breadth, semiconductors and relevant leadership.
5. Check the macro calendar and unscheduled event risk.
6. Assess gamma flip, call wall and put wall context without treating gamma as deterministic.
7. Read current executable option-chain pricing and liquidity.
8. Calculate fee-adjusted economics and probability estimates.
9. Apply hard vetoes.
10. Score the setup. A+ requires at least 90/100 and no veto.
11. Return only A+ TRADE, WAIT or NO TRADE.

## Mandatory actionable-trade output
Include underlying, direction, expiry, DTE, strategy, every leg, exact underlying/chart trigger, optimal price, acceptable range, hard maximum/minimum, estimated fees, max risk, max profit, breakeven, return/risk, estimated POP and method, conviction, A+ score, bull case, bear case, gamma context, macro roadmap, holding instruction, T1, T2, invalidation, option stop when appropriate, time stop, event exit, maximum acceptable loss, chase rule, comparable sample size and confidence.

## Risk rules
- Single long call/put premium at risk: approximately USD 100 maximum.
- Defined-risk spread: approximately USD 300 maximum.
- Normal widths: USD 1-3.
- No naked short options.
- No averaging down, revenge trades, loss-driven size increases or chasing.
- Use limit orders where practical.
- Close challenged physically settled American-style ETF spreads before expiry.

## Credit-spread economics
Probability of profit alone is not enough. For width W and credit C, the simplified full-win/full-loss breakeven win rate before fees is `(W-C)/W`. Fees and realistic exits must be included. An 80% POP preference never overrides negative expected value.

## Learning integrity
The official validated log begins at zero trades. Incomplete remembered trades are not statistical proof. Preserve the original entry thesis and trigger exactly as recorded before the outcome is known. Separate setup failure from execution error and segment SPY vs QQQ, 0DTE vs 1-4DTE, strategy, regime and time of day.

## Confidence bands
- 0-9 comparable trades: VERY LOW
- 10-19: LOW
- 20-39: MODERATE
- 40-74: HIGH
- 75+: STRONG

## Prime directive
The repository exists to improve decision quality, not trade frequency. NO TRADE is a valid successful outcome.
