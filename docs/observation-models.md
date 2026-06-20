# Observation Models in CEOS

Every Reality Claim defines (or references) an **observation model** that maps raw outcomes into the claim’s specific evidence space.

## Purpose

- Makes claims locally well-posed
- Allows heterogeneous domains (retention, revenue, behavior, etc.)
- Enables content-addressed semantic pinning (fingerprinting)

## How to Write an Observation Model

```python
def my_claim_observation_model(raw_outcome: dict) -> Evidence:
    """Maps raw system/world outcome to normalized evidence."""
    return {
        "signal": float(raw_outcome.get("delta", 0.0)),   # [-1.0, 1.0]
        "weight": min(1.0, raw_outcome.get("sample_size", 0) / 1000.0),
        "claim_id": raw_outcome["claim_id"]
    }
```

## Registration

```python
registry.register(my_claim_observation_model)
# Returns fingerprint for use in events
```

## Best Practices

- Keep models pure and deterministic
- Normalize signal to [-1.0, 1.0] where possible
- Include weight for evidence reliability
- Version via content hash (automatic fingerprinting)

See `src/ceos/observation/` for the registry implementation.