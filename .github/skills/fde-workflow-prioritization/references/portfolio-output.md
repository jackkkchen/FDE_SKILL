# Portfolio Output Protocol v1

Write outputs to `local-portfolio/<YYYY-MM-DD>/`.

## `workflow-portfolio.md`

Include:

1. Run metadata and input directory
2. Accepted and skipped package counts
3. Consolidation method
4. Portfolio table
5. One evidence-linked card per consolidated workflow
6. Preserved contradictions
7. Cross-workflow dependencies
8. Evidence and Owner gaps
9. Limitations

Portfolio table columns:

| Workflow | Recommendation | Value | Feasibility | AI Fit | Risk | Confidence | Source sessions |
|---|---|---:|---:|---:|---|---|---|

Each score rationale must cite `<session-id>:<Evidence-ID>`.

## `priority-matrix.csv`

Use this exact header:

```csv
workflow_id,workflow_name,recommendation,value_score,feasibility_score,ai_fit,risk,evidence_confidence,source_sessions,primary_owner,top_evidence_gap
```

Quote fields containing commas. Use period decimal separators.

## `leadership-discussion.md`

Organize the meeting around decisions rather than presentations:

1. Recommended `Now` candidates and why
2. `Validate` candidates and the cheapest next validation
3. High-risk or blocked items requiring leadership direction
4. Opportunities better solved without AI
5. Conflicting employee accounts to resolve
6. Proposed next actions with Owner and decision needed

Never present the matrix as an approved roadmap.

## `portfolio.json`

Include:

- `portfolio_version`: `1.0.0`
- `generated_at`
- `input_directory`
- `accepted_packages`: session IDs
- `skipped_packages`: path and reason
- `workflows`: consolidated workflow objects
- `conflicts`
- `cross_workflow_dependencies`
- `leadership_decisions_required`

Each workflow object contains component scores, formulas, rationales, Evidence IDs, sources, recommendation, risk/mitigations, confidence, Owner, validation action, and unresolved questions.
