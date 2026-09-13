# Sources and research provenance

AH-PF uses original implementation. External research is treated as hypothesis/evidence input, not copied trading code.

## General policy

- Record source, date, instrument, sample period, assumptions and limitations for every external strategy claim.
- Separate SPX evidence from SPY/QQQ transfer validation.
- Do not treat claimed win rate as expected live performance.
- Include fees, slippage and settlement differences in reproduction work.
- New external ideas remain experimental until out-of-sample and paper validation gates pass.

## Predictive-model policy

- Feature values must be timestamped and available at prediction time.
- Future data may appear only in outcome labels, never in model inputs.
- Random train/test splits are not accepted for time-series performance claims.
- Use chronological expanding-window validation and, where practical, an untouched final holdout.
- Compare complex models against simple baselines before promotion.
- Track Brier score, log loss, calibration error, net expectancy after estimated costs and regime coverage.
- Predictive models run in shadow mode until the reliability gate passes.
- Approved predictive models remain subordinate to A+ hard vetoes and risk rules.

## Implementation boundary

No external code has been copied into the AH-PF implementation. Public research, exchange education and academic work may inform hypotheses and test design, while code remains original unless a future dependency is explicitly reviewed and documented with its license.
