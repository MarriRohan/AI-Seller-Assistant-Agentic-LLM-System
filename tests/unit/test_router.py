from src.agents.router import route_workflow


def test_route_response_drafting_default() -> None:
    assert route_workflow("draft response") == "response_drafting"


def test_route_lead_qualification() -> None:
    assert route_workflow("lead qualification") == "lead_qualification"
