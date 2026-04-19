# Worked Example — Support and Customer Success

This example shows a completed assessment and learning plan for a Support and Customer Success professional. Use it as a reference when filling in your own templates.

---

## Participant Context

- **Name:** Morgan
- **Role:** Support Team Lead
- **Function:** Support and Customer Success
- **JD summary:** Manages Tier 1 and Tier 2 support queue, owns response quality and escalation decisions, and trains new support agents.
- **Role scope:** Full ownership of Tier 1 response and Tier 2 triage. Escalates to engineering for Tier 3. Does not own product roadmap input.
- **Role success metrics:** First response time, customer satisfaction score (CSAT), escalation rate, resolution rate.
- **Primary recurring workflow:** Triage and first-draft response for high-volume Tier 1 tickets.
- **Target outcome:** Improve CSAT on AI-assisted Tier 1 responses from current baseline to match manually written response CSAT within 60 days.

---

## Baseline Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Delegation | 2 | Uses AI for low-complexity tickets when queue is full. No formal triage criteria — decision is made case by case. High-complexity and sensitive tickets always stay human-owned but this isn't written down. |
| Description | 2 | Prompt includes ticket text and customer tier. Revises once if tone is off. Has no saved templates; writes prompts from memory. |
| Discernment | 3 | Runs a consistent review before sending: accuracy, tone, policy compliance, escalation trigger check. Has caught AI errors that would have created policy violations. Documents these in a running note. |
| Diligence | 3 | Removes customer PII before pasting into AI tool. Flags AI-assisted responses in internal ticketing notes. Named as accountable reviewer for all responses before send. |

**Evidence available:** Running error-catch log (informal), ticketing system notes showing AI flag, one documented policy compliance catch.

---

## Priority Gaps

1. **Delegation (2 → 3):** No written triage criteria. Relies on intuition — works for Morgan but isn't teachable or auditable. A written decision framework would make the workflow scalable.
2. **Description (2 → 3):** No prompt templates. Rebuilds context from scratch on each ticket, which slows throughput and creates inconsistency.

---

## Stop Doing / Start Doing

Stop doing:
- Making triage decisions by feel, without a documented framework.
- Writing prompts from scratch for every ticket type.

Start doing:
- Using a written triage framework that specifies which ticket types go to AI draft and which stay human-written.
- Maintaining a prompt library with templates for the top 5 ticket categories by volume.

---

## 30/60/90 Plan

### 30 Days — Foundation

- Write a triage decision framework: for each of the top 5 ticket categories, define whether AI draft is appropriate, what context the prompt must include, and what the review pass looks like.
- Build a prompt library with 5 templates, one per category.
- Track CSAT for AI-assisted vs. manually written responses separately for 30 days.

**Evidence:** Written triage framework, prompt library v1, 30-day CSAT split by response type.
**JD alignment:** Maps to CSAT (primary success metric) and escalation rate.

### 60 Days — Operationalization

- Run the triage framework on 100% of Tier 1 tickets for 30 consecutive days.
- Review CSAT data: target AI-assisted responses reach parity with manually written responses.
- Update prompt library based on error log patterns.

**Evidence:** CSAT parity data, prompt library v2, updated error log.
**JD alignment:** CSAT improvement directly maps to primary success metric.

### 90 Days — Scale

- Train two new agents on the triage framework and prompt library during onboarding.
- Write a one-page AI use guide for the support team: what we use it for, what we verify, what we never do.
- Define an escalation trigger for AI-generated responses that may need senior review before send.

**Evidence:** Onboarding materials with AI section, team AI use guide, escalation trigger documented in runbook.
**JD alignment:** Agent training maps directly to JD responsibility for training new support staff.

---

## Non-Generic Check

- Workflow named: Tier 1 ticket triage and first-draft response ✓
- Measurable signal: CSAT parity between AI-assisted and manual responses within 60 days ✓
- Accountability owner: Morgan owns all review and send decisions before ticket closes ✓
- JD alignment: maps to CSAT, escalation rate, and agent training scope ✓
