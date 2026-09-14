from __future__ import annotations

from dataclasses import dataclass

from .calibration import brier_score
from .predictor import StandardizedLogisticRegression, binary_log_loss
from .walkforward import expanding_window_folds


@dataclass(frozen=True)
class WalkForwardMetrics:
    predictions: int
    brier: float
    log_loss: float
    accuracy: float
    forecasts: tuple[float, ...]
    outcomes: tuple[int, ...]


def walk_forward_logistic(
    X: list[list[float]],
    y: list[int],
    *,
    min_train_size: int,
    test_size: int,
    step_size: int | None = None,
    model_kwargs: dict | None = None,
) -> WalkForwardMetrics:
    if len(X) != len(y):
        raise ValueError("X and y must have equal length")
    folds = expanding_window_folds(len(X), min_train_size, test_size, step_size)
    forecasts: list[float] = []
    outcomes: list[int] = []
    kwargs = model_kwargs or {}

    for fold in folds:
        model = StandardizedLogisticRegression(**kwargs)
        train_X = X[fold.train_start:fold.train_end]
        train_y = y[fold.train_start:fold.train_end]
        test_X = X[fold.test_start:fold.test_end]
        test_y = y[fold.test_start:fold.test_end]
        model.fit(train_X, train_y)
        forecasts.extend(model.predict_proba(test_X))
        outcomes.extend(test_y)

    if not forecasts:
        raise ValueError("no walk-forward predictions produced")
    accuracy = sum((p >= 0.5) == bool(yv) for p, yv in zip(forecasts, outcomes)) / len(outcomes)
    return WalkForwardMetrics(
        predictions=len(forecasts),
        brier=brier_score(forecasts, outcomes),
        log_loss=binary_log_loss(forecasts, outcomes),
        accuracy=accuracy,
        forecasts=tuple(forecasts),
        outcomes=tuple(outcomes),
    )
