# Troubleshooting

## Setup Issues

### Python not installed

Install Python 3.10 or newer, then rerun `python3 --version`.

### Running from wrong folder

Generator expects to run from repository root.

Fix:
```bash
pwd
ls
```
Confirm folders like `tools/` and `learning-plans/` are present.

## Output Issues

### Output feels generic

- Improve `--outcome` specificity.
- Add role-specific recurring workflows to your generated draft.
- Use reference plans for stronger role language.

### Missing accountability checks

Add:
- Disclosure statement
- Human review gate
- Risk and privacy checks

## Getting Unblocked

1. Re-run quickstart from `START-HERE.md`.
2. Compare with `examples/`.
3. Open an issue at https://github.com/c-b-g-m/gtm-ai-fluency-kit/issues with:
   - your command
   - error text
   - expected output
