# Trading-Dep

AH-PF research and decision-support repository for SPY/QQQ short-dated options.

This repository is for research, backtesting, market-regime analysis, trade logging, and improving future recommendations. It is not an autonomous trading bot and must not execute brokerage orders.

## Core mandate

- Instruments: SPY and QQQ.
- Primary workflow: 0DTE to 4DTE defined-risk option spreads.
- Default status: paper-trade and educational only until the portfolio mandate is explicitly changed.
- A+ threshold: minimum 8/10.
- Default size: 1 spread.
- Never average down or add contracts to rescue a trade.
- Prefer 1-point debit spreads when they cap risk cleanly.
- Reject weak credit-spread economics even when quoted probability of profit looks high.
- Use underlying-price invalidation, not option-premium hope.
- Avoid binary-event exposure unless the event has passed and structure confirms.
- Target roughly 50% to 80% of available profit instead of holding automatically for max profit.
- Return NO TRADE when no setup qualifies.

## Repository map

- `docs/RULEBOOK.md` canonical trading and risk rules.
- `config/a_plus_rules.yaml` machine-readable A+ scoring gates.
- `data/trades.csv` canonical validated trade log.
- `data/macro_events.csv` scheduled and unscheduled macro-event log.
- `templates/trade_review.md` end-of-session review template.

## Required adviser sequence

1. Review the rulebook.
2. Review comparable prior trades and NO TRADE sessions.
3. Review current macro and event risk.
4. Confirm live SPY/QQQ structure.
5. Confirm live option-chain economics.
6. Score the setup.
7. Trade only if score is at least 8/10 and every hard gate passes.
8. Log the outcome after the session.

## Important

Deposits are not profit. Crypto is excluded from this repository and from the stock/options recovery mandate.
