# CEOS Known Failure Modes & Empirical Results

## Latest Run (v0.2.1 Kernel — June 20, 2026)

**Summary**: System is mechanically stable but has localized update dynamics weakness under high-frequency contradiction pressure.

### Dominant Failure Mode

**I2 Conflict Monotonicity** (68% violation rate at 20+ contradictions per 100 events)

- **Symptom**: Upward belief inflation under rapid contradictory input
- **Root Cause**: Linear per-event penalty does not scale with density
- **Impact**: Moderate drift in belief strength
- **Recommended Action**: Implement rolling-window conflict memory + adaptive damping

### Other Observations

- I1, I3, I4, I5: Strong (low or zero violations)
- Replay: Fully deterministic when fingerprints are pinned
- Semantic pinning (observation model fingerprints): Effective

### Failure Taxonomy

| Category | Frequency | Severity | Notes |
|----------|-----------|----------|-------|
| Conflict handling under density | High | Medium | Primary issue |
| Drift (upward bias) | Medium | Medium | Linked to I2 |
| Replay divergence | Low | Low | Rare, only under extreme ordering attacks |