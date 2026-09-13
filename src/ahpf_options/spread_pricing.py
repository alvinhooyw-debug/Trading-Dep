"""Fee-aware vertical-spread research calculations.

All monetary inputs are quoted in option points except fees, which are USD.
One option point is assumed to represent USD 100 per contract.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

MULTIPLIER = 100.0


@dataclass(frozen=True)
class SpreadEconomics:
    max_profit_usd: float
    max_loss_usd: float
    breakeven: float
    return_on_risk: float
    fees_usd: float


def debit_vertical(width: float, debit: float, long_strike: float, *, bullish: bool = True, fees_usd: float = 0.0) -> SpreadEconomics:
    if not (0 < debit < width):
        raise ValueError("debit must be greater than zero and less than width")
    gross_profit = (width - debit) * MULTIPLIER
    max_profit = gross_profit - fees_usd
    max_loss = debit * MULTIPLIER + fees_usd
    breakeven = long_strike + debit if bullish else long_strike - debit
    return SpreadEconomics(max_profit, max_loss, breakeven, max_profit / max_loss, fees_usd)


def credit_vertical(width: float, credit: float, short_strike: float, *, bullish: bool = True, fees_usd: float = 0.0) -> SpreadEconomics:
    if not (0 < credit < width):
        raise ValueError("credit must be greater than zero and less than width")
    max_profit = credit * MULTIPLIER - fees_usd
    max_loss = (width - credit) * MULTIPLIER + fees_usd
    breakeven = short_strike - credit if bullish else short_strike + credit
    return SpreadEconomics(max_profit, max_loss, breakeven, max_profit / max_loss, fees_usd)


def binary_expected_value(win_probability: float, win_usd: float, loss_usd: float) -> float:
    if not 0 <= win_probability <= 1:
        raise ValueError("win_probability must be between 0 and 1")
    return win_probability * win_usd - (1 - win_probability) * loss_usd


def minimum_credit_for_target_win_rate(width: float, win_probability: float, fees_usd: float = 0.0) -> float:
    """Minimum credit in option points for non-negative binary EV.

    Rounded upward to the next cent so cent rounding cannot turn the result negative.
    """
    if width <= 0 or not 0 < win_probability < 1:
        raise ValueError("invalid width or win probability")
    raw = (1 - win_probability) * width + fees_usd / MULTIPLIER
    return math.ceil((raw - 1e-12) * 100) / 100
