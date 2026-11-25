<div align="center">

# What to Submit

### RuleSmith &nbsp;·&nbsp; `P1B-RULESMITH`

**Due Sunday 6 December 2026**

</div>

## Checklist

| # | Deliverable | Where | Details |
|:--|:--|:--|:--|
| 1 | **Code repository** | Your Git repo | Public or shared with mentors. README with setup and one command to run each approach. Never commit API keys. |
| 2 | **Solutions** | `runs/oneshot/RS-01.py` ... and `runs/reflexion/RS-01.py` ... | One file per task for each approach, exactly as your agent produced it |
| 3 | **Scores** | `runs/*/score_check.json` | Output of `python harness/score.py runs/<approach> --suite check` |
| 4 | **Report** | `submission/REPORT.md` | See below |
| 5 | **Traces** | `submission/traces/RS-xx.json` | Full attempt log for 3 tasks: code, test results and the lesson for every attempt |
| 6 | **Demo video** | Link in your README | 5 minutes |

## The report (`submission/REPORT.md`)

1. **Your graph**: a diagram and one line per node.
2. **Results table**: one-shot vs Reflexion (and any variants), tasks solved, average attempts, total LLM calls or tokens.
3. **5 lessons your agent wrote** that actually fixed a task, copied from the traces.
4. **3 tasks it still fails**, and why you think so.
5. **What you tried that did not help.**

## How you are graded

| Area | Weight |
|:--|--:|
| Reflexion loop works as specified (generate, evaluate, reflect, memory, stop) | 30% |
| Improvement over one-shot, scored by mentors on the **private** tests | 25% |
| Honest measurement (same model, agent never saw `eval/check/`, reproducible runs) | 15% |
| Code quality (clean graph, state design, errors handled) | 15% |
| Report and demo | 15% |

## Your demo video must show

1. The graph (diagram or LangGraph drawing) in 30 seconds.
2. One task running live: first attempt fails, the lesson it writes, the next attempt passes.
3. Your before vs after table.
4. One thing you learned about *why* models fail on business rules.
