"""RuleSmith test runner: the evaluator your agent calls.

    from harness.runner import run_tests
    report = run_tests("RS-01", code_string)               # visible tests (the agent may see these)
    report = run_tests("RS-01", code_string, suite="check")  # check tests (for YOUR scoring only)

Command line:
    python harness/runner.py RS-01 my_solution.py [--suite visible|check]

The candidate code runs in a separate Python process with a time limit, so a bad
solution (infinite loop, crash, sys.exit) cannot take your agent down.
"""
import json, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = json.load(open(os.path.join(ROOT, "tasks", "index.json")))
TASKS = {t["id"]: t for t in INDEX}


def suite_path(task_id, suite):
    if suite == "visible":
        return os.path.join(ROOT, "tasks", TASKS[task_id]["folder"], "tests_visible.py")
    if suite == "check":
        return os.path.join(ROOT, "eval", "check", f"{task_id}.py")
    p = os.path.join(ROOT, "_private", "private_tests", f"{task_id}.py")
    if os.path.exists(p):
        return p
    raise ValueError(f"unknown suite {suite!r}")


def run_tests(task_id, code, suite="visible", timeout=10):
    task = TASKS[task_id]
    with tempfile.TemporaryDirectory() as tmp:
        sol = os.path.join(tmp, "solution.py")
        with open(sol, "w") as fh:
            fh.write(code)
        cmd = [sys.executable, "-I", os.path.join(ROOT, "harness", "_child.py"), sol, suite_path(task_id, suite), task["func"]]
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=tmp)
        except subprocess.TimeoutExpired:
            return dict(task_id=task_id, suite=suite, passed=0, total=None, all_passed=False, error=f"timed out after {timeout}s", failures=[])
    try:
        out = json.loads(p.stdout.strip().splitlines()[-1])
    except Exception:
        return dict(task_id=task_id, suite=suite, passed=0, total=None, all_passed=False, error=(p.stderr or p.stdout)[-2000:], failures=[])
    if out["load_error"]:
        return dict(task_id=task_id, suite=suite, passed=0, total=None, all_passed=False, error=out["load_error"], failures=[])
    res = out["results"]
    passed = sum(r["ok"] for r in res)
    return dict(task_id=task_id, suite=suite, passed=passed, total=len(res), all_passed=passed == len(res), error=None,
                failures=[{k: r.get(k) for k in ("name", "call", "message")} for r in res if not r["ok"]])


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("task_id"); ap.add_argument("solution_file"); ap.add_argument("--suite", default="visible")
    a = ap.parse_args()
    print(json.dumps(run_tests(a.task_id, open(a.solution_file).read(), a.suite), indent=2))
