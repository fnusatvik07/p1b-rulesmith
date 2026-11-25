"""One-shot baseline: one LLM call per task, no feedback. Writes runs/oneshot/RS-xx.py

    python starter/oneshot.py                # all 20 tasks
    python starter/oneshot.py RS-01 RS-09    # some tasks
    MODEL=gpt-4o-mini python starter/oneshot.py
"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from harness.runner import TASKS
from openai import OpenAI

MODEL = os.environ.get("MODEL", "gpt-4o-mini")
client = OpenAI()   # reads OPENAI_API_KEY


def ask_llm(prompt: str) -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a careful Python engineer at a bank."},
            {"role": "user", "content": prompt},
        ],
    )
    return resp.choices[0].message.content


def extract_code(text: str) -> str:
    blocks = re.findall(r"```(?:python)?\n(.*?)```", text, re.S)
    return blocks[-1] if blocks else text


def main(ids):
    out = os.path.join(ROOT, "runs", "oneshot")
    os.makedirs(out, exist_ok=True)
    for tid in ids:
        spec = open(os.path.join(ROOT, "tasks", TASKS[tid]["folder"], "spec.md")).read()
        prompt = ("Implement this function in Python 3.9 using only the standard library. "
                  "Return one python code block with the full module, imports included.\n\n" + spec)
        code = extract_code(ask_llm(prompt))
        open(os.path.join(out, f"{tid}.py"), "w").write(code)
        print("wrote", tid)


if __name__ == "__main__":
    main(sys.argv[1:] or sorted(TASKS))
