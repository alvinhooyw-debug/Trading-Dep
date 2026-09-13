from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class WalkForwardFold:
    train_start: int
    train_end: int
    test_start: int
    test_end: int


def expanding_window_folds(
    n_obs: int,
    min_train: int,
    test_size: int,
    step: int | None = None,
) -> list[WalkForwardFold]:
    if min_train <= 0 or test_size <= 0:
        raise ValueError("min_train and test_size must be positive")
    if n_obs < min_train + test_size:
        return []
    stride = step or test_size
    if stride <= 0:
        raise ValueError("step must be positive")

    folds: list[WalkForwardFold] = []
    train_end = min_train
    while train_end + test_size <= n_obs:
        folds.append(
            WalkForwardFold(
                train_start=0,
                train_end=train_end,
                test_start=train_end,
                test_end=train_end + test_size,
            )
        )
        train_end += stride
    return folds


def materialize_fold(data: Sequence[T], fold: WalkForwardFold) -> tuple[Sequence[T], Sequence[T]]:
    return data[fold.train_start:fold.train_end], data[fold.test_start:fold.test_end]
