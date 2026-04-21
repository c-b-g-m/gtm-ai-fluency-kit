# Build and Run Instructions

## Prerequisites

- Git
- Python 3.10 or newer (`python3 --version` to check)
- A shell terminal (macOS/Linux terminal, Windows PowerShell or Git Bash)

## 1) Clone

```bash
git clone https://github.com/c-b-g-m/gtm-ai-fluency-kit.git
cd gtm-ai-fluency-kit
```

## 2) Generate Starter Assets

```bash
python3 tools/generator.py \
  --name "Your Name" \
  --role "Your Role" \
  --function marketing \
  --maturity developing \
  --workflow "Name one recurring workflow you own" \
  --jd-summary "Summarize the role responsibilities from your job description" \
  --jd-metrics "List role success metrics from your job description" \
  --jd-scope "Describe your ownership boundaries and decision scope" \
  --outcome "Your key business outcome" \
  --output-dir generated/your-name
```

Valid `--function` values (these map to the three function tracks used throughout the kit):
- `marketing` → Marketing
- `sales-revops` → Sales and RevOps
- `support-success` → Support and Customer Success

Valid `--maturity` values:
- `emerging`
- `developing`
- `capable`

## 3) What You Get

You should see three files in `generated/<your-name>/`:

**`assessment-starter.md`** — Your assessment form, pre-filled with your role, workflow, JD details, and context. Open this first. Fill in your scores (1–3) for each dimension and complete the Scoring Summary and Priority Gaps sections. This is Document 1.

**`learning-plan-starter.md`** — Your learning plan form, pre-filled with the same role context. Open this after completing your assessment. Fill in your 30/60/90 milestones based on the two gap dimensions you identified. This is Document 2.

**`reference-learning-plan.md`** — A read-only reference showing what realistic milestones look like for your function track at each phase. Do not fill this in. Use it as a guide while building your learning-plan-starter.

The flow is: complete `assessment-starter.md` → carry your gaps into `learning-plan-starter.md` → use `reference-learning-plan.md` and `examples/[function]-example.md` as reference while you fill it in.

**Total time:** about 35–50 minutes (5 min setup + 30–45 min to complete both documents).

## 4) Manual-Only Path (No Script)

If you do not want to run scripts:
1. Copy templates in `templates/`.
2. Fill them manually.
3. Use `examples/` as reference.

## Common Errors

- `python3: command not found`
  - Install Python 3.10+ and retry.
- `No such file or directory: learning-plans/...`
  - Ensure you are running from repo root.
- Invalid function choice
  - Use one of the supported `--function` values listed above.
- Outcome is too generic
  - Rewrite outcome with a measurable business target and workflow context.
- JD summary is too generic
  - Add specific job responsibilities, role scope, and expected metrics from your job description.
