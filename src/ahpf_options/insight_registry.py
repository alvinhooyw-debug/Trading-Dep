from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class InsightStage(str, Enum):
    CANDIDATE = "candidate"
    BACKTESTED = "backtested"
    WALK_FORWARD_PASSED = "walk_forward_passed"
    PAPER_VALIDATED = "paper_validated"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass(frozen=True)
class InsightEvidence:
    sample_size: int
    expectancy: float
    out_of_sample_expectancy: float | None = None
    max_drawdown: float | None = None


def eligible_for_promotion(
    stage: InsightStage,
    evidence: InsightEvidence,
    *,
    min_sample: int = 40,
    require_positive_oos: bool = True,
) -> bool:
    if stage in {InsightStage.REJECTED, InsightStage.APPROVED}:
        return False
    if evidence.sample_size < min_sample:
        return False
    if evidence.expectancy <= 0:
        return False
    if require_positive_oos:
        if evidence.out_of_sample_expectancy is None or evidence.out_of_sample_expectancy <= 0:
            return False
    return True
