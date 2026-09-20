# FDE Workflow Discovery Skills

一套面向 GitHub Copilot Agent Mode 的自助式 FDE Workflow Discovery 工具。

- `fde-workflow-interview`：员工用不超过 8 个主问题、通常约 10 分钟梳理一条真实工作流，生成 As-Is、痛点/根因、To-Be 和可追溯证据包。
- `fde-workflow-prioritization`：FDE Lead 汇总员工已审阅的证据包，生成价值 × 可行性矩阵和领导讨论材料。

This repository contains two GitHub Copilot Agent Skills for structured workflow discovery and evidence-based prioritization.

## 使用前提

- VS Code 已安装并登录 GitHub Copilot；
- 使用 Copilot Chat 的 **Agent Mode**；
- 公司政策允许在当前 Copilot 环境中讨论相应工作内容；
- 不粘贴患者、HCP、员工个人敏感信息、账号口令、密钥或未经批准的明细业务数据。

VS Code 会从仓库的 `.github/skills/` 发现项目级 Agent Skills。参见 [VS Code Agent Skills 官方文档](https://code.visualstudio.com/docs/agent-customization/agent-skills)。

## 安装与调用

```bash
git clone https://github.com/jackkkchen/FDE_SKILL.git
cd FDE_SKILL
code .
```

在 VS Code Copilot Chat 中切换到 Agent Mode：

1. 输入 `/fde-workflow-interview`，开始个人 Workflow 访谈；
2. 完成后审阅 `local-output/<session-id>/` 中的文件；
3. 只通过公司批准的渠道，将审阅后的证据包和另外准备的证明材料提交给 FDE Lead；
4. FDE Lead 将已审阅证据包放入本地 `employee-submissions/`；
5. 输入 `/fde-workflow-prioritization` 生成组合分析。

如果 slash command 没有出现，打开 Copilot 的 Skills/Customizations 配置，确认当前工作区已启用 Agent Skills，并重新加载 VS Code 窗口。

第一次只输入“我要调用这个 Skill”也可以。Skill 会先简要说明用途、8 问以内的流程和材料边界，再询问岗位、团队、待梳理工作及姓名偏好；每个问题可附一行很短的可选回答提示。

## 本地输出

以下目录已被 Git 忽略，不会出现在普通提交中：

```text
local-output/          员工访谈证据包
employee-submissions/ FDE Lead 手工收到的已审阅证据包
local-portfolio/       汇总与优先级结果
```

提交或推送前仍应运行 `git status`，确认没有业务内容进入版本控制。不要使用 `git add -f` 强制添加上述目录。

## 证据和材料边界

- Skill 记录问答过程、结论及 Evidence ID。
- Skill 不搜索业务文件夹，不读取或复制截图、报表和数据文件，不自动上传任何内容。
- Skill 只列出为了验证结论建议后续提交的材料名称、用途、Owner 和敏感性提示。
- 员工必须审阅并确认结果；未确认的 `draft` 证据包不会进入正式汇总。
- 支撑材料应按公司规定另行保存和提交，不应提交到本公开仓库。

## 设计原则

1. 从最近一件真实工作开始，不从抽象岗位描述开始。
2. 先还原问题，再讨论 AI。
3. 区分事实、估算、假设、待确认和冲突。
4. 结论必须引用 Evidence ID。
5. 默认约 10 分钟且不超过 8 个主问题；信息不足进入 Open Questions，不追加第 9 问。
6. 访谈检查部门 Owner、权威数据源、审批、Human Gate、权限、安全/合规、变更留痕和异常升级，但不宣称完成正式合规认证。
7. 优先级结果是讨论输入，不替代业务、Security、Compliance 或管理层决策。

## Repository contents

```text
.github/skills/fde-workflow-interview/
.github/skills/fde-workflow-prioritization/
tests/fixtures/                         synthetic test data only
```

## License

[MIT](LICENSE)
