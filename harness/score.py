"""Score a folder of solutions (one file per task, named RS-01.py ... RS-20.py).

    python harness/score.py runs/reflexion/ --suite check

Prints a table and writes <folder>/score_<suite>.json.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness.runner import run_tests, TASKS


def score(folder, suite="check"):
    rows = []
    for tid in sorted(TASKS):
        f = os.path.join(folder, f"{tid}.py")
        if not os.path.exists(f):
            rows.append(dict(task_id=tid, solved=False, passed=0, total=None, note="missing")); continue
        r = run_tests(tid, open(f).read(), suite)
        rows.append(dict(task_id=tid, solved=r["all_passed"], passed=r["passed"], total=r["total"], note=r["error"] and r["error"].splitlines()[-1]))
    solved = sum(r["solved"] for r in rows)
    for r in rows:
        print(f"{r['task_id']}  {'PASS' if r['solved'] else 'fail'}  {r['passed']}/{r['total']}  {r['note'] or ''}")
    print(f"\nsolved {solved}/{len(rows)} on the '{suite}' suite")
    json.dump(dict(suite=suite, solved=solved, total=len(rows), tasks=rows), open(os.path.join(folder, f"score_{suite}.json"), "w"), indent=2)
    return solved


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("--suite", default="check")
    a = ap.parse_args(); score(a.folder, a.suite)
