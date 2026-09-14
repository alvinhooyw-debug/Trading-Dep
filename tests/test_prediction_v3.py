from datetime import datetime

from ahpf_options.calibration import brier_score
from ahpf_options.feature_store import FeatureSnapshot
from ahpf_options.labeling import binary_target, label_forward_path
from ahpf_options.model_registry import next_model_state
from ahpf_options.predictor import StandardizedLogisticRegression
from ahpf_options.reliability_gate import ReliabilityEvidence, evaluate_reliability
from ahpf_options.walkforward_model import walk_forward_logistic


def test_forward_labeling():
    outcome = label_forward_path(100.0, [101.0, 99.0, 102.0], upper_level=101.5, lower_level=99.5, strike=101.0)
    assert round(outcome.future_return, 4) == 0.02
    assert outcome.touched_upper is True
    assert outcome.touched_lower is True
    assert binary_target(outcome, "finished_above_strike") == 1


def test_feature_snapshot_vector():
    snap = FeatureSnapshot(
        datetime(2026, 9, 10, 10, 0), "QQQ", 710.0, 0.001, -0.002, -0.001,
        48.0, 52.0, -1.2, -0.3, 0.0015, 0.8, -1, -1, -1, 1,
        17.5, 18.0, 4.4, 0.1, -0.5, -1.0, 0.002, 90.0, 0.25, 0.18,
        0.05, 0.003, 0.0, 45.0,
    )
    assert len(snap.numeric_vector()) > 20


def test_logistic_predictor_learns_simple_signal():
    X = [[-2.0], [-1.0], [-0.5], [0.5], [1.0], [2.0]]
    y = [0, 0, 0, 1, 1, 1]
    model = StandardizedLogisticRegression(learning_rate=0.1, epochs=800).fit(X, y)
    assert model.predict_proba_one([1.5]) > 0.7
    assert model.predict_proba_one([-1.5]) < 0.3


def test_walk_forward_is_chronological_and_scores():
    X = [[float(i)] for i in range(30)]
    y = [0 if i < 15 else 1 for i in range(30)]
    result = walk_forward_logistic(X, y, min_train_size=10, test_size=5, step_size=5, model_kwargs={"epochs": 100})
    assert result.predictions == 20
    assert 0 <= result.brier <= 1
    assert 0 <= result.accuracy <= 1
    assert brier_score(result.forecasts, result.outcomes) == result.brier


def test_reliability_gate_blocks_weak_model_and_approves_strong_one():
    weak = ReliabilityEvidence(50, 0.30, 0.20, -1.0, 1, True, True, False)
    assert evaluate_reliability(weak).approved_for_live_scoring is False

    strong = ReliabilityEvidence(300, 0.18, 0.05, 4.0, 3, True, True, True)
    assert evaluate_reliability(strong).approved_for_live_scoring is True


def test_model_promotion_requires_shadow_and_reliability():
    assert next_model_state("EXPERIMENTAL", oos_pass=True) == "OOS_VALIDATED"
    assert next_model_state("OOS_VALIDATED", oos_pass=True, shadow_pass=True) == "SHADOW"
    assert next_model_state("SHADOW", oos_pass=True, shadow_pass=True, reliability_pass=True) == "APPROVED"
