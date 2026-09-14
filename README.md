# Trading-Dep

AH-PF research and decision-support repository for SPY/QQQ short-dated options.

This repository is for research, backtesting, market-regime analysis, trade logging, calibration, reporting, predictive validation, and improving future recommendations. It is not an autonomous trading bot and must not execute brokerage orders.

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
- `docs/PREDICTION_V3.md` predictive research, walk-forward validation and reliability gates.
- `docs/STRATEGY_EXPERIMENTS.md` external strategy hypotheses, adaptations and test plans.
- `config/a_plus_rules.yaml` canonical machine-readable hard gates.
- `config/a_plus_scoring.yaml` detailed scoring weights.
- `config/risk_limits.yaml` risk constraints.
- `config/fees.yaml` fee assumptions used by research math.
- `config/data_sources.yaml` minimum live/read-only data requirements.
- `config/prediction_v3.yaml` shadow-mode predictor governance and promotion thresholds.
- `config/strategy_experiments.yaml` parameter grids and promotion rules for experimental strategy families.
- `data/trades.csv` canonical validated trade log.
- `data/macro_events.csv` macro-event log.
- `data/external_strategies.csv` registered external strategy hypotheses and validation state.
- `data/templates/` research, trade, candidate, prediction and external-strategy schemas.
- `src/ahpf_options/` pricing, probability, regime, scoring, learning, prediction and reporting modules.
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

## V3 prediction and validation

V3 adds a shadow predictive layer. It does not influence A+ decisions until it passes the reliability gate.

- five-minute feature snapshots for price, momentum, volatility, multi-timeframe bias, macro, gamma and option-chain context
- forward-path labels for 15/30/60/120-minute research, level touches and strike outcomes
- dependency-free standardized logistic-regression baseline
- chronological expanding-window predictive evaluation
- Brier score, log loss and calibration tracking
- model lifecycle: `EXPERIMENTAL -> OOS_VALIDATED -> SHADOW -> APPROVED`
- reliability gate requiring adequate OOS sample, calibration, positive net expectancy, regime coverage, no leakage, fresh inputs and baseline outperformance
- prediction journal template for comparing forecasts with realized outcomes
- approved models still cannot override risk limits, event gates or hard vetoes

Current V3 mode is **shadow** and `live_scoring_enabled` is false. This is deliberate until the repository has enough clean historical and live observations to prove predictive value.

## Experimental strategy families

External strategy ideas are never promoted straight into A+ rules. The current research registry includes:

- structure-aligned OTM credit spreads: test whether selling beyond confirmed support/resistance improves fee-adjusted expectancy versus delta/distance-only selection
- 7-10 DTE trend credit spreads: a separate family testing whether lower gamma exposure improves expectancy and realized tail risk versus matched 0DTE and 1-4 DTE setups

Both remain `CANDIDATE` and have `live_trade_influence: false` until they pass reproduction, chronological OOS, reliability and paper-validation gates.

## Required adviser sequence

1. Review the rulebook and comparable validated trades.
2. Review current macro and event risk.
3. Confirm fresh SPY/QQQ structure and market context.
4. Confirm current option-chain economics, liquidity and fees.
5. Score the setup and apply hard vetoes.
6. If an approved predictive model exists, use its calibrated probability only as an additional scoring input.
7. Trade only when the setup independently meets the A+ standard.
8. Import actual fills and fees after execution.
9. Diagnose the outcome without rewriting the original thesis.
10. Promote new rules or models only after out-of-sample and shadow-validation gates.

## Safety boundary

Live provider adapters must remain read-only. Broker integrations are import-only. No module may submit, modify or cancel brokerage orders or handle trading credentials.

Deposits are not profit. Crypto is excluded from this repository and from the stock/options recovery mandate.
