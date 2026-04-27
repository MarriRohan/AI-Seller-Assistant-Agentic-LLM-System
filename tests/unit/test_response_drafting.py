from src.memory.session_store import add_session_note
from src.workflows.response_drafting import run_response_drafting


def test_response_drafting_happy_path() -> None:
    session_id = "test-session"
    add_session_note(session_id, "Customer cares about analytics.")

    result = run_response_drafting(
        session_id=session_id,
        customer_name="Avery",
        product_key="starter-plan",
        customer_need="budget-friendly setup",
        trace_id="trace-1",
    )

    assert result["status"] == "ok"
    assert "Starter Plan" in result["message"]
    assert result["facts_used"]
    assert result["context_used"]


def test_response_drafting_unknown_product() -> None:
    result = run_response_drafting(
        session_id="unknown-session",
        customer_name="Avery",
        product_key="nope",
        customer_need="anything",
        trace_id="trace-2",
    )

    assert result["status"] == "needs_clarification"
    assert result["facts_used"] == []
