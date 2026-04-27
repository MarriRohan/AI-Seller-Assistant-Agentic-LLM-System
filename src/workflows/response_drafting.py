"""Workflow for creating grounded seller response drafts."""

from typing import Any

from src.memory.retrieval import retrieve_context
from src.tools.product_lookup import lookup_product


def run_response_drafting(
    *,
    session_id: str,
    customer_name: str,
    product_key: str,
    customer_need: str,
    trace_id: str,
) -> dict[str, Any]:
    product_result = lookup_product(product_key)
    context = retrieve_context(session_id)

    if not product_result["found"]:
        message = (
            f"Hi {customer_name}, thanks for your interest. "
            "I want to make sure I recommend the right option—"
            "could you share a bit more about your use case?"
        )
        return {
            "trace_id": trace_id,
            "message": message,
            "facts_used": [],
            "context_used": context,
            "status": "needs_clarification",
        }

    product = product_result["product"]
    feature_text = ", ".join(product["key_features"][:2])
    message = (
        f"Hi {customer_name}, based on your need for {customer_need}, "
        f"I recommend our {product['name']} at ${product['price_usd']}/month. "
        f"It includes {feature_text}."
    )

    return {
        "trace_id": trace_id,
        "message": message,
        "facts_used": [
            f"Product: {product['name']}",
            f"Price: ${product['price_usd']}/month",
            f"Features: {', '.join(product['key_features'])}",
        ],
        "context_used": context,
        "status": "ok",
    }
