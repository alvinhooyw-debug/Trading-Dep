# AH-PF Trading Research Adviser

AH-PF is a research and decision-support repository for SPY/QQQ short-dated options. It is not an autonomous trading bot and must never place brokerage orders.

## Core mandate

- Instruments: SPY, QQQ
- DTE: 0-4, with 0DTE preferred when justified
- Output states: `A+ TRADE`, `WAIT`, `NO TRADE`
- Maximum single-leg premium at risk: about USD 100
- Maximum defined spread risk: about USD 300
- Limit orders preferred
- No averaging down, revenge trading, or uncovered short options
- A+ threshold: 90/100, subject to hard vetoes

## Repository purpose

This codebase stores the operating protocol, fee-aware spread economics, probability estimates, gamma/macro context, comparable-trade learning, reproducible research outputs, and a canonical validated trade log.

The official validated personal trade sample starts at zero. Historical conversational trades are not statistical evidence until reconstructed from broker records.

## Self-improvement model

AH-PF improves through evidence, not by automatically rewriting itself after recent wins or losses.

`observe -> classify -> recommend -> record -> diagnose -> compare -> test insight -> walk-forward validate -> paper validate -> approve`

The system now includes post-trade analytics, expanding-window walk-forward utilities, a candidate insight promotion gate, standardized research-run output files, and templates for logging rejected/no-trade candidates. See `docs/self_improvement_loop.md`.

## Structure

- `docs/` operating protocol, methodology and learning governance
- `config/` risk, fee, and scoring configuration
- `src/ahpf_options/` research, analytics and learning modules
- `data/` templates and validated logs
- `backtests/` reproducible experiment outputs
- `tests/` unit tests

## Safety boundary

Do not add broker execution, API keys, passwords, account credentials, or autonomous order placement. This repository improves decision quality, not trade frequency.

## Development

```bash
python -m pip install -e .[dev]
pytest
```
