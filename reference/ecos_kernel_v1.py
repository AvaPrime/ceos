"""
E-COS Kernel v1
Minimal Event-Sourced Cognitive Substrate Prototype

Core properties:
- Append-only event store
- Deterministic replay
- State derived entirely from events
- No hidden memory
"""

import uuid
import json
from datetime import datetime
from copy import deepcopy


# =========================================================
# EVENT STORE (APPEND-ONLY)
# =========================================================

class EventStore:
    def __init__(self):
        self._events = []

    def append(self, event: dict):
        validated = self._validate(event)
        self._events.append(validated)

    def all_events(self):
        return deepcopy(self._events)

    def _validate(self, event: dict):
        required = [
            "event_id",
            "timestamp",
            "event_type",
            "actor",
            "payload",
            "context",
            "epistemic_status"
        ]

        for r in required:
            if r not in event:
                raise ValueError(f"Missing required field: {r}")

        return deepcopy(event)


# =========================================================
# REPLAY ENGINE (DETERMINISTIC STATE DERIVATION)
# =========================================================

class ReplayEngine:
    def __init__(self, store: EventStore):
        self.store = store

    def replay(self):
        state = {
            "memory": {},
            "identity": {},
            "skills": {},
            "beliefs": {},
            "trace": []
        }

        for event in self.store.all_events():
            state = self._apply(state, event)

        return state

    def _apply(self, state, event):
        etype = event["event_type"]
        payload = event["payload"]

        # -------------------------
        # MEMORY
        # -------------------------
        if etype == "memory_commit":
            mid = payload.get("memory_id", str(uuid.uuid4()))
            state["memory"][mid] = payload

        # -------------------------
        # IDENTITY
        # -------------------------
        elif etype == "identity_shift":
            state["identity"].update(payload)

        # -------------------------
        # SKILLS
        # -------------------------
        elif etype == "skill_formation":
            sid = payload.get("skill_id", str(uuid.uuid4()))
            state["skills"][sid] = payload

        # -------------------------
        # BELIEFS (CEOS HOOK)
        # -------------------------
        elif etype == "belief_update":
            bid = payload.get("belief_id", str(uuid.uuid4()))
            state["beliefs"][bid] = {
                "data": payload,
                "epistemic": event.get("epistemic_status", {})
            }

        # -------------------------
        # TRACE ALL EVENTS
        # -------------------------
        state["trace"].append(event["event_id"])

        return state


# =========================================================
# EVENT FACTORY (CONVENIENCE)
# =========================================================

def create_event(event_type, actor, payload=None, context=None, epistemic_status=None):
    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "actor": actor,
        "payload": payload or {},
        "context": context or {
            "session_id": "default",
            "trace_id": str(uuid.uuid4()),
            "causal_parent": None
        },
        "epistemic_status": epistemic_status or {
            "confidence": 1.0,
            "source": "system",
            "verified": False
        }
    }


# =========================================================
# DEMO / EXECUTION
# =========================================================

def main():
    store = EventStore()

    # -------------------------
    # Simulated cognitive events
    # -------------------------

    e1 = create_event(
        "memory_commit",
        actor="agent_1",
        payload={"memory_id": "m1", "content": "User prefers structured systems."}
    )

    e2 = create_event(
        "identity_shift",
        actor="agent_1",
        payload={"trait": "systematic_reasoning", "strength": 0.7}
    )

    e3 = create_event(
        "skill_formation",
        actor="agent_1",
        payload={"skill_id": "s1", "name": "event_sourcing", "level": 0.4}
    )

    e4 = create_event(
        "belief_update",
        actor="ceos_stub",
        payload={"belief_id": "b1", "claim": "Event-sourcing improves traceability."},
        epistemic_status={"confidence": 0.86, "source": "model", "verified": False}
    )

    # Append events
    for e in [e1, e2, e3, e4]:
        store.append(e)

    # Replay system state
    engine = ReplayEngine(store)
    state = engine.replay()

    # Output
    print("\n=== E-COS REPLAY RESULT ===\n")
    print(json.dumps(state, indent=2))


if __name__ == "__main__":
    main()