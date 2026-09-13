from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable


@dataclass(frozen=True)
class BrokerFill:
    trade_id: str
    timestamp: datetime
    symbol: str
    expiry: str
    strike: float
    right: str
    side: str
    quantity: int
    price: float
    fees: float = 0.0

    @property
    def signed_cashflow(self) -> float:
        sign = 1.0 if self.side.upper() == "SELL" else -1.0
        return sign * self.price * 100 * self.quantity - self.fees


def aggregate_trade_cashflow(fills: Iterable[BrokerFill]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for fill in fills:
        totals[fill.trade_id] = totals.get(fill.trade_id, 0.0) + fill.signed_cashflow
    return totals


def validate_defined_risk_vertical(fills: Iterable[BrokerFill]) -> tuple[bool, str]:
    rows = list(fills)
    if len(rows) != 2:
        return False, "vertical requires exactly two legs"
    if rows[0].symbol != rows[1].symbol or rows[0].expiry != rows[1].expiry:
        return False, "legs must share symbol and expiry"
    if rows[0].right != rows[1].right:
        return False, "legs must use the same option right"
    if rows[0].side == rows[1].side:
        return False, "vertical must contain one buy and one sell"
    return True, "valid vertical"
