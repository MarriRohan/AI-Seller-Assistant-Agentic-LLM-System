"""Simple trace helpers for workflow runs."""

from contextlib import contextmanager
from time import perf_counter
from uuid import uuid4


def new_trace_id() -> str:
    return str(uuid4())


@contextmanager
def timed_step() -> float:
    start = perf_counter()
    elapsed = {"seconds": 0.0}
    try:
        yield elapsed
    finally:
        elapsed["seconds"] = perf_counter() - start
