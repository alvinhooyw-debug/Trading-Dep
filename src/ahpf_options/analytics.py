from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Iterable


@dataclass(frozen=True)
class TradeOutcome:
    net_pnl: float
    mae: float | None = None
    mfe: float | None = None
    slippage: float | None = None
    fees: float = 0.0
    classification: str = "strategy_loss"


def expectancy(outcomes: Iterable[TradeOutcome]) -> float | None:
    values = [o.net_pnl for o in outcomes]
    return mean(values) if values else None


def win_rate(outcomes: Iterable[TradeOutcome]) -> float | None:
    values = list(outcomes)
    if not values:
        return None
    return sum(o.net_pnl > 0 for o in values) / len(values)


def average_fee_drag(outcomes: Iterable[TradeOutcome]) -> float | None:
    values = [o.fees for o in outcomes]
    return mean(values) if values else None


def summarize(outcomes: Iterable[TradeOutcome]) -> dict[str, float | int | None]:
    values = list(outcomes)
    wins = [o.net_pnl for o in values if o.net_pnl > 0]
    losses = [o.net_pnl for o in values if o.net_pnl < 0]
    return {
        "n": len(values),
        "win_rate": win_rate(values),
        "expectancy": expectancy(values),
        "avg_win": mean(wins) if wins else None,
        "avg_loss": mean(losses) if losses else None,
        "avg_fees": average_fee_drag(values),
    }
