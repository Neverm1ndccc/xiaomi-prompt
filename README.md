# 小米影像 AI 运营工具箱

一个可独立安装到 Codex 的中文运营 Skill，覆盖小米影像内容策划、标题优化、案例拆解、创作者分析、数据复盘、品牌校准、影像知识、用户互动、竞品监测和每周数据回顾。

它直接使用每位用户自己的 Codex 登录与可用额度，不依赖额外模型 API Key。网页工作台保留为可选配套，用于任务记录、状态管理和结果回填；工作台无法访问时不影响 Skill 使用。

## 能力范围

| 模块 | 能力 | 典型交付 |
|---|---|---|
| M1 | 内容策划 | 选题矩阵、主方案、素材与验证计划 |
| M2 | 标题优化 | 多风格标题、首选建议、A/B 设计 |
| M3 | 爆款案例拆解 | 结构、机制假设、迁移边界与实验 |
| M4 | 创作者分析 | 证据化评分、合作策略、背调清单 |
| M5 | 数据复盘 | 指标变化、原因假设、行动项 |
| M6 | 品牌调性校准 | 风险诊断、逐条修改、可发布稿 |
| M7 | 影像知识助手 | 原理、步骤、误区、知识边界 |
| M8 | 用户互动运营 | 多语气回复、风险等级、升级路径 |
| M9 | 竞品监测 | 变化、趋势、机会风险、观察项 |
| M10 | 每周数据回顾 | 周报、Top/Bottom、AI 证据、下周动作 |

## 从私有 GitHub 仓库安装

前提：

- 已安装 Codex。
- 当前设备能够访问本私有仓库。组织仓库需先由管理员授予权限。
- 使用 GitHub CLI 凭据、Git Credential Manager，或设置只读 `GH_TOKEN` / `GITHUB_TOKEN`。不要把令牌写进 README、聊天记录或仓库。

仓库地址：<https://github.com/Neverm1ndccc/xiaomi-prompt>

运行 Codex 内置安装器：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Neverm1ndccc/xiaomi-prompt \
  --path . \
  --name xiaomi-image-ai-operations
```

安装完成后重启 Codex，使新 Skill 出现在可用列表中。

也可以直接告诉 Codex：

```text
请使用 skill-installer，从私有 GitHub 仓库 Neverm1ndccc/xiaomi-prompt 的根目录安装，
Skill 名称为 xiaomi-image-ai-operations。
```

若目标目录已存在，安装器会安全退出而不是覆盖。更新前先通过文件管理器将旧目录
`~/.codex/skills/xiaomi-image-ai-operations` 移到备份位置，再重新运行安装命令。

## 使用

显式调用最稳定：

```text
$xiaomi-image-ai-operations
为秋季影像大赛设计两周内容传播方案，目标是提升有效投稿量。
已有材料：活动规则、三个历史案例和上期数据。请输出选题矩阵、主方案、渠道文案和验证指标。
```

也可以直接描述任务；当内容明确属于 M1–M10 时，Codex 会根据 Skill 描述进行路由。

建议输入至少包含：

- 业务目标、目标人群、平台和时间窗。
- 已确认的事实、素材、数据或品牌规范。
- 资源、版权、合规和禁用表达等约束。
- 期望交付、核心指标、基线和审核人。

详细示例见 [references/examples.md](references/examples.md)，模块方法见 [references/prompts.md](references/prompts.md)。

## 每周数据回顾

M10 同时复盘业务表现和 AI 使用效果，建议固定记录：

- 业务规模、内容效率、内容质量和转化。
- AI 任务量、覆盖模块、采纳率、节省时间、一次通过率和重大错误。
- 新增 Prompt / 模板 / 规则、实际复用次数、分享培训与采纳人数。
- 上周行动完成情况，以及含负责人、截止时间和验收标准的下周动作。

没有真实数据时，Skill 只会提供采集模板，不会生成趋势结论。数据口径与计算规则见 [references/prompts.md](references/prompts.md#M10-每周数据回顾)。

## 可选工作台

配套网页工作台：<https://mi-image-ai-toolkit.wyfdcjh.chatgpt.site/>

推荐流程：

1. 在工作台整理任务，复制“小米影像 AI 工作台任务”。
2. 在 Codex 中调用 `$xiaomi-image-ai-operations` 并粘贴任务。
3. 人工审核事实、品牌、数据、版权和发布风险。
4. 将结果末尾的“工作台回填”块复制回工作台。

工作台与 Skill 权限彼此独立。Skill 不会声称已自动写回网页或数据库。字段协议见 [references/workbench-protocol.md](references/workbench-protocol.md)。

## 安全与治理

- 仓库只保存方法、模板和虚构示例，不保存真实业务数据。
- 不提交手机号、邮箱、账号密码、访问令牌、未发布产品信息和其他敏感内容。
- AI 产出是草稿和决策辅助，不是事实来源；对外发布和经营结论必须人工审核。
- 产品能力、参数、活动规则和竞品事实必须回到可追溯的权威材料。

完整规则见 [references/governance.md](references/governance.md)。

## 本地验证

```bash
python3 tests/validate_skill.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

人工行为验收场景见 [tests/scenarios.md](tests/scenarios.md)。

## 目录结构

```text
.
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── examples.md
│   ├── governance.md
│   ├── prompts.md
│   └── workbench-protocol.md
└── tests/
    ├── scenarios.md
    └── validate_skill.py
```

## 维护建议

- 业务方法更新：修改 `references/prompts.md`。
- 品牌、隐私或数据规则更新：修改 `references/governance.md`。
- 工作台字段变化：同步修改 `references/workbench-protocol.md`。
- 每次更新后运行两项验证，提交清晰的变更说明，再由其他设备重新安装。
