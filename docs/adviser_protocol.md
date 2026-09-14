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
9. Apply thesis-failure / expected-move-failure checks before final scoring.
10. Apply hard vetoes and the mandatory A+ credit-spread gates below. A failed gate cannot be rescued by directional conviction or score averaging.
11. Score the setup. A+ requires at least 90/100 AND every mandatory gate to pass.
12. Return only A+ TRADE, WAIT or NO TRADE.

## Mandatory A+ credit-spread gates
For the user's core high-POP 0DTE credit-spread mandate, every item below is pass/fail. If any required item fails or cannot be verified with fresh data, the output is WAIT or NO TRADE, never A+.

1. **Freshness gate:** Current underlying price, completed intraday candles, current option chain, bid/ask, short-leg delta and event calendar must be fresh enough for the decision. Stale or unavailable chain economics means no trigger.
2. **High-POP gate:** Target approximately 80% or better modeled POP. Short-leg absolute delta around 0.15-0.20 may be used only as a rough probability proxy, never as proof of POP. A materially higher short delta requires independently modeled evidence that still satisfies the high-POP mandate.
3. **Economics gate:** Credit, width, fees, slippage, planned exits and tail loss must produce positive estimated expectancy. For the current one-contract fee assumptions, approximate screening floors for an 80% full-win/full-loss profile are $0.26 on $1-wide, $0.46 on $2-wide and $0.66 on $3-wide. These are screening floors, not automatic approval. A spread below the applicable floor cannot be labelled A+ unless a more complete documented exit model demonstrates positive net expectancy and the high-POP requirement still passes.
4. **Follow-through gate:** Directional conditions alone are insufficient. After the trigger/rejection, require actual price acceptance in the thesis direction, normally a completed 5-minute structural break plus follow-through or a failed reclaim. Mere RSI rollover, SQZMOM deceleration, resistance contact, or higher-timeframe bearish/bullish bias is not confirmation by itself.
5. **Thesis-failure gate:** If price has multiple reasons to move in the thesis direction but refuses to do so, treat that resilience as adverse evidence. Unresolved thesis-failure warnings automatically block A+.
6. **Countertrend gate:** When the execution timeframe or 15-minute structure flips against the proposed trade while higher timeframes still support it, do not use the higher timeframes to override the conflict. Require a fresh trigger and renewed acceptance before reconsideration.
7. **Risk gate:** Defined-risk spread must remain within the approximately USD300 maximum risk and must have a pre-defined technical invalidation, option-loss rule, time stop and event rule.
8. **No stale-strike gate:** Any material underlying move, BOS/CHoCH, volatility change or thesis failure requires fresh strike selection, delta, POP and credit. Never reuse an earlier candidate spread after the market state changes.

### Anti-overconfidence rule
A numerical A+ score is subordinate to the gates. A 90+ score cannot turn a failed POP, economics, freshness, follow-through, thesis-failure or risk gate into an A+ trade. If evidence conflicts, prefer WAIT/NO TRADE. The system is optimized for avoiding large asymmetric losses, not maximizing trade count.

## Thesis-failure / expected-move-failure rule
A setup must be downgraded when price fails to behave in the direction the thesis reasonably expects. Failure to follow through is not neutral information.

For a bearish setup, explicitly watch for:
- expected downside failing to materialize within several completed 5-minute candles after the trigger or rejection;
- bearish momentum indicators weakening while price itself refuses to make meaningful lower lows;
- higher lows forming into a repeatedly tested resistance level;
- reversal structures such as a double top failing to confirm through the neckline;
- 15-minute bias flipping bullish against a still-bearish 1H/4H/Daily backdrop;
- VIX falling or DXY/cross-asset conditions becoming more supportive for equities while price remains resilient;
- repeated resistance tests being absorbed without downside follow-through;
- a bullish BOS with volume or momentum re-expansion after the bearish setup stalls.

For a bullish setup, apply the exact mirror logic.

### Mandatory response to thesis failure
- Reduce conviction and A+ score immediately when the expected move fails.
- Do not keep recycling the original setup simply because higher-timeframe bias still agrees.
- If no follow-through occurs within roughly 3-5 completed 5-minute candles, treat the stalled setup as degraded unless a fresh trigger forms.
- If a failed setup is followed by opposite-direction BOS/CHoCH, higher-low/lower-high continuation structure, and momentum/volume re-expansion, mark the original thesis INVALIDATED and raise opposite-breakout risk.
- Recalculate strike selection, POP and option economics after any material thesis failure. Do not reuse stale deltas or credits.
- A setup with unresolved thesis-failure warnings cannot qualify as A+.

## Mandatory actionable-trade output
Include underlying, direction, expiry, DTE, strategy, every leg, exact underlying/chart trigger, optimal price, acceptable range, hard maximum/minimum, estimated fees, max risk, max profit, breakeven, return/risk, estimated POP and method, conviction, A+ score, bull case, bear case, gamma context, macro roadmap, holding instruction, T1, T2, invalidation, option stop when appropriate, time stop, event exit, maximum acceptable loss, chase rule, comparable sample size and confidence.

For every proposed credit spread, also show a compact **gate card** with PASS/FAIL/UNKNOWN for Freshness, High-POP, Economics, Follow-through, Thesis-failure, Countertrend, Risk and Stale-strike. Any FAIL or required UNKNOWN means the trade cannot be A+.

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

Thesis-failure events should be logged even when no trade is taken. Record the expected move, the number of completed 5-minute candles without follow-through, structure changes, 15m bias changes, momentum behavior, VIX/DXY changes, opposite-direction BOS/CHoCH, and whether the opposite move subsequently continued. These observations are research inputs, not proof of edge until validated out-of-sample.

## Confidence bands
- 0-9 comparable trades: VERY LOW
- 10-19: LOW
- 20-39: MODERATE
- 40-74: HIGH
- 75+: STRONG

## Prime directive
The repository exists to improve decision quality, not trade frequency. NO TRADE is a valid successful outcome.
