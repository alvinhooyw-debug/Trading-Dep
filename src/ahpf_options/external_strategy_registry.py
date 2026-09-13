from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class StrategyStatus(str, Enum):
    CANDIDATE = "CANDIDATE"
    REPRODUCED = "REPRODUCED"
    OOS_VALIDATED = "OOS_VALIDATED"
    PAPER_VALIDATED = "PAPER_VALIDATED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


@dataclass(frozen=True)
class ExternalStrategy:
    strategy_id: str
    source: str
    source_underlying: str
    target_underlying: str
    family: str
    hypothesis: str
    claimed_win_rate: float | None = None
    sample_size: int | None = None
    notes: str = ""


@dataclass(frozen=True)
class TransferEvidence:
    reproduced_trades: int = 0
    oos_trades: int = 0
    oos_expectancy: float | None = None
    paper_trades: int = 0
    paper_expectancy: float | None = None


def strategy_status(e: TransferEvidence, min_oos: int = 40, min_paper: int = 20) -> StrategyStatus:
    if e.oos_expectancy is not None and e.oos_expectancy < 0:
        return StrategyStatus.REJECTED
    if e.paper_expectancy is not None and e.paper_expectancy < 0:
        return StrategyStatus.REJECTED
    if e.reproduced_trades < 30:
        return StrategyStatus.CANDIDATE
    if e.oos_trades < min_oos or e.oos_expectancy is None:
        return StrategyStatus.REPRODUCED
    if e.oos_expectancy <= 0:
        return StrategyStatus.REJECTED
    if e.paper_trades < min_paper or e.paper_expectancy is None:
        return StrategyStatus.OOS_VALIDATED
    if e.paper_expectancy <= 0:
        return StrategyStatus.REJECTED
    return StrategyStatus.APPROVED


def requires_transfer_validation(strategy: ExternalStrategy) -> bool:
    return strategy.source_underlying.upper() != strategy.target_underlying.upper()
