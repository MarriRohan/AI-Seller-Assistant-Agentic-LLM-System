"""In-memory session summary store for local development."""

from collections import defaultdict

_SESSION_SUMMARIES: dict[str, list[str]] = defaultdict(list)


def add_session_note(session_id: str, note: str) -> None:
    _SESSION_SUMMARIES[session_id].append(note)


def get_session_notes(session_id: str) -> list[str]:
    return list(_SESSION_SUMMARIES.get(session_id, []))
