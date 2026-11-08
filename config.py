from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    project_name: str = "AURELION"
    version: str = "1.0.0"
    research_mode: bool = True

settings = Settings()
