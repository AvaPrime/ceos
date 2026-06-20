# CEOS — Empirical Epistemic Operating System

**CEOS** is a production-grade, event-sourced system for maintaining, testing, revising, and compounding organizational beliefs under uncertainty. It treats **Reality Claims** (intervention hypotheses) as first-class citizens and provides deterministic replay, versioned observation models, and measurable failure modes.

## Current Status (v0.2.1)

- ✅ Event-sourced truth layer with content-addressed observation models
- ✅ Deterministic, fingerprint-pinned replay
- ✅ Bounded update dynamics with 5 formal invariants (I1–I5)
- ✅ Empirical Failure Laboratory (minimal falsification kernel)
- ✅ Strong architectural foundation (VSM-aligned, causal observation models)

**Not yet production-ready for decision automation** — the system is currently optimized for **reproducible belief evolution and falsification**, not yet for autonomous resource allocation.

## Quick Start

```bash
git clone https://github.com/AvaPrime/ceos.git
cd ceos
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
docker compose up -d neo4j
python -m ceos.api
```

See `docs/getting-started.md` for full instructions.

## Architecture Overview

```
Event Log (immutable, ordered, fingerprinted)
        ↓
Observation Model Registry (content-addressed)
        ↓
Evidence (normalized signal + weight)
        ↓
Epistemic Kernel / Worker (bounded update, invariants)
        ↓
Belief State (Reality Graph projection)
        ↓
Empirical Failure Laboratory (adversarial testing)
```

Key principles:
- **Events are truth**
- **Observation models are versioned by content hash**
- **Replay must be semantically deterministic**
- **Invariants are runtime-enforceable**
- **Failure modes are measurable**