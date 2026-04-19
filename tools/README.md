# Tools

## generator.py

Lightweight scaffold generator for assessment and learning-plan starters.

### Usage

```bash
python3 tools/generator.py \
  --name "Jane Doe" \
  --role "Senior Marketing Manager" \
  --function marketing \
  --maturity developing \
  --workflow "Campaign brief creation and revision" \
  --jd-summary "Own campaign briefing, copy review, and cross-functional launch coordination" \
  --jd-metrics "Campaign launch cycle time, message quality score, conversion lift" \
  --jd-scope "Owns campaign brief and review process; partners with design and analytics" \
  --outcome "Reduce campaign brief cycle time from 5 days to 3 days within 60 days" \
  --output-dir generated/jane-doe
```

Valid `--function` values:
- `marketing`
- `sales-revops`
- `support-success`

Valid `--maturity` values:
- `emerging`
- `developing`
- `capable`

The generator will reject overly generic outcomes and prompt you to provide a measurable, role-specific target.
It also requires job-description grounding so generated plans map to real role scope and success metrics.
