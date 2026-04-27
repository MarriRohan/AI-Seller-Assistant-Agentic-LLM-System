"""Routes incoming intents to workflows."""

from src.agents.planner_agent import plan_for_intent


def route_workflow(intent: str) -> str:
    return plan_for_intent(intent)
