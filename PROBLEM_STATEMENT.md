# RuleSmith: Problem Statement

**Project 1B · `P1B-RULESMITH` · Wed 25 Nov to Sun 6 Dec 2026**

## 1. The situation

Harborline Bank's product team writes business rules in plain English: fees, deadlines, limits, rewards. Engineering turns each rule into a small, well-tested Python function. The backlog is long, so the team wants an agent that drafts these functions.

They tried the obvious thing: paste the rule into an LLM and take the answer. It looked great in the demo. In testing, about a third of the functions broke on an edge the rule clearly stated: rounding half up, New York time with daylight saving, "day 30 still counts", a cap, a tie-break.

The team does not need a smarter model. They need an agent that **checks its own work, understands its mistakes and does not repeat them.**

## 2. What you build

An agent that, for each of the 20 tasks in `tasks/`:

1. **Generates** a Python function from `spec.md`.
2. **Evaluates** it by calling `harness.runner.run_tests(task_id, code, suite="visible")`.
3. **Reflects** when tests fail: a short written lesson that names the rule it broke and what to do differently.
4. **Remembers** every lesson for that task and puts them into the next attempt.
5. **Stops** when all tests pass, or after a maximum number of attempts that you choose and justify.

This is the **Reflexion** pattern (Shinn et al., 2023). Build it as a LangGraph graph: state, nodes, a conditional edge and a loop.

## 3. The catch (this is the real project)

Each task has only **3 visible tests**. The check and private tests probe edges the visible tests do not. So an agent that only reacts to visible failures stops too early: the code passes 3 tests and still breaks the rules.

The strongest Reflexion agents also **write their own tests from the spec**, the way the original paper did for coding tasks. But the model's own tests can be wrong, and a wrong test teaches a wrong lesson. Deciding which feedback to trust is the core engineering problem of this project.

## 4. Rules of the game

| Rule | Why |
|:--|:--|
| Use **one small model** for the whole run, for example `gpt-4o-mini`, `claude-haiku` or a local model. Same model for one-shot and Reflexion. | The point is lifting a cheap model, not buying a bigger one. |
| Your agent may read `spec.md` and the visible tests. It must **never** read `eval/check/`. | Those tests are your honest measuring stick. |
| No hand-editing of generated solutions. | We grade the agent, not you. |
| Python 3.9+, standard library only, inside the generated functions. | Same as the bank's runtime. |

## 5. Baselines we measured

With `gpt-4o-mini`, tasks fully solved out of 20:

| Approach | Check tests (you can measure) | Private tests (mentors grade) |
|:--|--:|--:|
| One-shot (one call, no feedback) | 15 | 13 |
| Basic Reflexion (visible tests only, up to 4 attempts) | 15 | 13 |
| Reflexion + self-written tests (naive: trusts every test) | 17 | 14 |

LLM output varies: another one-shot run solved only 11 tasks across all tests. **Run each approach 3 times and report the average**, not your best run.

**Your target: beat 17 / 20 on the check tests** with the same kind of model, gain on the private tests too, and explain what made the difference.

## 6. Must-haves

- [ ] LangGraph graph with `generate`, `evaluate`, `reflect` nodes and a conditional edge
- [ ] State that keeps every attempt: code, test results, reflection (use a reducer to append)
- [ ] Memory: lessons from earlier attempts go into the next prompt
- [ ] A stop rule (all pass, or max attempts) and a cost guard (count tokens or calls)
- [ ] One-shot baseline and Reflexion run on all 20 tasks, both scored with `harness/score.py`
- [ ] A trace log per task: every attempt, its test results and the lesson written

## 7. Stretch goals

- [ ] **Self-written tests** with a way to decide when a failing self-test is wrong (for example: ask the model to recompute the expected value step by step from the rule, or keep only tests that two independent samples agree on)
- [ ] **Best-so-far**: if a new attempt passes fewer tests than an earlier one, keep the earlier code
- [ ] **Cross-task memory**: lessons that apply everywhere ("money is Decimal, round half up") carried from task to task, and a run that shows whether it helps
- [ ] LangSmith or Langfuse tracing of the whole graph

## 8. Out of scope

A UI, a database, deployment. This is a one-week build about the loop.
