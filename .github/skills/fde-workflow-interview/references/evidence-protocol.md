# Evidence Package Protocol v1

Create exactly these files under `local-output/<session-id>/`.

## 1. `transcript.md`

Include:

- session ID, date/time, target duration, language, question count;
- participant identity mode, optional name/alias, required role and team;
- sequential `Q01`, `A01`, `Q02`, `A02` entries;
- playback, participant corrections, and final review response.

Preserve meaning accurately. Do not silently rewrite an answer into stronger language.

## 2. `evidence-register.md`

Use this table:

| Evidence ID | Claim | Status | Source | Scope | Notes / resolver |
|---|---|---|---|---|---|

Allowed status values:

- `Reported`: participant explicitly stated it;
- `Estimated`: participant supplied an approximate range;
- `Documented`: a later approved material can verify it;
- `Assumption`: a working inference, not a fact;
- `Open`: no answer yet;
- `Contradicted`: sources or statements conflict.

Assign IDs sequentially as `E001`, `E002`, and so on. Every substantive conclusion in other outputs must cite one or more IDs.

## 3. `discovery-report.md`

Use these sections:

1. Session and workflow scope
2. Executive summary
3. As-Is workflow table
4. Normal path and exception path
5. Roles, systems, data, and business rules
6. Pain points, symptoms, root causes, and control gaps
7. Current baseline
8. To-Be workflow and Human Gates
9. Opportunity classification
10. Open Questions
11. Evidence coverage and confidence
12. Participant review status

Add evidence citations such as `[E003, E007]` after every claim. A Mermaid flow is optional; the workflow table is required.

## 4. `result.json`

Follow [the JSON Schema](discovery-result.schema.json). Use `null` or empty arrays for unknown optional values. Never create a plausible value to fill a gap.

Required claim-bearing objects use `evidence_ids`. Opportunities must use one of `process-governance`, `rule-automation`, `data-product`, or `ai-assisted`.

## 5. `submission-checklist.md`

Include:

- participant review checkboxes;
- sensitive-information review;
- current `review.status`;
- exact supporting materials requested, with purpose, suggested filename, likely Owner, sensitivity warning, and related Evidence IDs;
- reminder that the Skill did not inspect or copy those materials;
- instructions to submit through an approved internal channel, never this public repository.

## Review transition

Initial status is `draft`. Change to `approved_by_participant` only after an explicit confirmation. Record `reviewed_at` and all corrections. Approval means “accurate representation for discovery,” not business, compliance, or implementation approval.
