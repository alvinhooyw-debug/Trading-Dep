# AH-PF Self-Improvement Loop

AH-PF must improve by accumulating evidence, not by rewriting rules after a few wins or losses.

## Closed loop

1. Observe current market, option, macro and regime conditions.
2. Classify the setup before entry.
3. Preserve the exact recommendation, trigger, vetoes, score and assumptions.
4. Record actual entry and exit fills, fees and execution quality.
5. Calculate outcome diagnostics including net P/L, MAE, MFE, slippage and fee drag.
6. Compare the trade with prior validated observations.
7. Generate candidate insights only when a repeatable pattern appears.
8. Backtest the candidate using realistic execution assumptions.
9. Test it on unseen later data with walk-forward validation.
10. Paper-validate material strategy changes before approval.
11. Promote only evidence-backed rules into the live adviser protocol.

## Loss classification

Each losing trade should be assigned a primary cause:

- `strategy_loss`: valid setup, market moved against it.
- `execution_loss`: fill, slippage, late exit or order handling materially worsened the result.
- `rule_violation`: the trade should not have been opened under the standing protocol.
- `model_failure`: repeated evidence suggests a model assumption or rule is wrong.
- `exogenous_shock`: unscheduled information dominated the setup.

This prevents every loss from being mislabelled as a strategy failure.

## Evidence promotion

A newly discovered pattern starts as a candidate. It may move through:

`candidate -> backtested -> walk_forward_passed -> paper_validated -> approved`

It may be rejected at any stage.

No rule becomes approved only because in-sample performance improved. The default minimum comparable sample for a personal-edge claim is 40 trades, and stronger claims should require more observations. Small samples can still inform caution, but they should not dominate scoring.

## Anti-overfitting requirements

- Preserve an untouched out-of-sample period.
- Use realistic bid/ask, commissions and slippage.
- Never use data that was unavailable at the decision timestamp.
- Log serious rejected candidates and NO TRADE decisions where feasible.
- Keep training and test results separate.
- Prefer simple rules that survive multiple regimes over highly tuned parameter combinations.
- Do not automatically change risk limits or position sizing from recent P/L.

## External research

Ideas from exchanges, academic papers, professional analytics and open-source repositories are hypotheses, not AH-PF rules. Record their source, exact hypothesis, claimed conditions and reproduction status. Promote only after independent testing.
