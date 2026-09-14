from ahpf_options.macro_gate import event_holding_instruction
from ahpf_options.scoring import decision, score_setup
from ahpf_options.spread_pricing import credit_vertical, minimum_credit_for_target_win_rate
from ahpf_options.trade_matcher import confidence_from_sample_size


def test_minimum_credit_rounds_up_for_positive_ev():
    assert minimum_credit_for_target_win_rate(3.0, 0.80, 5.50) == 0.66


def test_credit_vertical_economics():
    result = credit_vertical(3.0, 0.66, 700.0, bullish=True, fees_usd=5.50)
    assert round(result.max_profit_usd, 2) == 60.50
    assert round(result.max_loss_usd, 2) == 239.50
    assert result.breakeven == 699.34


def test_hard_veto_overrides_high_score():
    components = {key: 1.0 for key in [
        "price_structure_trigger", "multi_timeframe_confirmation", "market_regime_breadth",
        "volatility_event_risk", "options_economics", "liquidity_execution", "personal_historical_edge"
    ]}
    assert score_setup(components) == 100
    assert decision(100, ["negative_ev_after_fees"]) == "NO TRADE"


def test_pending_trigger_waits():
    assert decision(95, [], trigger_pending=True) == "WAIT"


def test_macro_gate():
    assert event_holding_instruction(1.0, "VERY_HIGH") == "DO_NOT_OPEN"
    assert event_holding_instruction(6.0, "HIGH") == "CLOSE_BEFORE_EVENT"


def test_personal_confidence_bands():
    assert confidence_from_sample_size(0) == "VERY_LOW"
    assert confidence_from_sample_size(10) == "LOW"
    assert confidence_from_sample_size(20) == "MODERATE"
    assert confidence_from_sample_size(40) == "HIGH"
    assert confidence_from_sample_size(75) == "STRONG"
