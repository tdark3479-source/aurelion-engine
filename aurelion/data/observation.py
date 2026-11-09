from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class Observation:
    source: str
    value: float
    timestamp: str
    metadata: dict[str, Any] | None = None

    @classmethod
    def create(
        cls,
        source: str,
        value: float,
        metadata: dict[str, Any] | None = None
    ) -> "Observation":

        if not source.strip():
            raise ValueError("source cannot be empty")

        return cls(
            source=source,
            value=float(value),
            timestamp=datetime.now(timezone.utc).isoformat(),
            metadata=metadata
      )
