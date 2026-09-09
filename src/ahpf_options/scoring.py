"""A+ score and hard-veto decision layer."""

from __future__ import annotations

DEFAULT_WEIGHTS = {
    "price_structure_trigger": 20,
    "multi_timeframe_confirmation": 15,
    "market_regime_breadth": 15,
    "volatility_event_risk": 15,
    "options_economics": 20,
    "liquidity_execution": 10,
    "personal_historical_edge": 5,
}


def score_setup(component_fractions: dict[str, float], weights: dict[str, float] | None = None) -> float:
    weights = weights or DEFAULT_WEIGHTS
    score = 0.0
    for key, weight in weights.items():
        fraction = float(component_fractions.get(key, 0.0))
        score += max(0.0, min(1.0, fraction)) * weight
    return round(score, 2)


def decision(score: float, vetoes: list[str] | None = None, threshold: float = 90.0, trigger_pending: bool = False) -> str:
    if vetoes:
        return "NO TRADE"
    if trigger_pending or score < threshold:
        return "WAIT"
    return "A+ TRADE"
