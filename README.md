# Trading-Dep

AH-PF research and decision-support repository for SPY/QQQ short-dated options.

This repository is for research, backtesting, market-regime analysis, trade logging, calibration, reporting, and improving future recommendations. It is not an autonomous trading bot and must not execute brokerage orders.

## Core mandate

- Instruments: SPY and QQQ.
- Primary workflow: 0DTE to 4DTE defined-risk option spreads.
- Default size: 1 spread.
- Never average down or add contracts to rescue a trade.
- Reject weak credit-spread economics even when quoted probability of profit looks high.
- Use underlying-price invalidation, not option-premium hope.
- Avoid binary-event exposure unless the event has passed and structure confirms.
- Return NO TRADE when no setup qualifies.

## Repository map

- `docs/RULEBOOK.md` canonical trading and risk rules.
- `docs/adviser_protocol.md` adviser decision sequence.
- `docs/self_improvement_loop.md` governed learning process.
- `docs/UPGRADES_V2.md` market-data, broker-ingestion, reporting and calibration architecture.
- `config/a_plus_rules.yaml` canonical machine-readable hard gates.
- `config/a_plus_scoring.yaml` detailed scoring weights.
- `config/risk_limits.yaml` risk constraints.
- `config/fees.yaml` fee assumptions used by research math.
- `config/data_sources.yaml` minimum live/read-only data requirements.
- `data/trades.csv` canonical validated trade log.
- `data/macro_events.csv` macro-event log.
- `data/templates/` research, trade, candidate and external-strategy schemas.
- `src/ahpf_options/` pricing, probability, regime, scoring, learning and reporting modules.
- `backtests/` standardized research-run schema.
- `tests/` unit tests run by GitHub Actions.

## V2 capabilities

- fee-aware vertical-spread economics and minimum-credit checks
- probability helpers and calibration diagnostics
- hard-veto A+ scoring
- macro event holding gate
- contextual gamma-regime classification
- comparable-trade confidence matching
- post-trade analytics and loss classification
- expanding-window walk-forward splits
- evidence-gated insight promotion
- read-only market-data adapter contracts with freshness checks
- broker-fill normalization and defined-risk vertical validation
- weekly edge reports by setup, symbol, DTE, entry hour and regime
- external-strategy registry with SPX-to-SPY/QQQ transfer-validation gates

## Required adviser sequence

1. Review the rulebook and comparable validated trades.
2. Review current macro and event risk.
3. Confirm fresh SPY/QQQ structure and market context.
4. Confirm current option-chain economics, liquidity and fees.
5. Score the setup and apply hard vetoes.
6. Trade only when the setup independently meets the A+ standard.
7. Import actual fills and fees after execution.
8. Diagnose the outcome without rewriting the original thesis.
9. Promote new rules only after backtest, out-of-sample and paper-validation gates.

## Safety boundary

Live provider adapters must remain read-only. Broker integrations are import-only. No module may submit, modify or cancel brokerage orders or handle trading credentials.

Deposits are not profit. Crypto is excluded from this repository and from the stock/options recovery mandate.
