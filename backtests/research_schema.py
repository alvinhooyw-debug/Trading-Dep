from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ResearchRunConfig:
    strategy: str
    underlying: str
    start_date: str
    end_date: str
    parameters: dict[str, Any]
    data_source: str
    notes: str = ""


def initialize_run_directory(base_dir: str | Path, run_id: str, config: ResearchRunConfig) -> Path:
    run_dir = Path(base_dir) / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    (run_dir / "run_config.json").write_text(json.dumps(asdict(config), indent=2, sort_keys=True), encoding="utf-8")
    (run_dir / "summary.csv").write_text("metric,value\n", encoding="utf-8")
    (run_dir / "trades.csv").write_text("trade_id,entry_time,exit_time,net_pnl,fees,mae,mfe\n", encoding="utf-8")
    (run_dir / "coverage.json").write_text("{}\n", encoding="utf-8")
    (run_dir / "quality_report.json").write_text("{}\n", encoding="utf-8")
    return run_dir
