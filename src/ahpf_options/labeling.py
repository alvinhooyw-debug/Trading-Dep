from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ForwardOutcome:
    future_return: float
    max_favorable_excursion: float
    max_adverse_excursion: float
    touched_upper: bool
    touched_lower: bool
    finished_above_strike: bool | None


def label_forward_path(
    entry_price: float,
    future_prices: list[float],
    *,
    upper_level: float | None = None,
    lower_level: float | None = None,
    strike: float | None = None,
) -> ForwardOutcome:
    if entry_price <= 0:
        raise ValueError("entry_price must be positive")
    if not future_prices or any(p <= 0 for p in future_prices):
        raise ValueError("future_prices must contain positive prices")
    returns = [(p / entry_price) - 1.0 for p in future_prices]
    return ForwardOutcome(
        future_return=returns[-1],
        max_favorable_excursion=max(returns),
        max_adverse_excursion=min(returns),
        touched_upper=upper_level is not None and max(future_prices) >= upper_level,
        touched_lower=lower_level is not None and min(future_prices) <= lower_level,
        finished_above_strike=None if strike is None else future_prices[-1] >= strike,
    )


def binary_target(outcome: ForwardOutcome, target: str) -> int:
    if target == "up":
        return int(outcome.future_return > 0)
    if target == "down":
        return int(outcome.future_return < 0)
    if target == "touched_upper":
        return int(outcome.touched_upper)
    if target == "touched_lower":
        return int(outcome.touched_lower)
    if target == "finished_above_strike":
        if outcome.finished_above_strike is None:
            raise ValueError("strike outcome unavailable")
        return int(outcome.finished_above_strike)
    raise ValueError(f"unsupported target: {target}")
