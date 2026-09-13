# AH-PF Prediction & Validation V3

## Objective

V3 does not attempt to predict a single future price. It estimates probabilities for precisely defined outcomes and only allows a model to influence A+ scoring after it demonstrates stable out-of-sample performance, calibration, positive net expectancy after costs, and adequate regime coverage.

## Predictive layers

1. **Direction**: probability SPY/QQQ is higher or lower after 15, 30, 60 and 120 minutes.
2. **Range / touch**: probability an upper or lower level is touched during the horizon.
3. **Strike outcome**: probability the underlying finishes above/below a candidate strike.
4. **Trade outcome**: downstream research should map these forecasts to spread target/stop outcomes and net expectancy after fees/slippage.

## Feature snapshots

`FeatureSnapshot` is designed for five-minute observations and includes price returns, VWAP distance, RSI/RSI-MA, SQZMOM level/change, ATR, volume strength, multi-timeframe bias, VIX/VIX1D, 10Y yield, DXY, breadth, semiconductors, gamma distance, macro-event proximity and option-chain features.

Every candidate observation should be stored, including NO TRADE decisions. Recording only executed trades creates selection bias and leaves too little data for useful prediction research.

## Labels

Forward paths are labelled after the fact using future prices. Labels include future return, MFE, MAE, upper/lower touch and finish relative to strike. Feature generation must use only information available at the prediction timestamp. Future information may appear only in the label stage.

## Baseline model

V3 includes a dependency-free standardized logistic-regression baseline. This is intentional. More complex models must beat the simple baseline out-of-sample after estimated costs before they can be considered useful.

Future candidates may include gradient-boosted trees and ensembles, but complexity is not evidence of edge.

## Chronological validation

Random train/test splits are prohibited for time-series claims. Use expanding-window walk-forward evaluation. Training observations must always precede test observations.

Recommended development sequence:

- Train on older observations.
- Test on the next unseen block.
- Expand training window.
- Repeat.
- Keep a final untouched holdout where practical.

## Calibration

Accuracy alone is insufficient. If a model repeatedly forecasts 80%, outcomes in that forecast bucket should occur near 80% over a sufficiently large sample. Track Brier score, log loss and bucket-level calibration error.

## Reliability gate

Default gate before live scoring influence:

- at least 200 out-of-sample predictions
- Brier score <= 0.22
- maximum calibration error <= 0.08
- positive net expectancy after fees/slippage
- at least two represented regimes
- leakage checks passed
- live inputs fresh
- existing rule-based baseline beaten

These defaults are research thresholds, not guarantees of profitability.

## Model states

`EXPERIMENTAL -> OOS_VALIDATED -> SHADOW -> APPROVED`

A model first produces shadow forecasts that cannot alter trade decisions. Only an approved model may contribute to A+ scoring. It still cannot override a hard veto.

Models can be `DEMOTED` when calibration or expectancy deteriorates and `REJECTED` when evidence fails.

## Live safety boundary

- No model places brokerage orders.
- No model overrides risk limits or hard vetoes.
- Missing/stale inputs disable predictive influence.
- Event-risk rules remain separate from prediction output.
- Provider and broker integrations remain read-only/import-only.

## Practical next data step

The largest missing ingredient is data volume. Build read-only provider adapters that persist five-minute SPY/QQQ feature snapshots and historical option-chain observations. The prediction engine should remain in `shadow` mode until enough chronologically valid observations exist to pass the reliability gate.
