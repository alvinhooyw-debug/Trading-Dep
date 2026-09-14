# AH-PF Strategy Experiments

This document records external strategy ideas that are useful enough to test but not trusted enough to influence live A+ decisions.

## Governance

All experiments begin as `CANDIDATE`. They must be reproduced, tested chronologically out-of-sample, evaluated after fees/slippage, paper-validated, and pass the V3 reliability gate before promotion. No experiment may override hard risk vetoes.

## 1. Structure-aligned OTM credit spreads

Source idea: Austin Bouley, summarized from a YouTube video supplied by the user.

### Hypothesis
Trend-aligned OTM credit spreads placed beyond confirmed support/resistance will produce better fee-adjusted expectancy than spreads selected mainly by delta or arbitrary distance.

### What is retained
- Defined-risk credit spreads.
- Trade with prevailing trend.
- Place the short strike beyond meaningful support/resistance.
- Exit when the underlying invalidates the thesis.
- Prefer high-probability structures only when premium adequately compensates risk.

### What is not adopted blindly
- MA10 alone is not sufficient trend confirmation.
- A fixed $20-$25 credit target is not portable across spread widths.
- Planned stop-loss risk is not maximum risk.
- A short-strike breach is an emergency condition, not necessarily the best first stop.

### AH-PF adaptation
Use multi-timeframe alignment, VWAP/structure, regime, macro proximity, option-chain economics, delta, liquidity, fees and credit-to-width instead of a single moving average or fixed premium target.

Risk must be recorded three ways:
1. contractual maximum loss,
2. planned stop loss,
3. stress-case loss including slippage.

Test short-delta bands 0.05-0.10, 0.10-0.15, 0.15-0.20 and 0.20-0.25; widths $1-$3; and multiple credit-to-width buckets.

## 2. 7-10 DTE trend credit spreads

### Hypothesis
A separate 7-10 DTE trend-aligned credit-spread family may deliver better fee-adjusted expectancy and lower realized tail loss than comparable 0DTE structures because gamma risk is lower and the thesis has more time to develop.

### Separation from core system
This is not an extension of the 0DTE mandate. It is a distinct experiment and must be reported separately.

### Initial test specification
- Underlyings: SPY and QQQ.
- DTE: 7-10.
- Trend: require at least 1H and 4H alignment; MA10 is only a feature.
- Short strike: beyond confirmed support/resistance.
- Short-delta test bands: 0.10-0.15, 0.15-0.20, 0.20-0.25.
- Widths: $1, $2 and $3.
- Profit-capture test points: 50%, 60% and 70% of collected credit.
- Avoid untested binary-event exposure.
- Technical invalidation remains primary.

### Comparison groups
Compare against matched 0DTE and 1-4 DTE structure-aligned credit spreads using similar underlying regime and structural setup.

## Promotion criteria
An experiment stays out of live A+ scoring until it passes the V3 reliability gate. At minimum it must show positive net expectancy after realistic fees/slippage, acceptable calibration, enough out-of-sample observations, more than one represented regime, no data leakage, and performance superior to the existing rule-based baseline.
