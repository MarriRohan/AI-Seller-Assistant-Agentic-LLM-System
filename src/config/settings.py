"""Application settings loaded from environment variables."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "AI Seller Assistant")
    default_workflow: str = os.getenv("DEFAULT_WORKFLOW", "response_drafting")


def load_settings() -> Settings:
    return Settings()
