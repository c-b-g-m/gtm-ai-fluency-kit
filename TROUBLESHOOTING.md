# Troubleshooting

---

## Assessment Issues (Manual Path)

### "I don't know what workflow to pick"

Pick the one thing you do weekly (or more often) that involves writing, researching, reviewing, or communicating — and where you already use or want to use AI. Not your most complex workflow. Not the one you think will impress anyone. The one you'd genuinely benefit from improving.

If you're still stuck: pick the task that takes the most time relative to the value it produces. That tension is usually where AI can help most.

---

### "My scores feel inflated — I'm not sure I can back them up"

That instinct is correct. Drop the score by one level.

The evidence rule is the whole point: a score of 3 means you can open an artifact right now — a saved prompt, a decision log, a checklist you use this week — and show it to someone. If you'd have to recreate it from memory, you're a 2 at best.

Read `HOW-TO-SCORE.md` for dimension-specific watch-outs. The most common inflation pattern is scoring Delegation high because you use AI often, when the actual question is whether you have *criteria* for what you delegate.

---

### "I can't write a diligence statement — I don't know what it is"

Open `examples/diligence-statement-examples.md` before you try to write one. It defines the format and shows one example per function track. A diligence statement is 3–5 sentences: what AI was used for, what data went into the prompt, who reviewed the output, and what you'd do differently. That's it.

---

### "The assessment questions feel too broad for my actual job"

They are intentionally role-neutral so they work across functions. Narrow them yourself: wherever the question says "recurring task," substitute the specific workflow you named in your Participant Context. That keeps your answers grounded in real work rather than hypotheticals.

---

### "I don't have 30 minutes right now"

Do the assessment in two sittings. Fill in the Participant Context and score yourself on two dimensions today. Come back for the other two and the learning plan. The form doesn't expire.

What to avoid: scoring all four dimensions quickly without reading the calibrated examples. That produces inflated scores that won't help you. Better to do two dimensions properly than four quickly.

---

## Generator Issues (Script Path)

### Python not installed

Install Python 3.10 or newer from python.org, then rerun:
```bash
python3 --version
```

---

### "No such file or directory: learning-plans/..."

You're running the generator from the wrong folder. The script expects to run from the repository root — the folder that contains `tools/`, `learning-plans/`, `templates/`, etc.

Fix:
```bash
pwd
ls
```
If you don't see `tools/` and `learning-plans/` listed, `cd` to the repo root and rerun.

---

### "Outcome is too generic"

The generator rejected your `--outcome` because it matched a generic pattern (e.g., "improve productivity," "use AI better," "work faster"). The generator exits when this happens — it does not re-prompt.

**Why this matters:** a generic outcome produces a generic plan. The generator enforces specificity so you don't waste 30 minutes filling in a plan that doesn't connect to your actual role.

Fix: rewrite `--outcome` to include a measurable target and a timeframe. Instead of:
```
"improve my productivity"
```
Use something like:
```
"Reduce weekly pipeline report prep from 3 hours to 90 minutes within 60 days"
```

A well-formed outcome has: *what changes*, *by how much*, *by when*.

---

### "JD summary is too generic"

Same root cause as a generic outcome — your `--jd-summary` was too short or matched a vague pattern. Fix: pull actual language from your job description. Include specific responsibilities, not role-category descriptions.

Instead of:
```
"responsible for marketing activities"
```
Use:
```
"Own campaign briefing, copy review, and cross-functional launch coordination for 4–6 campaigns per quarter"
```

---

### Output feels generic even after the generator accepted it

The generator validates that inputs aren't vague, but it can't make your outputs specific — only you can. If the generated files feel generic, the issue is usually one of:

1. **`--workflow` is too broad.** "Content creation" is a category. "Writing and revising weekly campaign briefs" is a workflow.
2. **`--jd-metrics` is missing.** If you left this vague, the plan has nothing to measure against. Go back and add your real role metrics — the ones your manager evaluates you on.
3. **`--outcome` is specific but disconnected from your actual pain.** The outcome drives the Stop Doing / Start Doing section. If it doesn't reflect a real bottleneck, the plan won't feel relevant.

Rerun the generator with tighter inputs rather than manually editing the generic output. The template is designed so that specific inputs produce specific outputs without extra work.

---

### Missing accountability checks in the generated plan

If your generated plan is missing disclosure statements, human review gates, or privacy checks, add them to the **Evidence Tracker** section of `learning-plan-starter.md`. These three things belong there:

- **Disclosure statement** — when and how you'll flag AI involvement in handoffs to teammates or clients
- **Human review gate** — who reviews AI-assisted output before it's used or shared, and at what stage
- **Risk and privacy check** — what you verify before pasting customer data, internal data, or PII into any AI tool

The Diligence dimension of the assessment specifically measures whether these are consistent habits, not one-off practices.

---

## After Day 30

### "I completed the plan but nothing really changed"

This is the most common outcome when the plan was specific on paper but too abstract to execute. Check which of these applies:

- **The workflow you named wasn't actually recurring.** If you picked a workflow you do quarterly instead of weekly, there weren't enough repetitions to build a habit. Pick a different workflow and restart the 30-day cycle.
- **The milestone was an outcome, not an action.** "Improve my prompt quality" is an outcome. "Write one new reusable prompt template by Friday and use it twice next week" is an action. If your plan had the former, rewrite it as the latter.
- **There was no accountability checkpoint.** Did anyone ask you about it at day 14? If not, the plan had no external pressure. Run the facilitator session with at least one other person, or share your plan with a colleague and ask them to check in at two weeks.

---

### "My manager didn't see value in this and I deprioritized it"

That's real. Frameworks without organizational buy-in stall. Two options:

1. **Do it for yourself first, quietly.** You don't need manager endorsement to run your own workflow differently. Pick your lowest-friction gap — usually Description — and change one thing in the next week. Then you have a before/after story.
2. **Run the facilitator session.** One team session is often more persuasive than a solo pitch. If your team leaves with shared language and one concrete commitment each, the framework earns its own legitimacy.

---

### "I finished the 30-day phase but didn't continue to 60 or 90"

Common. The 30-day phase is high-motivation; 60 and 90 require institutional memory. 

What works: at the end of your 30-day check-in, schedule the 60-day check-in before you close the document. If you wait until day 45 to schedule day 60, you won't. Same for 90. Block the time while the work is fresh.

---

### "I want to measure whether I actually improved"

Your evidence tracker in the learning plan is the mechanism — but it only works if you used it. Go back and answer honestly: what artifact do you have from this 30-day period that you didn't have at day zero?

If you have something — a prompt library, a decision log entry, a workflow doc — re-score yourself on that dimension. Compare to your baseline. Movement is real even if it's one level on one dimension.

If you have nothing: that's a signal, not a failure. It means the plan didn't produce the behavior that would create the artifact. Start smaller — one reusable prompt, documented, used at least three times. That's a 2 in Description.

---

## Getting Unblocked

**If you're stuck on a step:** Go back to `START-HERE.md` and re-read the workflow section. Confirm which document you're filling in and which you're using as reference.

**If your output doesn't match the examples:** Open `examples/[your-function]-example.md` and compare line by line. The worked examples show the level of specificity expected. If yours is more abstract, that's the gap.

**If something in the repo is broken or missing:** Open an issue at https://github.com/c-b-g-m/gtm-ai-fluency-kit/issues. You don't need a GitHub account to read existing issues, but you'll need one (free) to submit a new one. Describe what you were trying to do, what happened, and what you expected. No technical knowledge required — plain language is fine.
