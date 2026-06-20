# Contributing to CEOS

Thank you for your interest in CEOS. We are currently in the **empirical validation phase**. Contributions that help us discover and understand failure modes are especially valuable.

## Development Setup

```bash
git clone https://github.com/AvaPrime/ceos.git
cd ceos
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Code Style

- We use `ruff` for linting and formatting.
- Type hints are required (mypy in strict mode).
- All new code must be accompanied by tests, preferably property-based or adversarial.

## Empirical Contribution Guidelines

When adding or modifying behavior:

1. Add or extend an attack in `scripts/adversarial.py`
2. Ensure the change is covered by the falsification kernel (`run_experiment.py`)
3. Document any new invariants or observation model requirements in `docs/`

## Pull Request Process

- Keep PRs focused. One logical change per PR.
- Include empirical results from the falsification kernel when changing update dynamics.
- Update `docs/invariants.md` and `docs/failure-modes.md` when behavior changes.