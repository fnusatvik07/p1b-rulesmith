"""RuleSmith: Reflexion graph skeleton. Fill in the TODOs.

    python starter/reflexion_graph.py RS-09        # one task, prints every attempt
    python starter/reflexion_graph.py              # all tasks -> runs/reflexion/

Graph:   generate -> evaluate -> (all pass or out of attempts?) -> END
                                        \\-> reflect -> generate ...
"""
import json, operator, os, sys
from typing import Annotated, TypedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from harness.runner import TASKS, run_tests
from langgraph.graph import StateGraph, END
from starter.oneshot import ask_llm, extract_code

MAX_ATTEMPTS = 4   # TODO: choose and justify


class State(TypedDict):
    task_id: str
    spec: str
    code: str                                         # latest attempt (replaced each loop)
    test_report: dict                                 # latest run_tests() result (replaced)
    lessons: Annotated[list, operator.add]            # memory: every reflection so far (appended)
    attempts: Annotated[list, operator.add]           # trace: one dict per attempt (appended)


def generate(state: State) -> dict:
    """Write (or rewrite) the function. On attempt 2+ the prompt must include the lessons."""
    prompt = ("Implement this function in Python 3.9 using only the standard library. "
              "Return one python code block with the full module, imports included.\n\n" + state["spec"])
    if state["lessons"]:
        # TODO: add the lessons (and maybe the previous code) to the prompt. Wording matters: experiment.
        pass
    code = extract_code(ask_llm(prompt))
    return {"code": code}


def evaluate(state: State) -> dict:
    """Run the visible tests. (Stretch: also run tests your agent wrote itself.)"""
    report = run_tests(state["task_id"], state["code"], suite="visible")
    attempt = {"n": len(state["attempts"]) + 1, "code": state["code"], "passed": report["passed"],
               "total": report["total"], "failures": report["failures"], "error": report["error"]}
    return {"test_report": report, "attempts": [attempt]}


def reflect(state: State) -> dict:
    """Turn the test failures into a short, specific lesson for the next attempt."""
    # TODO: build a prompt with the spec, the code and the failures (state["test_report"]).
    #       Ask for 2-4 sentences: which numbered rule was broken, and what to do differently.
    lesson = "TODO"
    return {"lessons": [lesson]}


def should_continue(state: State) -> str:
    # TODO: return "done" when all tests pass or MAX_ATTEMPTS is reached, else "reflect".
    return "done"


def build_graph():
    g = StateGraph(State)
    g.add_node("generate", generate)
    g.add_node("evaluate", evaluate)
    g.add_node("reflect", reflect)
    g.set_entry_point("generate")
    g.add_edge("generate", "evaluate")
    g.add_conditional_edges("evaluate", should_continue, {"reflect": "reflect", "done": END})
    g.add_edge("reflect", "generate")
    return g.compile()


def solve(task_id: str) -> dict:
    spec = open(os.path.join(ROOT, "tasks", TASKS[task_id]["folder"], "spec.md")).read()
    return build_graph().invoke({"task_id": task_id, "spec": spec, "code": "", "test_report": {}, "lessons": [], "attempts": []})


if __name__ == "__main__":
    ids = sys.argv[1:] or sorted(TASKS)
    out = os.path.join(ROOT, "runs", "reflexion"); os.makedirs(os.path.join(out, "traces"), exist_ok=True)
    for tid in ids:
        final = solve(tid)
        open(os.path.join(out, f"{tid}.py"), "w").write(final["code"])
        json.dump({"task_id": tid, "lessons": final["lessons"], "attempts": final["attempts"]},
                  open(os.path.join(out, "traces", f"{tid}.json"), "w"), indent=2)
        last = final["attempts"][-1]
        print(f"{tid}: {len(final['attempts'])} attempt(s), visible {last['passed']}/{last['total']}")
