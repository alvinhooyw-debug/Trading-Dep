from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class TradeRecord:
    setup: str
    symbol: str
    dte: int
    net_pnl: float
    fees: float
    hour_et: int | None = None
    regime: str | None = None


@dataclass(frozen=True)
class EdgeStats:
    trades: int
    wins: int
    win_rate: float
    expectancy: float
    total_net_pnl: float
    fee_drag: float


def summarize(records: Iterable[TradeRecord]) -> EdgeStats:
    rows = list(records)
    if not rows:
        return EdgeStats(0, 0, 0.0, 0.0, 0.0, 0.0)
    wins = sum(r.net_pnl > 0 for r in rows)
    total = sum(r.net_pnl for r in rows)
    fees = sum(r.fees for r in rows)
    return EdgeStats(len(rows), wins, wins / len(rows), total / len(rows), total, fees)


def group_by(records: Iterable[TradeRecord], field: str) -> dict[str, EdgeStats]:
    groups: dict[str, list[TradeRecord]] = defaultdict(list)
    for row in records:
        value = getattr(row, field)
        groups[str(value)].append(row)
    return {key: summarize(rows) for key, rows in groups.items()}


def weekly_edge_report(records: Iterable[TradeRecord]) -> dict[str, object]:
    rows = list(records)
    return {
        "overall": summarize(rows),
        "by_setup": group_by(rows, "setup"),
        "by_symbol": group_by(rows, "symbol"),
        "by_dte": group_by(rows, "dte"),
        "by_hour_et": group_by(rows, "hour_et"),
        "by_regime": group_by(rows, "regime"),
    }
