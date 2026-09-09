"""Contextual gamma-level classification. Gamma levels are not deterministic signals."""

from __future__ import annotations


def classify_gamma_regime(spot: float, gamma_flip: float | None = None, call_wall: float | None = None, put_wall: float | None = None, atr_5m: float | None = None) -> dict:
    tolerance = max((atr_5m or 0.0) * 0.25, 0.01)
    result = {"spot": spot, "context_only": True}
    if gamma_flip is not None:
        result["gamma_flip_relation"] = "ABOVE" if spot > gamma_flip else "BELOW" if spot < gamma_flip else "AT"
        result["gamma_flip_distance_atr"] = None if not atr_5m else (spot - gamma_flip) / atr_5m
    if call_wall is not None:
        result["call_wall_relation"] = "NEAR" if abs(spot - call_wall) <= tolerance else "ABOVE" if spot > call_wall else "BELOW"
    if put_wall is not None:
        result["put_wall_relation"] = "NEAR" if abs(spot - put_wall) <= tolerance else "ABOVE" if spot > put_wall else "BELOW"
    return result
