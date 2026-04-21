# Contributing

## What This Project Accepts

Contributions that improve the framework's accuracy, accessibility, or usefulness for GTM teams:

- Corrections to rubric criteria or scoring anchors
- New or improved role-specific examples in `assessment/calibrated-scoring-examples.md`
- Additional function track learning plans (beyond Marketing, Sales/RevOps, Support/Success)
- Improvements to `tools/generator.py` — better validation, new parameters, cleaner output
- Documentation improvements: clearer language, missing steps, broken references

## What This Project Does Not Accept

- Changes that introduce role-specific consulting playbooks or client materials
- Major framework changes without discussion first — open an issue to propose
- Pull requests without a clear description of what changed and why

## How to Contribute

1. Fork the repo
2. Create a branch (`git checkout -b improve/rubric-delegation-criteria`)
3. Make your change, test it, and describe it clearly
4. Open a pull request using this format:

```
## What changed
[One sentence describing the specific file(s) and content affected]

## Why it's an improvement
[What problem this fixes or what gap it closes — reference the file and section if possible]

## How you tested it
[Examples: "Ran the generator with the updated validation logic and confirmed output"; 
"Completed the manual path against the updated rubric and compared to the worked example";
"Read the updated section against the original and confirmed the steps are unambiguous"]
```

Pull requests without this structure will be asked to revise before review.

## Opening Issues

Use GitHub Issues at https://github.com/c-b-g-m/gtm-ai-fluency-kit/issues to:
- Report broken generator behavior (include your command and error text)
- Suggest new function tracks
- Flag gaps in documentation or examples

## Framework Lineage

The 4D model and rubric are a practical synthesis of:
- Anthropic's AI fluency teaching and assessment concepts
- Zapier-style progression and accountability framing for role-based AI capability

This is not a verbatim reproduction of either source. Contributions should maintain this attribution and not introduce unattributed proprietary frameworks.
