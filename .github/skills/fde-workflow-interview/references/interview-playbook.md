# Interview Playbook

## Mode selection

Use **Validation mode** when the participant can already name the workflow, its start and end, current problem, desired outcome, and Owner. Verify rather than rediscover.

Use **Discovery mode** when they describe a broad role, miscellaneous requests, or an unclear process. Ask for the most recent concrete instance and follow that case from trigger to business outcome.

## Question budget

Treat 15–20 minutes as a target, not a guarantee. Use this sequence as a budget, not a questionnaire:

1. Scope and recent case: 2 questions.
2. As-Is steps, actors, systems, data, rules, exceptions: 4–5 questions.
3. Frequency, effort, waiting, rework, impact, and root cause: 2–3 questions.
4. Desired outcome, Human Gates, constraints, and success signal: 2 questions.
5. Playback and participant review: 1 closing exchange.

Ask only the next question that most reduces uncertainty. Do not bundle several unrelated questions.

## High-value prompts

### Scope and case

- 你最近一个月主要负责哪几类工作？我们今天先选哪一件具体工作讲清楚？
- 最近一次实际发生是什么时候？从谁提出什么需求开始？

### Workflow reconstruction

- 你收到输入后第一步做什么？接下来交给谁或进入哪个系统？
- 哪一步需要判断，而不是机械执行？你依据什么判断？
- 正常情况怎么走？最近一次异常或返工是怎么发生的？

### Data and systems

- 这一步用到哪些系统、表、文件或字段？哪个来源被认为是权威来源？
- 数据不完整、口径不一致或无法匹配时，现在怎么处理？

### Handoffs and ownership

- 哪些问题由你确认，哪些必须由业务、数据 Owner 或审批人确认？
- 等不到回复时流程会怎样？谁有最终决定权？

### Baseline and impact

- 这件事多久发生一次？一批多少？操作时间和等待时间分别大约多少？
- 不解决会影响谁、哪张报表、哪个截止时间或什么业务决策？

### To-Be

- 如果先不考虑具体技术，你希望问题在哪个节点被发现或处理？
- 哪些步骤可自动执行，哪些必须保留人工确认？怎样算改善成功？

## Recovery moves

- **Vague answer:** ask for the latest real occurrence.
- **Solution-first answer:** park the solution and ask what happened before the proposed tool was needed.
- **No metric:** request a range from the last three occurrences and mark it `Estimated`.
- **Contradiction:** state both versions neutrally, create a `Contradicted` evidence item, and ask what source or Owner can resolve it.
- **Too broad:** split by trigger/output and select one workflow.
- **Sensitive detail:** stop the detail, retain only a generalized description, and add a material request instead.

## Opportunity classification

Classify only after As-Is and root causes are clear:

| Pattern | Default classification |
|---|---|
| Owner unclear, waiting, missing escalation | process-governance |
| Stable calculation or deterministic rule | rule-automation |
| Missing semantic layer, catalog, trusted view | data-product |
| Unstructured text, fuzzy matching, explanation, knowledge reuse | ai-assisted |

High-stakes decisions remain Human Gates even when AI assists.
