"""Runs one candidate solution against one test file in a separate process. Prints JSON."""
import sys, json, importlib.util, traceback
from decimal import Decimal
from datetime import date, datetime, timezone, timedelta

sol_path, cases_path, func_name = sys.argv[1], sys.argv[2], sys.argv[3]
NS = {"Decimal": Decimal, "date": date, "datetime": datetime, "timezone": timezone, "timedelta": timedelta}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def same(got, exp):
    if type(got) is not type(exp):
        return False
    if isinstance(exp, Decimal):
        return str(got) == str(exp)
    if isinstance(exp, dict):
        return got.keys() == exp.keys() and all(same(got[k], exp[k]) for k in exp)
    if isinstance(exp, list):
        return len(got) == len(exp) and all(same(a, b) for a, b in zip(got, exp))
    return got == exp


out = {"load_error": None, "results": []}
try:
    fn = getattr(load(sol_path, "solution"), func_name)
except Exception:
    out["load_error"] = traceback.format_exc(limit=3)
    print(json.dumps(out)); sys.exit(0)

for case in load(cases_path, "cases").CASES:
    r = {"name": case["name"], "call": f"{func_name}({case['args']})", "expected": case["expect"]}
    args = eval("(" + case["args"] + ",)", dict(NS))
    try:
        got = fn(*args)
        r["got"] = repr(got)
        if case["expect"].startswith("RAISES:"):
            r["ok"] = False
            r["message"] = f"expected {case['expect'][7:]} to be raised, but it returned {got!r}"
        else:
            exp = eval(case["expect"], dict(NS))
            r["ok"] = same(got, exp)
            if not r["ok"]:
                r["message"] = f"expected {exp!r}, got {got!r}"
    except Exception as e:
        want = case["expect"][7:] if case["expect"].startswith("RAISES:") else None
        r["got"] = f"{type(e).__name__}: {e}"
        r["ok"] = want is not None and type(e).__name__ == want
        if not r["ok"]:
            r["message"] = f"raised {type(e).__name__}: {e}" + (f" (expected {want})" if want else "")
    out["results"].append(r)
print(json.dumps(out))
