from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CalibrationBin:
    lower: float
    upper: float
    count: int
    mean_forecast: float
    observed_rate: float
    brier_component: float


def calibration_bins(forecasts: Iterable[float], outcomes: Iterable[int], bins: int = 5) -> list[CalibrationBin]:
    xs = list(forecasts)
    ys = list(outcomes)
    if len(xs) != len(ys):
        raise ValueError("forecasts and outcomes must have equal length")
    if bins < 1:
        raise ValueError("bins must be positive")
    if any(p < 0 or p > 1 for p in xs):
        raise ValueError("forecasts must be between 0 and 1")
    result: list[CalibrationBin] = []
    for i in range(bins):
        lo = i / bins
        hi = (i + 1) / bins
        idx = [j for j, p in enumerate(xs) if (lo <= p < hi) or (i == bins - 1 and p == 1)]
        if not idx:
            continue
        mf = sum(xs[j] for j in idx) / len(idx)
        obs = sum(ys[j] for j in idx) / len(idx)
        brier = sum((xs[j] - ys[j]) ** 2 for j in idx) / len(idx)
        result.append(CalibrationBin(lo, hi, len(idx), mf, obs, brier))
    return result


def brier_score(forecasts: Iterable[float], outcomes: Iterable[int]) -> float:
    xs = list(forecasts)
    ys = list(outcomes)
    if not xs or len(xs) != len(ys):
        raise ValueError("non-empty equal-length inputs required")
    return sum((p - y) ** 2 for p, y in zip(xs, ys)) / len(xs)
