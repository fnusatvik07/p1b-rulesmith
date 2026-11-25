# Learning Path

## What to watch, in order

All six are in **AI Launchpad** on Skool: [Classroom](https://www.skool.com/the-agent-lab-3899/classroom). The lesson number is its position in the course's lesson list. Watching at 1.5x takes about 6 hours.

| # | When | Course → lesson | Length | Focus on |
|:--|:--|:--|:--|:--|
| 1 | Wed 25 Nov | **AI Fundamentals for Beginners** → #1 *LLM API Calls, Messages, Tokens and Memory* | 1h 54m | API calls, system / human / AI messages, tokens, JSON output. Everything the `generate` and `reflect` nodes do. |
| 2 | Thu 26 Nov | **Claude Code for Builders** → #2 *Claude Code: Setup to First Build* | 59m | Install and run Claude Code. Give clear, objective asks (you are the PM, Claude is the engineer). Plan mode vs Accept Edits vs Auto. |
| 3 | Thu 26 Nov | **Claude Code for Builders** → #4 *What is Claude.md ?* | 1h 15m | What goes in a CLAUDE.md and why it makes Claude remember your project. |
| 4 | Fri 27 Nov | **Claude Code for Builders** → #5 *CLAUDE.md Scopes, Rules & Auto Memory* | 1h 17m | Project vs user scope, rules, and auto memory. |
| 5 | Sat 28 Nov | **Agent Builder** → #13 *Bonus- Coding LangGraph Chatbot* | 1h 33m | The simplest LangGraph app: state, nodes, edges, reducers, compile. |
| 6 | Sun 29 Nov | **Agent Builder** → #14 *Bonus- Building a User Story Reflection Agent* | 1h 59m | Generate node, reflect node, conditional edge, a loop with an exit. |

Then read **Reflection Agents** on the LangChain blog: [blog.langchain.com/reflection-agents](https://blog.langchain.com/reflection-agents).

## Use Claude Code on this project

1. **Run it** in your RuleSmith repo and let it explore the code before you ask for anything.
2. **Give it clear asks and plan first.** Use Plan mode before each node (`generate`, `evaluate`, `reflect`), read the plan, then approve.
3. **Write a CLAUDE.md** for the repo: how to run the harness, "money is always `Decimal`", "the agent must never read `eval/check/`".
4. **Use auto memory.** Let Claude save what it learns about the project, and check what it saved at the end of each session.

Write the three nodes yourself. Use Claude Code to scaffold, review and debug.

### The three reflection methods

| Method | How it works | Feedback comes from |
|:--|:--|:--|
| **1. Basic Reflection** | Generate, critique, revise, for a fixed number of rounds | The LLM's own opinion |
| **2. Reflexion** ← *you build this* | Act, evaluate against something real, write a lesson, remember it, retry | External signal (here: tests) + memory of lessons |
| **3. Language Agent Tree Search (LATS)** | Try several candidates, score them, search a tree of attempts | Scores + reflections, with search |

Video 6 builds method 1. RuleSmith is method 2: the same loop shape, but the critique is grounded in test results, and the lessons are kept.

## Go deeper (optional)

| What | Where |
|:--|:--|
| Reflexion paper (Shinn et al., 2023) | [arxiv.org/abs/2303.11366](https://arxiv.org/abs/2303.11366) |
| Agent Builder → #12 *Class 7- Introduction to LangGraph* and *Class 8: Thinking in LangGraph & Workflow Patterns* | Classroom → *Agent Builder* |
| *Building effective agents* (the "evaluator-optimizer" workflow) | [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) |

## Suggested plan

| Days | Focus | Output |
|:--|:--|:--|
| Wed 25 to Thu 26 Nov | Videos 1 to 3, set up Claude Code and CLAUDE.md | One-shot baseline scored |
| Fri 27 to Sun 29 Nov | Videos 4 to 6, the blog post | Auto memory on, your own one-node LangGraph chatbot |
| Mon 30 Nov to Tue 1 Dec | Fill in the graph | `generate → evaluate → reflect` loop working on 3 tasks |
| Wed 2 to Thu 3 Dec | Memory, stop rule, traces, all 20 tasks | Reflexion run scored (3 runs) |
| Fri 4 to Sun 6 Dec | One stretch goal, report and demo | Submission (due Sunday) |
