# Build and Run Instructions

## 1) Clone

```bash
git clone <PUBLIC_REPO_URL>
cd <PUBLIC_REPO_FOLDER>
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

Valid `--function` values:
- `marketing`
- `sales-revops`
- `support-success`

Valid `--maturity` values:
- `emerging`
- `developing`
- `capable`

## 3) Validate Output

You should see:
- `generated/<your-name>/assessment-starter.md`
- `generated/<your-name>/learning-plan-starter.md`
- `generated/<your-name>/reference-learning-plan.md`

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
