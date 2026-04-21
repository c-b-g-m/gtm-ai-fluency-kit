# Tools

## generator.py

Lightweight scaffold generator. Takes your role context as input and writes three pre-filled starter files to an output directory.

Run from the repository root (the folder containing `tools/`, `learning-plans/`, `templates/`).

### Example

```bash
python3 tools/generator.py \
  --name "Jane Doe" \
  --role "Senior Marketing Manager" \
  --function marketing \
  --maturity developing \
  --workflow "Campaign brief creation and revision" \
  --jd-summary "Own campaign briefing, copy review, and cross-functional launch coordination for 4–6 campaigns per quarter" \
  --jd-metrics "Campaign launch cycle time, message quality score, conversion lift" \
  --jd-scope "Owns campaign brief and review process; partners with design and analytics" \
  --outcome "Reduce campaign brief cycle time from 5 days to 3 days within 60 days" \
  --output-dir generated/jane-doe
```

### Flag Reference

| Flag | Required | What to put here |
|------|----------|-----------------|
| `--name` | Yes | Your name — used to label the output files |
| `--role` | Yes | Your job title |
| `--function` | Yes | Your function track: `marketing`, `sales-revops`, or `support-success` |
| `--maturity` | Yes | Your current self-assessed level: `emerging`, `developing`, or `capable` |
| `--workflow` | Yes | One specific recurring workflow you want to improve — name the task, not the category (e.g., "writing weekly pipeline reports" not "sales work") |
| `--jd-summary` | Yes | 1–3 sentences of actual language from your job description — specific responsibilities, not category descriptions |
| `--jd-metrics` | Yes | The success metrics your role is evaluated on (cycle time, revenue, CSAT, conversion, etc.) |
| `--jd-scope` | Yes | What you own vs. what you hand off — your decision boundary |
| `--outcome` | Yes | The specific, measurable result you want to achieve and by when (e.g., "Reduce escalation rework by 20% in 60 days") |
| `--output-dir` | No | Where to write the files — defaults to `generated/` |

### Validation

The generator checks `--outcome` and `--jd-summary` for specificity before writing any files. If either is too generic (too short, or matches a vague pattern), it exits with an error message and an example of what a valid input looks like.

**It does not re-prompt.** Fix the flagged input and rerun the full command.

A well-formed `--outcome` has: *what changes*, *by how much*, *by when*.
A well-formed `--jd-summary` uses language from your actual job description, not a category description.

### Output

Three files in `--output-dir`:

| File | What it is | What to do |
|------|-----------|-----------|
| `assessment-starter.md` | Assessment form pre-filled with your role context | Fill in your 1–3 scores per dimension and complete Priority Gaps |
| `learning-plan-starter.md` | Learning plan pre-filled with your role context and a Stop Doing / Start Doing starter | Fill in your 30/60/90 milestones after completing the assessment |
| `reference-learning-plan.md` | Read-only reference showing realistic milestones for your function track | Use as a guide while writing your learning plan — do not fill this in |

Full instructions for completing the generated files are in `BUILD.md`.
