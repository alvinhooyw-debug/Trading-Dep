"""Research probability helpers. These are estimates, never guarantees."""

from __future__ import annotations

import math


def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def risk_neutral_finish_above(spot: float, strike: float, years: float, volatility: float, rate: float = 0.0) -> float:
    if spot <= 0 or strike <= 0 or years <= 0 or volatility <= 0:
        raise ValueError("spot, strike, years and volatility must be positive")
    d2 = (math.log(spot / strike) + (rate - 0.5 * volatility**2) * years) / (volatility * math.sqrt(years))
    return _norm_cdf(d2)


def risk_neutral_finish_below(spot: float, strike: float, years: float, volatility: float, rate: float = 0.0) -> float:
    return 1.0 - risk_neutral_finish_above(spot, strike, years, volatility, rate)


def delta_probability_proxy(delta: float) -> float:
    """Absolute delta as a rough probability proxy, not a calibrated forecast."""
    return min(1.0, max(0.0, abs(delta)))
