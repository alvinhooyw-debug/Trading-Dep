from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReliabilityEvidence:
    oos_predictions: int
    brier_score: float
    max_calibration_error: float
    net_expectancy: float
    represented_regimes: int
    leakage_check_passed: bool
    live_inputs_fresh: bool
    baseline_beaten: bool


@dataclass(frozen=True)
class ReliabilityPolicy:
    min_oos_predictions: int = 200
    max_brier_score: float = 0.22
    max_calibration_error: float = 0.08
    min_net_expectancy: float = 0.0
    min_represented_regimes: int = 2
    require_no_leakage: bool = True
    require_fresh_inputs: bool = True
    require_baseline_beaten: bool = True


@dataclass(frozen=True)
class ReliabilityDecision:
    approved_for_live_scoring: bool
    reasons: tuple[str, ...]


def evaluate_reliability(evidence: ReliabilityEvidence, policy: ReliabilityPolicy | None = None) -> ReliabilityDecision:
    p = policy or ReliabilityPolicy()
    reasons: list[str] = []
    if evidence.oos_predictions < p.min_oos_predictions:
        reasons.append("insufficient_oos_predictions")
    if evidence.brier_score > p.max_brier_score:
        reasons.append("brier_score_too_high")
    if evidence.max_calibration_error > p.max_calibration_error:
        reasons.append("calibration_error_too_high")
    if evidence.net_expectancy <= p.min_net_expectancy:
        reasons.append("non_positive_net_expectancy")
    if evidence.represented_regimes < p.min_represented_regimes:
        reasons.append("insufficient_regime_coverage")
    if p.require_no_leakage and not evidence.leakage_check_passed:
        reasons.append("leakage_check_failed")
    if p.require_fresh_inputs and not evidence.live_inputs_fresh:
        reasons.append("stale_live_inputs")
    if p.require_baseline_beaten and not evidence.baseline_beaten:
        reasons.append("baseline_not_beaten")
    return ReliabilityDecision(not reasons, tuple(reasons))
