"""Retrieval helpers for contextual enrichment."""

from src.memory.session_store import get_session_notes


def retrieve_context(session_id: str, limit: int = 3) -> list[str]:
    notes = get_session_notes(session_id)
    return notes[-limit:]
