<div align="center">

# Walkthrough Video Script

### RuleSmith &nbsp;·&nbsp; `P1B-RULESMITH`

</div>

About 3 minutes (2:51).

Voice: Kokoro (open source, Apache-2.0). Images: generated for this video.

## Scene 1: Small rules

> Every bank runs on thousands of small rules. Waive the foreign fee for Voyager cards. But not at the ATM. Wires sent after five p.m. New York time go out tomorrow. Never more than three overdraft fees in a day.

## Scene 2: The edges

> Product writes these rules in plain English. Engineers turn them into code. And the bugs hide in the edges. Round half up, not half even. New York time, with daylight saving. Day thirty still counts.

## Scene 3: Asking once

> So the team tried the obvious thing. Paste the rule into an AI model, and take the code. It looked great in the demo. Then the tests ran. A small model, asked once, got fifteen rules out of twenty right. The other five were wrong... and it never said so.

## Scene 4: Welcome

> Welcome to Project One B. RuleSmith! Your mission: build an agent that learns from its own mistakes.

## Scene 5: Three reflection methods

> There are three well known ways to make a model improve its own work. Basic reflection: write, critique, rewrite. Reflexion: check the answer against something real, write down the lesson, and remember it. And tree search, which tries many answers and searches through them. You will build the second one. Reflexion.

## Scene 6: The Reflexion loop

> Here is the loop. Generate the function. Evaluate it, by running the tests. If something fails, reflect. Which rule did I break, and what will I do differently? Save that lesson to memory. Then try again, with every lesson in hand.

## Scene 7: What is in the repo

> The repo gives you everything you need. Twenty banking rules, from fees and deadlines to card masking and time zones. A test harness that your agent calls as its judge. Check tests, for your own honest scoring. And a starter, with a working baseline and a graph for you to finish.

## Scene 8: The catch

> But here is the catch. Each rule has only three visible tests. Passing them does not mean the code is right. So your agent must write its own tests from the spec... and some of those tests will be wrong. Deciding which feedback to trust is the real project.

## Scene 9: Baselines and your target

> We measured the baselines. One shot: fifteen out of twenty. Basic Reflexion: fifteen. Reflexion with its own tests: seventeen. Your target is to beat seventeen. Same small model. And show us why it worked.

## Scene 10: Watch first

> Start with the videos in AI Launchpad, on Skool. AI Fundamentals for Beginners, for your first API calls. Then, Coding a LangGraph Chatbot. Then, the User Story Reflection Agent. That is the exact loop shape you need.

## Scene 11: What you submit

> You submit your code, the solutions from both runs, your scores, a short report with the lessons your agent learned, three traces, and a five minute demo.

## Scene 12: Due date

> It is due Sunday, the sixth of December. Build the agent that gets better every time it fails. Welcome to Project One B. Let's build.
