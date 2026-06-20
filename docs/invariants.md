# CEOS Invariants (I1–I5) — v0.1

These invariants define the enforceable rules of valid belief evolution. They are runtime-checkable and empirically tested via the Empirical Failure Laboratory.

## I1 — Bounded Update Invariant

**Statement**: No single event may change belief strength by more than ε (default 0.15).

**Rationale**: Prevents unbounded instantaneous regret / prediction error.

**Current Empirical Status**: 0% violation rate (stable).

## I2 — Conflict Monotonicity Invariant

**Statement**: Increased opposition must reduce net update magnitude.

**Rationale**: Contradictory evidence should increase expected future causal error and therefore damp learning.

**Current Empirical Status**: 68% violation rate under high-density contradiction (dominant failure mode). Needs regime-aware damping.

## I3 — Ordering Invariance

**Statement**: Events with identical `event_seq` must produce the same final state regardless of order.

**Rationale**: Ensures consistent regret/error trajectories under replay.

**Current Empirical Status**: 4% violation rate (good).

## I4 — Idempotency Invariant

**Statement**: Re-processing an already-processed event produces zero marginal change.

**Rationale**: Duplicate evidence contributes zero new causal information.

**Current Empirical Status**: 8% violation rate (acceptable).

## I5 — Semantic Determinism Invariant

**Statement**: For a fixed event log and fixed observation model fingerprints, replay must produce identical belief state.

**Rationale**: Semantic reproducibility across deployments and time.

**Current Empirical Status**: 0% violation rate (strong).

---

**Latest empirical results** (v0.2.1 kernel): Dominant issue is I2 under rapid contradiction density. See `docs/failure-modes.md` for details.