# Validation Scenarios

All fixtures are synthetic and contain no company-specific information.

## Repository checks

Run:

```bash
python3 tests/validate_repository.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .github/skills/fde-workflow-interview
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .github/skills/fde-workflow-prioritization
```

The exact `quick_validate.py` path may differ outside Codex; VS Code discovery remains the runtime test.

## Manual interview scenarios

1. Participant already has a clear As-Is and To-Be: Skill should select Validation mode.
2. Participant says “my work is miscellaneous”: Skill should select one recent case and use Discovery mode.
3. Participant withholds their name: package should remain valid when role and team are present.
4. Participant has no precise metrics: retain ranges as `Estimated`.
5. Participant proposes an AI solution immediately: park it and return to the workflow and root cause.
6. Participant provides sensitive detail: stop collecting it and add a generalized material request.
7. Question budget is reached: produce a draft and convert gaps into Open Questions.
8. Participant says only “我要调用这个 Skill”: explain the purpose and short flow first, then ask one opening intake question.
9. Every completed short interview uses no more than 8 main questions; optional answer tips stay brief and do not become evidence.
10. Department controls are unknown: record Owner, authoritative source, approval, access/security/compliance, rollback, and SLA gaps as Open rather than guessing.

## Manual prioritization scenarios

- `approved-a` and `approved-b` describe similar work but disagree on the responsible Owner; retain the conflict.
- `draft` must be skipped because participant review is incomplete.
- `malformed` must be skipped because required structure is missing.
- A deterministic workflow with AI Fit ≤ 2 must become `Improve without AI` even when valuable.
- An unmitigated High Risk workflow must not become `Now`.

Before publishing, open the repository in VS Code Agent Mode and confirm `/fde-workflow-interview` and `/fde-workflow-prioritization` are discoverable.
