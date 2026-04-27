"""Seller assistant facade used by the application entrypoint."""

from typing import Any

from src.agents.router import route_workflow
from src.observability.tracing import new_trace_id, timed_step
from src.workflows.response_drafting import run_response_drafting


def handle_request(payload: dict[str, Any]) -> dict[str, Any]:
    intent = payload.get("intent", "draft")
    workflow = route_workflow(intent)
    trace_id = new_trace_id()

    with timed_step() as elapsed:
        if workflow != "response_drafting":
            return {
                "trace_id": trace_id,
                "workflow": workflow,
                "status": "not_implemented",
                "message": f"Workflow '{workflow}' is planned but not implemented yet.",
                "duration_seconds": elapsed["seconds"],
            }

        result = run_response_drafting(
            session_id=payload["session_id"],
            customer_name=payload["customer_name"],
            product_key=payload["product_key"],
            customer_need=payload["customer_need"],
            trace_id=trace_id,
        )

    result["workflow"] = workflow
    result["duration_seconds"] = elapsed["seconds"]
    return result
