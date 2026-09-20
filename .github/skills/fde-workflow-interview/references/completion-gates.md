# Completion Gates

Stop when the information supports the next decision; do not wait until every detail is known.

## Minimum As-Is gate

- One bounded workflow has a name, trigger, start, end, input, and output.
- At least one recent concrete case supports the description.
- Main steps, actors, handoffs, systems, and data sources are recorded.
- At least one business rule or decision point is identified.
- The normal path and at least one exception or failure path are captured.
- The downstream user and business decision are known.

## Value gate

- The pain is more specific than “low efficiency.”
- Symptom, direct cause, root cause, and control gap are separated where evidence allows.
- At least two of frequency, volume, handling time, waiting time, rework, error rate, or business impact are reported or estimated.
- The current workaround and consequence of doing nothing are documented.

## To-Be gate

- The desired business outcome is clear without relying on a named technology.
- Earlier detection/handling point, responsible role, and needed information are described.
- Automatable steps and Human Gates are distinguished.
- A measurable or observable success signal exists.

## Enterprise and department fit gate

- Workflow Owner and Data/System Owner are identified or explicitly `Open`.
- The authoritative data source or business-rule owner is identified or explicitly `Open`.
- Required approval and Human Gates are preserved.
- Relevant access, privacy, security, compliance, change-traceability/rollback, and escalation/SLA constraints are captured or explicitly `Open`.
- The output does not claim formal compliance or recommend bypassing an existing control.

## Handoff gate

- Open Questions and requested supporting materials are listed.
- Participant reviewed the playback; package remains `draft` until explicit approval.

## Stop behavior

If the 8-question limit is reached before all gates pass:

1. Generate a draft package.
2. State which gates are incomplete.
3. Convert each missing item into a precise Open Question or material request.
4. Do not extend the interview unless the participant explicitly asks to continue.

If the participant asks to continue, finish the short package first and offer a separately labeled follow-up session; never add a ninth main question to the same interview.
