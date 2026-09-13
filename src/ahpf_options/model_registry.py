from __future__ import annotations

from dataclasses import dataclass


MODEL_STATES = {
    "EXPERIMENTAL",
    "OOS_VALIDATED",
    "SHADOW",
    "APPROVED",
    "DEMOTED",
    "REJECTED",
}


@dataclass(frozen=True)
class ModelCard:
    model_id: str
    target: str
    symbol_scope: tuple[str, ...]
    feature_version: str
    train_start: str
    train_end: str
    oos_start: str
    oos_end: str
    state: str = "EXPERIMENTAL"
    notes: str = ""

    def validate(self) -> None:
        if self.state not in MODEL_STATES:
            raise ValueError(f"invalid model state: {self.state}")
        if not self.model_id or not self.target:
            raise ValueError("model_id and target are required")
        if any(symbol not in {"SPY", "QQQ"} for symbol in self.symbol_scope):
            raise ValueError("symbol scope must contain only SPY/QQQ")


def next_model_state(current: str, *, oos_pass: bool = False, shadow_pass: bool = False, reliability_pass: bool = False) -> str:
    if current not in MODEL_STATES:
        raise ValueError("invalid current state")
    if current in {"REJECTED", "DEMOTED"}:
        return current
    if not oos_pass:
        return "EXPERIMENTAL"
    if not shadow_pass:
        return "OOS_VALIDATED"
    if not reliability_pass:
        return "SHADOW"
    return "APPROVED"
