from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class AurelionEngine:
    observations: list[dict[str, Any]] = field(default_factory=list)
    started_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def record(self, observation: dict[str, Any]) -> None:
        if not isinstance(observation, dict):
            raise TypeError("observation must be a dictionary")
        self.observations.append(observation.copy())

    def status(self) -> dict[str, Any]:
        return {
            "engine": "AURELION",
            "version": "1.0.0",
            "observations_recorded": len(self.observations),
            "started_at": self.started_at,
        }
