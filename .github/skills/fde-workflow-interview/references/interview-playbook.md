# Interview Playbook

## Mode selection

Use **Validation mode** when the participant can already name the workflow, its start and end, current problem, desired outcome, and Owner. Verify rather than rediscover.

Use **Discovery mode** when they describe a broad role, miscellaneous requests, or an unclear process. Ask for the most recent concrete instance and follow that case from trigger to business outcome.

## Question budget

Target about 10 minutes. Use 6–8 main questions and never exceed 8. The sequence below is an adaptive coverage map, not a fixed questionnaire:

1. Opening scope and recent case: 1–2 questions.
2. As-Is steps, actors, handoffs, systems, data, rule, and exception: 2–3 questions.
3. Frequency/effort, impact, and cause: 1–2 questions.
4. To-Be, enterprise controls, Human Gates, and success signal: 1–2 questions.
5. Playback and participant review: a closing exchange, not another discovery round.

Ask only the next question that most reduces uncertainty. Bundle only tightly related details under one theme. At question 8, stop and write unresolved items as `Open`.

## Invocation-only opening

When the participant says only “我要调用这个 Skill” or equivalent, give a compact overview before collecting details. A suitable shape is:

> 这个 Skill 会用不超过 8 个主问题、通常约 10 分钟，基于最近一个真实案例梳理 As-Is、问题原因和 To-Be，并生成一套本地证据包供你审阅。过程中会核对 Owner、审批、数据来源和合规边界，但不会读取或上传业务附件。接下来依次确认范围、还原流程、量化影响、设计 To-Be，最后由你确认结果。

Then ask for `岗位｜团队｜想梳理的工作｜姓名偏好（实名/别名/不填写）` in one opening question.

## Short answer tips

When useful, place one brief line immediately after the question:

`回答提示（可选）：可以按“谁提出 → 你做什么 → 交给谁”回答。`

Keep tips generic, optional, and shorter than the question. Do not introduce an answer, business fact, solution, or additional sub-question through a tip.

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

### Enterprise and department fit

- 这条流程由谁负责，哪些数据源或口径是权威的，哪些步骤必须审批或留痕？
- 有哪些权限、隐私、安全、合规、变更回滚或时限要求？不知道的可以直接说不知道。

## Recovery moves

- **Vague answer:** ask for the latest real occurrence.
- **Solution-first answer:** park the solution and ask what happened before the proposed tool was needed.
- **No metric:** request a range from the last three occurrences and mark it `Estimated`.
- **Contradiction:** state both versions neutrally, create a `Contradicted` evidence item, and ask what source or Owner can resolve it.
- **Too broad:** split by trigger/output and select one workflow.
- **Sensitive detail:** stop the detail, retain only a generalized description, and add a material request instead.
- **Question limit reached:** generate the draft, list incomplete gates, and do not ask a ninth main question.

## Opportunity classification

Classify only after As-Is and root causes are clear:

| Pattern | Default classification |
|---|---|
| Owner unclear, waiting, missing escalation | process-governance |
| Stable calculation or deterministic rule | rule-automation |
| Missing semantic layer, catalog, trusted view | data-product |
| Unstructured text, fuzzy matching, explanation, knowledge reuse | ai-assisted |

High-stakes decisions remain Human Gates even when AI assists.
