"""Simple configurable macro-event holding gate for research workflows."""

from __future__ import annotations


def event_holding_instruction(hours_to_event: float | None, impact: str | None) -> str:
    if hours_to_event is None or impact is None:
        return "SAFE_TO_HOLD"
    impact = impact.upper()
    if impact not in {"LOW", "MEDIUM", "HIGH", "VERY_HIGH"}:
        raise ValueError("unsupported impact")
    if hours_to_event < 0:
        return "SAFE_TO_HOLD"
    if impact == "VERY_HIGH" and hours_to_event <= 24:
        return "DO_NOT_OPEN" if hours_to_event <= 2 else "CLOSE_BEFORE_EVENT"
    if impact == "HIGH" and hours_to_event <= 24:
        return "CLOSE_BEFORE_EVENT" if hours_to_event <= 8 else "REDUCE_BEFORE_EVENT"
    if impact in {"HIGH", "VERY_HIGH"} and hours_to_event <= 48:
        return "REDUCE_BEFORE_EVENT"
    return "SAFE_TO_HOLD"
