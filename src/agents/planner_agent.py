"""Simple planning helper for workflow selection reasoning."""


def plan_for_intent(intent: str) -> str:
    normalized = intent.strip().lower()
    if "follow" in normalized:
        return "followup_sequence"
    if "qualif" in normalized:
        return "lead_qualification"
    return "response_drafting"
