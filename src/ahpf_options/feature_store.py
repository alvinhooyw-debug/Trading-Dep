from __future__ import annotations

from dataclasses import dataclass, fields
from datetime import datetime


@dataclass(frozen=True)
class FeatureSnapshot:
    timestamp: datetime
    symbol: str
    underlying_price: float
    return_5m: float
    return_15m: float
    vwap_distance_pct: float
    rsi: float
    rsi_ma: float
    sqzmom: float
    sqzmom_change: float
    atr_pct: float
    volume_strength: float
    bias_15m: float
    bias_1h: float
    bias_4h: float
    bias_daily: float
    vix: float
    vix1d: float
    treasury_10y: float
    dxy_change_pct: float
    breadth_score: float
    semiconductor_return_pct: float
    gamma_distance_pct: float
    minutes_to_macro_event: float
    option_iv: float
    option_delta: float
    bid_ask_width_pct: float
    strike_distance_pct: float
    dte: float
    minutes_from_open: float

    def validate(self) -> None:
        if self.symbol not in {"SPY", "QQQ"}:
            raise ValueError("symbol must be SPY or QQQ")
        if self.underlying_price <= 0:
            raise ValueError("underlying_price must be positive")
        if self.dte < 0 or self.dte > 4:
            raise ValueError("dte must be between 0 and 4")
        if not 0 <= self.rsi <= 100 or not 0 <= self.rsi_ma <= 100:
            raise ValueError("RSI values must be between 0 and 100")
        if not -1 <= self.option_delta <= 1:
            raise ValueError("option_delta must be between -1 and 1")

    def numeric_vector(self) -> list[float]:
        self.validate()
        excluded = {"timestamp", "symbol", "underlying_price"}
        return [float(getattr(self, f.name)) for f in fields(self) if f.name not in excluded]


FEATURE_NAMES = [
    f.name
    for f in fields(FeatureSnapshot)
    if f.name not in {"timestamp", "symbol", "underlying_price"}
]
