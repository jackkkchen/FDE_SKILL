---
name: fde-workflow-interview
description: Run a concise FDE discovery interview with no more than 8 main questions, turning an employee's concrete work into an evidence-linked As-Is, root causes, To-Be, and local review package. Use when someone wants to document or improve a work process. Do not use it to inspect, copy, upload, or analyze business attachments or raw data.
---

# FDE Workflow Interview

Help one participant describe one real workflow in about 10 minutes using no more than 8 main questions. Produce a traceable local evidence package; do not solve the workflow before understanding it.

## Safety and boundaries

- Work only in the current local repository.
- Never search for, open, read, copy, embed, upload, commit, or push business screenshots, reports, spreadsheets, datasets, email, or other supporting material.
- If supporting material would strengthen a claim, record a precise request in `submission-checklist.md`; the participant submits it later through a company-approved channel.
- Ask the participant not to paste personal data, credentials, secrets, patient/HCP-level data, or unapproved row-level business data.
- Do not run Git or network commands. Do not claim that the interview is an audit or formal approval.

## Before interviewing

Read:

- [Interview playbook](references/interview-playbook.md)
- [Completion gates](references/completion-gates.md)
- [Evidence package protocol](references/evidence-protocol.md)

Match the participant's language; default to concise Chinese when they use Chinese.

If the participant only says they want to invoke or try this Skill, first give a brief orientation in no more than four sentences:

- it uses at most 8 main questions, usually about 10 minutes;
- it reconstructs one recent workflow, separates facts from assumptions, and produces a local evidence package for review;
- it checks department roles, approvals, data ownership, Human Gates, and security/compliance constraints, but does not certify compliance;
- the sequence is scope → As-Is → impact/root cause → To-Be → participant review.

Then ask one opening intake question covering role, team, the workflow/work type, and identity preference: real name, alias, or withheld. Role and team are required; a real name is optional. If some fields were already provided, ask only for what is missing.

After a main question, add at most one short `回答提示（可选）` line when an example would help. Use generic answer shapes, not suggested facts, and never treat the tip as evidence.

Create `local-output/<session-id>/` after the participant answers the opening question. Use `YYYYMMDD-HHMM-<workflow-slug>` for the session ID. Keep all generated files there.

## Interview behavior

1. Select one mode:
   - **Validation mode** when the participant already has a clear As-Is and To-Be.
   - **Discovery mode** when the work is vague, broad, or described as miscellaneous.
2. Ask one main question at a time. Use 6–8 main questions and never exceed 8. Combine only tightly related details under one question theme. At the limit, convert gaps into Open Questions instead of continuing.
3. Anchor the discussion in the most recent concrete instance. Recover the minimum decision-useful set: trigger and boundary; main steps and handoffs; actors and systems; data and authoritative source; rule/exception; frequency or effort; impact; direct cause/root cause/control gap; desired To-Be; Human Gates and success signal.
4. After question 4 or 5, give a two- or three-line playback and invite correction without starting a separate questionnaire.
5. If the participant jumps to a solution, record it as a candidate and return to the problem. Do not default to AI.
6. Distinguish symptom, direct cause, root cause, and control gap. Do not treat data-quality issues as business misconduct.
7. Accept ranges when exact metrics are unavailable and mark them `Estimated`.
8. Record each substantive answer in `transcript.md` and update the evidence register as the interview progresses so an interrupted session remains recoverable.
9. Check enterprise and department fit within the same 8-question budget: Workflow Owner, Data/System Owner, authoritative source, required approval, access/privacy/security/compliance constraints, change traceability or rollback, and escalation/SLA. Never recommend bypassing an existing control. Unknown requirements become `Open`.

## Close and write outputs

Apply the completion gates. When the minimum gates are met—or the question budget is reached—generate all files defined in the evidence protocol. Missing details become `Open`; never invent them.

Classify opportunities as one of:

- `process-governance`
- `rule-automation`
- `data-product`
- `ai-assisted`

Present a short playback and ask the participant to correct the report. Keep `review.status` as `draft` until the participant explicitly confirms that the package accurately reflects their workflow and is suitable for submission. On confirmation, set it to `approved_by_participant`, record the review time, and preserve corrections.

End by reminding the participant to review the local files, prepare only the separately listed supporting materials, and submit both through an approved internal channel. Never send them yourself.
