"""Deterministic product lookup tool."""

from typing import Any

PRODUCTS = {
    "starter-plan": {
        "name": "Starter Plan",
        "price_usd": 29,
        "key_features": ["Email support", "Basic analytics", "1 user seat"],
    },
    "pro-plan": {
        "name": "Pro Plan",
        "price_usd": 99,
        "key_features": ["Priority support", "Advanced analytics", "5 user seats"],
    },
}


def lookup_product(product_key: str) -> dict[str, Any]:
    if product_key not in PRODUCTS:
        return {
            "found": False,
            "message": f"No product found for key '{product_key}'.",
        }

    return {
        "found": True,
        "product": PRODUCTS[product_key],
    }
