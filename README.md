# AI Seller Assistant Agentic LLM System

AI-powered seller assistant architecture for building agentic LLM workflows.

## Overview
This repository provides a minimal but runnable starter scaffold for an **agentic seller assistant**. It includes:
- a workflow router,
- one concrete workflow (`response_drafting`),
- one deterministic tool (`product_lookup`),
- lightweight in-memory session storage,
- retrieval context enrichment,
- basic logging/tracing primitives,
- and an evaluation harness seed.

The goal is to establish a foundation that is easy to extend while keeping responsibilities clear between agents, tools, workflows, and memory.

## Goals
- Automate seller-facing tasks like lead qualification and response drafting.
- Keep deterministic data-fetching logic in tools, not in prompts.
- Make behavior observable with trace IDs and consistent logs.
- Support fast iteration with unit tests and lightweight eval scenarios.

## Non-Goals
- Full production deployment configuration.
- Vendor-specific LLM SDK integrations.
- Autonomous outbound actions without review.

## Architecture (high-level)
1. An input request enters `main.py`.
2. `agents/router.py` chooses the best workflow.
3. A workflow (e.g., `response_drafting`) invokes tools for grounded facts.
4. Memory + retrieval modules enrich context.
5. The workflow returns a structured result with trace metadata.

## Repository Structure
```text
src/
  main.py                     Entry point + CLI demo runner
  config/settings.py          Environment-driven app settings
  agents/
    router.py                 Workflow selection logic
    planner_agent.py          Minimal planning helper
    seller_assistant_agent.py Facade for handling requests
  tools/
    product_lookup.py         Deterministic product lookup tool
  workflows/
    response_drafting.py      End-to-end draft generation workflow
  memory/
    session_store.py          In-memory session summaries
    retrieval.py              Context retrieval from session memory
  prompts/
    system/default_system_prompt.txt
    tasks/response_drafting_prompt.txt
  observability/
    logging.py                Logger setup
    tracing.py                Trace ID helper + timing context

tests/
  unit/test_router.py
  unit/test_response_drafting.py
  evals/run_eval.py
  evals/datasets/seller_response_cases.json
```

## Getting Started
### 1) Create a virtual environment and install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 2) Run the example workflow
```bash
python -m src.main
```

### 3) Run tests
```bash
pytest
```

### 4) Run eval harness
```bash
python -m tests.evals.run_eval
```

## Example Workflow
Input:
- seller intent,
- product name,
- optional customer profile.

Steps:
- fetch product details from tool,
- gather contextual memory,
- generate a grounded suggested response,
- return response + evidence + trace metadata.

Output includes:
- `message` (draft reply),
- `facts_used` (tool-sourced facts),
- `trace_id` and timing metadata.

## Evaluation
The included eval harness runs simple scenario checks against expected keywords and required fields. This should evolve into richer semantic checks and scoring.

## Roadmap
- **v0**: single workflow + deterministic tool (current).
- **v1**: add lead qualification + follow-up sequencing workflows.
- **v2**: multi-agent handoffs, persistent storage, and CRM integrations.
