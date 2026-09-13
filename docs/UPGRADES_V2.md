# AH-PF V2 Upgrades

## Purpose

V2 turns the repository from a rules-and-research scaffold into a more complete decision-support platform while preserving the boundary that it does not place trades.

## 1. Read-only market data layer

`src/ahpf_options/market_data.py` defines normalized quote, option quote and market snapshot objects plus freshness validation. Provider-specific integrations should implement `MarketDataAdapter` and remain read-only.

Live A+ decisions should fail closed when quote timestamps are missing or stale.

## 2. Broker fill ingestion

`src/ahpf_options/broker_ingestion.py` normalizes fills and validates two-leg defined-risk verticals. It can calculate trade cashflows after fees from imported fills.

This is import-only. No order placement or credential handling is allowed.

## 3. Weekly edge reporting

`src/ahpf_options/reports.py` produces overall and segmented statistics by setup, symbol, DTE, entry hour and regime. The intended weekly report should track:

- trade count and win rate
- expectancy
- total net P/L
- fee drag
- SPY vs QQQ
- 0DTE vs 1-4DTE
- setup family
- entry time
- market regime

NO TRADE decisions should be reviewed separately so restraint can be measured rather than ignored.

## 4. Probability calibration

`src/ahpf_options/calibration.py` adds Brier score and calibration bins. This allows the system to answer whether claimed POP and conviction estimates are actually calibrated.

Example: trades forecast near 80% POP should eventually win near 80% under comparable definitions, or the probability model must be revised.

## 5. External strategy registry

`src/ahpf_options/external_strategy_registry.py` stores external research as hypotheses rather than accepted rules. Evidence from SPX must not be silently transferred to SPY or QQQ.

Promotion path:

`CANDIDATE -> REPRODUCED -> OOS_VALIDATED -> PAPER_VALIDATED -> APPROVED`

Negative out-of-sample or paper expectancy sends a strategy to `REJECTED`.

## 6. Data-source policy

`config/data_sources.yaml` defines the minimum fields for live market snapshots, imported broker fills and macro releases. Live recommendations should use current data and reject stale pricing.

## Next implementation phase

Provider-specific adapters can now be added without contaminating the research logic. Priorities are:

1. reliable SPY/QQQ underlying and option-chain feed
2. VIX/VIX1D, Treasury, DXY, breadth and SOX inputs
3. Moomoo statement/fill importer
4. scheduled macro-event importer
5. persistent report generation and dashboards
6. realistic historical option-chain ingestion for walk-forward backtests

## Safety boundary

The repository remains research, journaling, backtesting and decision support only. It must not submit, modify or cancel brokerage orders.
