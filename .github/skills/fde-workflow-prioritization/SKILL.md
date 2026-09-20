---
name: fde-workflow-prioritization
description: Aggregate participant-approved FDE workflow discovery packages into an evidence-linked portfolio, value-versus-feasibility matrix, and leadership discussion agenda. Use after interview packages have been manually placed in employee-submissions. Do not upload evidence or make final business, security, compliance, or management decisions.
---

# FDE Workflow Prioritization

Turn multiple reviewed discovery packages into a decision aid. Preserve sources, uncertainty, and disagreement; do not manufacture precision or replace accountable leaders.

## Boundaries

- Read only local files. Never upload, commit, push, email, or send evidence.
- Default input is `employee-submissions/`; accept another local path only when the user explicitly provides it.
- Never search outside the named submissions directory.
- Read `result.json` first. Read `discovery-report.md` and `evidence-register.md` only to resolve a specific gap. Read a transcript only when a cited conflict cannot otherwise be understood, and tell the user which Evidence IDs require that review.
- Do not inspect separately submitted screenshots, reports, spreadsheets, or datasets.
- Conclusions are recommendations for discussion, not approvals or audit findings.

## Before aggregating

Read:

- [Scoring framework](references/scoring-framework.md)
- [Portfolio output protocol](references/portfolio-output.md)
- [Interview evidence protocol](../fde-workflow-interview/references/evidence-protocol.md)
- [Discovery result schema](../fde-workflow-interview/references/discovery-result.schema.json)

## Input validation

Recursively locate `result.json` only under the selected submissions directory.

For every package:

1. Parse JSON and verify required top-level fields.
2. Require `schema_version` of `1.0.0`.
3. Require `review.status` of `approved_by_participant`.
4. Verify referenced Evidence IDs exist in the package evidence array.
5. Skip drafts, malformed files, unsupported versions, and structurally incomplete packages. Record the reason; never silently repair or infer missing content.

## Consolidation

- Group workflows only when trigger, scope, main output, and downstream decision are materially the same. Similar names alone are insufficient.
- Retain every source session ID and Evidence ID.
- If descriptions conflict, keep both versions, flag the field as `Contradicted`, and lower Evidence Confidence. Do not average incompatible values.
- Separate workflow improvement from proposed technology. Reclassify deterministic work away from AI when appropriate.

## Score and classify

Apply the scoring framework. Every component score needs a short rationale and Evidence IDs. Missing evidence lowers confidence; it does not justify a guessed score.

Use these recommendation classes exactly:

- `Now`
- `Validate`
- `Improve without AI`
- `Park`

Treat unmitigated High Risk as a barrier to `Now` regardless of numeric score.

## Write outputs

Create `local-portfolio/<YYYY-MM-DD>/` and write exactly:

- `workflow-portfolio.md`
- `priority-matrix.csv`
- `leadership-discussion.md`
- `portfolio.json`

Follow the portfolio output protocol. Cite package/session and Evidence IDs for all findings. Clearly separate source facts, calculations, recommendations, and unresolved decisions.

Finish with a concise summary of accepted packages, skipped packages and reasons, leading candidates, conflicts, evidence gaps, and decisions required from leadership.
