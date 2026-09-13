"""Comparable-trade matching helpers for the validated AH-PF log."""

from __future__ import annotations


def confidence_from_sample_size(n: int) -> str:
    if n < 10:
        return "VERY_LOW"
    if n < 20:
        return "LOW"
    if n < 40:
        return "MODERATE"
    if n < 75:
        return "HIGH"
    return "STRONG"


def categorical_similarity(candidate: dict, historical: dict, weights: dict | None = None) -> float:
    weights = weights or {
        "ticker": 2.0, "dte_bucket": 1.5, "strategy": 2.0, "direction": 1.0,
        "regime": 1.5, "vol_bucket": 1.0, "gamma_regime": 1.0,
        "macro_bucket": 1.0, "time_bucket": 0.75, "trigger_type": 1.25,
    }
    total = sum(weights.values())
    if total == 0:
        return 0.0
    matched = sum(weight for key, weight in weights.items() if candidate.get(key) is not None and candidate.get(key) == historical.get(key))
    return matched / total


def comparable_summary(candidate: dict, history: list[dict], minimum_similarity: float = 0.6) -> dict:
    scored = [(categorical_similarity(candidate, row), row) for row in history]
    matches = [(score, row) for score, row in scored if score >= minimum_similarity]
    matches.sort(key=lambda item: item[0], reverse=True)
    net_pnls = [float(row.get("net_pnl_usd", 0.0)) for _, row in matches if row.get("net_pnl_usd") not in (None, "")]
    wins = sum(p > 0 for p in net_pnls)
    n = len(matches)
    return {
        "sample_size": n,
        "confidence": confidence_from_sample_size(n),
        "win_rate": (wins / len(net_pnls)) if net_pnls else None,
        "average_net_pnl_usd": (sum(net_pnls) / len(net_pnls)) if net_pnls else None,
        "matches": matches,
    }
