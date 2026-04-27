"""Entrypoint for local execution and smoke testing."""

import json

from src.agents.seller_assistant_agent import handle_request
from src.memory.session_store import add_session_note
from src.observability.logging import configure_logging


def main() -> None:
    configure_logging()

    session_id = "session-123"
    add_session_note(session_id, "Customer asked for a plan suitable for a small team.")

    payload = {
        "intent": "draft_response",
        "session_id": session_id,
        "customer_name": "Jordan",
        "product_key": "pro-plan",
        "customer_need": "managing a growing sales pipeline",
    }

    result = handle_request(payload)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
