from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Protocol, Sequence


@dataclass(frozen=True)
class Quote:
    symbol: str
    price: float
    bid: float | None = None
    ask: float | None = None
    timestamp: datetime | None = None

    def age_seconds(self, now: datetime | None = None) -> float | None:
        if self.timestamp is None:
            return None
        current = now or datetime.now(timezone.utc)
        stamp = self.timestamp if self.timestamp.tzinfo else self.timestamp.replace(tzinfo=timezone.utc)
        return max(0.0, (current - stamp).total_seconds())


@dataclass(frozen=True)
class OptionQuote:
    symbol: str
    expiry: str
    strike: float
    right: str
    bid: float
    ask: float
    delta: float | None = None
    iv: float | None = None
    volume: int | None = None
    open_interest: int | None = None
    timestamp: datetime | None = None

    @property
    def mid(self) -> float:
        return (self.bid + self.ask) / 2.0

    @property
    def spread(self) -> float:
        return max(0.0, self.ask - self.bid)


@dataclass(frozen=True)
class MarketSnapshot:
    underlying: Quote
    options: Sequence[OptionQuote]
    vix: float | None = None
    vix1d: float | None = None
    ten_year_yield: float | None = None
    dxy: float | None = None
    breadth: float | None = None
    sox_change_pct: float | None = None
    source: str = "manual"


class MarketDataAdapter(Protocol):
    """Read-only adapter contract. Implementations must never place orders."""

    def snapshot(self, symbol: str) -> MarketSnapshot:
        ...


def validate_freshness(snapshot: MarketSnapshot, max_age_seconds: int = 60) -> tuple[bool, str]:
    age = snapshot.underlying.age_seconds()
    if age is None:
        return False, "underlying timestamp missing"
    if age > max_age_seconds:
        return False, f"stale underlying quote: {age:.0f}s old"
    return True, "fresh"
