# AH-PF Canonical Rulebook

## 1. Purpose

This system supports research and discretionary decision-making for SPY and QQQ short-dated options. It does not place trades automatically.

## 2. Portfolio mandate

- Real-money short-dated options remain suspended unless the user explicitly changes the mandate.
- Paper-trade and educational analysis is the default.
- Stock/options recovery target is separate from crypto.
- Deposits do not count as trading profit.

## 3. Instruments and structures

Preferred instruments:
- SPY
- QQQ

Preferred structures:
- 1-point call debit spread
- 1-point put debit spread
- Defined-risk credit spread only when credit economics are attractive and event risk is acceptable

Avoid:
- Naked options
- Undefined-risk structures
- Averaging down
- Adding contracts to rescue a losing setup
- Trades entered only because probability-of-profit looks high

## 4. A+ hard gates

A setup cannot qualify unless every applicable gate passes.

1. Score at least 8/10.
2. Live underlying structure is confirmed.
3. Live option-chain bid/ask is available and executable.
4. Reward/risk is acceptable after fees.
5. No unresolved binary event is about to hit the position.
6. Entry is not a chase after an extended move.
7. Underlying invalidation is defined before entry.
8. Default size is 1 spread.
9. No averaging or adding after entry.
10. Trade fits current market regime.

If any hard gate fails, return NO TRADE.

## 5. Market-regime checklist

Before every trade review:

- SPY and QQQ trend on 5m, 15m, 1H, 4H, Daily
- Market breadth
- VIX and VIX1D when available
- SPX gamma positioning when available
- Treasury yields, especially 2Y and 10Y
- Fed expectations
- DXY
- Oil
- Gold
- Bitcoin as cross-asset signal only
- SOX / semiconductor strength
- SPY and QQQ flows when available
- Earnings calendar
- Major scheduled macro releases
- Unscheduled geopolitical or market-moving headlines

## 6. Technical confirmation

Do not trade a macro opinion by itself.

For bullish continuation:
- Break or reclaim of a meaningful level
- 5-minute confirmation
- Successful hold or retest
- Higher low or continuation structure
- Volume and momentum should support the move

For bearish continuation:
- Breakdown of meaningful support
- Failed reclaim or lower high
- 5-minute confirmation
- Selling pressure should remain present

Price gets the final vote when macro and tape disagree.

## 7. Debit-spread rules

Prefer 1-point debit spreads when they keep maximum loss small.

General target:
- Maximum debit around $0.35 to $0.40 when structure and strikes allow
- Do not force the trade simply to meet this debit
- Maximum loss equals debit paid x 100, plus fees
- Maximum profit equals spread width less debit, x 100, minus fees

Profit-taking:
- Usually capture roughly 50% to 80% of available spread profit
- Do not automatically hold for maximum expiry value

Exit:
- Use underlying-price invalidation first
- Exit if the technical thesis fails even if the option spread has not reached theoretical max loss

## 8. Credit-spread rules

Credit spreads require more than a high quoted probability of profit.

Reject when:
- Credit is too small relative to max loss
- Short strike is too close to live structure
- Event or headline risk is high
- Spread is illiquid
- Reward does not justify tail risk

Target economics should generally provide enough gross return on risk to justify execution and fees. A nominal 80% POP is not sufficient by itself.

## 9. Position sizing

Default:
- 1 contract / spread

Never:
- Add a second contract because the first is losing
- Average the entry price
- Increase size to recover a prior loss

## 10. Binary-event policy

Avoid new 0DTE exposure immediately before:
- CPI
- PPI
- FOMC rate decision
- Fed press conference
- Payrolls
- Major scheduled policy announcements
- Known company-specific binary events affecting QQQ/SPY materially

After the event:
- Wait for price structure to settle
- Prefer at least two 5-minute candles when volatility is extreme
- Reassess yields, VIX, DXY and breadth

## 11. Fees

Always account for fees on both entry and exit when estimating net P/L.

Report:
- Gross debit/credit
- Estimated entry fees
- Estimated exit fees
- Net expected profit
- Net maximum loss where relevant

## 12. Trade scoring

Suggested 10-point scale:

- Regime alignment: 0 to 2
- Technical structure: 0 to 2
- Trigger/retest quality: 0 to 2
- Option economics: 0 to 2
- Macro/event risk: 0 to 1
- Relative strength/weakness and confirmation: 0 to 1

Minimum qualifying score: 8/10.

A score does not override a failed hard gate.

## 13. Lessons already learned

- Do not manufacture high probability with poor reward/risk.
- Do not chase a move after it has already expanded.
- Do not short bullish price action only because the news sounds bearish.
- Do not buy bullish exposure only because price is green without confirmation.
- Overnight and forced-liquidation risk matter.
- Misclicks and accidental multiple-contract entries are serious execution risks.
- Low-credit spreads can be correctly directional and still be bad trades.
- A NO TRADE session is a valid outcome.

## 14. Required output for every qualifying setup

- Ticker
- Direction
- Exact spread and expiry
- Required underlying trigger
- Required confirmation
- Maximum acceptable debit or minimum acceptable credit
- Maximum profit
- Maximum loss
- Breakeven
- Estimated probability / edge
- Profit-taking level
- Hard invalidation / exit
- Macro and news risks
- A+ score

If no setup reaches 8/10 after all hard gates, output NO TRADE.
