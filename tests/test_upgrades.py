from datetime import datetime, timedelta, timezone

from ahpf_options.broker_ingestion import BrokerFill, aggregate_trade_cashflow, validate_defined_risk_vertical
from ahpf_options.calibration import brier_score, calibration_bins
from ahpf_options.external_strategy_registry import ExternalStrategy, TransferEvidence, StrategyStatus, requires_transfer_validation, strategy_status
from ahpf_options.market_data import MarketSnapshot, Quote, validate_freshness
from ahpf_options.reports import TradeRecord, weekly_edge_report


def test_market_freshness_gate():
    now = datetime.now(timezone.utc)
    snap = MarketSnapshot(Quote("QQQ", 700.0, timestamp=now - timedelta(seconds=10)), [])
    ok, _ = validate_freshness(snap, max_age_seconds=60)
    assert ok


def test_broker_vertical_and_cashflow():
    t = datetime.now(timezone.utc)
    fills = [
        BrokerFill("T1", t, "QQQ", "2026-09-10", 712, "C", "SELL", 1, 0.42, 1.0),
        BrokerFill("T1", t, "QQQ", "2026-09-10", 714, "C", "BUY", 1, 0.20, 1.0),
    ]
    ok, _ = validate_defined_risk_vertical(fills)
    assert ok
    assert round(aggregate_trade_cashflow(fills)["T1"], 2) == 20.0


def test_calibration_metrics():
    assert round(brier_score([0.8, 0.2], [1, 0]), 4) == 0.04
    bins = calibration_bins([0.8, 0.7, 0.2], [1, 0, 0], bins=2)
    assert sum(b.count for b in bins) == 3


def test_external_strategy_transfer_gate():
    s = ExternalStrategy("x", "paper", "SPX", "QQQ", "credit_spread", "test")
    assert requires_transfer_validation(s)
    assert strategy_status(TransferEvidence(reproduced_trades=100, oos_trades=50, oos_expectancy=1.0, paper_trades=25, paper_expectancy=0.5)) == StrategyStatus.APPROVED


def test_weekly_edge_report_groups():
    rows = [
        TradeRecord("BCS", "QQQ", 0, 20.0, 5.0, 11, "bearish"),
        TradeRecord("CDS", "QQQ", 2, -139.0, 5.0, 14, "mixed"),
    ]
    report = weekly_edge_report(rows)
    assert report["overall"].trades == 2
    assert "BCS" in report["by_setup"]
