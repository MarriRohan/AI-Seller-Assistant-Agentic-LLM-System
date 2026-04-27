"""Simple keyword-based evaluation harness."""

import json
from pathlib import Path

from src.workflows.response_drafting import run_response_drafting


def run() -> int:
    dataset_path = Path(__file__).parent / "datasets" / "seller_response_cases.json"
    cases = json.loads(dataset_path.read_text())

    passed = 0
    for case in cases:
        result = run_response_drafting(**case["input"])
        message = result["message"].lower()
        keywords = [kw.lower() for kw in case["expects_keywords"]]

        if all(keyword in message for keyword in keywords):
            passed += 1

    print(f"Passed {passed}/{len(cases)} eval cases")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(run())
