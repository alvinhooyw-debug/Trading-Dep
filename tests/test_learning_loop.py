from ahpf_options.analytics import TradeOutcome, summarize
from ahpf_options.insight_registry import InsightEvidence, InsightStage, eligible_for_promotion
from ahpf_options.walkforward import expanding_window_folds


def test_trade_summary_uses_net_results_and_fees():
    result = summarize([
        TradeOutcome(net_pnl=25, fees=5),
        TradeOutcome(net_pnl=-15, fees=5),
        TradeOutcome(net_pnl=10, fees=4),
    ])
    assert result["n"] == 3
    assert result["win_rate"] == 2 / 3
    assert result["expectancy"] == 20 / 3
    assert result["avg_fees"] == 14 / 3


def test_walk_forward_never_overlaps_test_with_training_future():
    folds = expanding_window_folds(n_obs=100, min_train=40, test_size=20)
    assert len(folds) == 3
    assert folds[0].train_end == folds[0].test_start == 40
    assert folds[-1].test_end == 100


def test_insight_requires_sample_and_positive_out_of_sample_expectancy():
    weak = InsightEvidence(sample_size=39, expectancy=10, out_of_sample_expectancy=8)
    assert not eligible_for_promotion(InsightStage.BACKTESTED, weak)

    overfit = InsightEvidence(sample_size=50, expectancy=10, out_of_sample_expectancy=-2)
    assert not eligible_for_promotion(InsightStage.BACKTESTED, overfit)

    credible = InsightEvidence(sample_size=50, expectancy=10, out_of_sample_expectancy=4)
    assert eligible_for_promotion(InsightStage.BACKTESTED, credible)
