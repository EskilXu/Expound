# Claude 培训与认证指南

> **本指南面向两类读者**:
> - **企业 / 团队**:希望让组织系统化掌握 Claude,无论是否加入 Anthropic Partner Network
> - **个人**:希望自学 Claude、通过官方认证、把它转化为职业能力的工程师 / 售前 / PM
>
> 如果你只关心 **Partner Network 的端到端流程**(申请→培训→认证→上市→续期),请看 [`partner-journey.md`](./partner-journey.md);本指南更聚焦 **培训配比与备考策略**。
>
> **声明**:本文档基于截至 2026 年 5 月公开可见的 Anthropic 课程结构与认证框架,实际课程目录、考试形式、有效期以官方 Partner Portal / Anthropic Academy 最新说明为准。

---

## 第一部分:企业级培训指南(Enterprise Track)

### 1.1 适用对象

| 组织类型 | 典型动机 | 目标 |
|---|---|---|
| 系统集成商 / 咨询公司 | 加入 Partner Network、获得 NFR 与折扣、做 Claude 实施业务 | 1–3 个月达到 Registered,3–6 个月达到 Select |
| ISV / SaaS | 在产品里集成 Claude,需要内部能力支撑 | 工程团队 80% 完成 Tech Track,1–2 名 Agent Developer |
| 大型企业内部 AI 部门 | 推广内部 Claude 用例、培训跨团队人员 | 建立内部 Center of Excellence,持续输出认证人员 |
| 培训机构 / 高校 | 开 Claude 相关课程或实验班 | 教师全员 Tech Track,学员按 Business / Dev 路径分流 |

### 1.2 角色矩阵与培训配比

不要"全员一起学"。先盘点角色,再按职责分配学习路径。

| 内部角色 | 推荐路径 | 目标认证 | 投入(每人) | 完成时间 |
|---|---|---|---|---|
| 售前 / 解决方案咨询 | Business + Technical | Business Associate + Solutions Architect | ~80h | 6–8 周 |
| 销售 / Alliance | Business | Business Associate | ~30h | 2–3 周 |
| PM / Product | Business + 选学 Tech | Business Associate(Tech 选 1 模块) | ~40h | 3–4 周 |
| 后端 / 应用开发 | Developer / Agent | Agent Developer | ~120h | 8–12 周 |
| Solutions Engineer | Technical + Developer | Solutions Architect + Agent Developer | ~150h | 10–14 周 |
| 数据 / ML 工程 | Technical(深) | Solutions Architect | ~80h | 6–8 周 |
| 法务 / 合规 | Business 中"安全合规"模块 | 不需认证 | ~8h | 1 周 |
| Marketing / Content | Business 速览 | 不需认证 | ~6h | 1 周 |

### 1.3 团队认证目标(参考 Tier 配比)

以 30 人规模的咨询公司、目标 Select tier 为例:

```
        Business Associate × 5 ─────────────────────  覆盖售前 / PM / Alliance
        Solutions Architect × 3 ────────────────────  覆盖 SE / 售前主力
        Agent Developer × 2 ────────────────────────  覆盖核心交付工程师
        + 1 名行业专项(如 Financial / Healthcare)──  支持目标垂直行业
```

冗余度建议:每个关键认证至少 2 人持有,避免单点。

### 1.4 季度运营节奏(参考)

| 季度 | 主题 | 关键产出 |
|---|---|---|
| Q1 | **盘点 + Business 普及** | 全员完成 Business 速览;3–5 人启动 Business Associate |
| Q2 | **Tech 主力培训** | SA / Dev 候选人完成核心 Tech 模块;2 个内部 hackathon |
| Q3 | **认证冲刺** | 模考 + Office Hour 答疑,目标人数完成认证 |
| Q4 | **复盘 + GTM 落地** | 案例白皮书、客户参考、来年学习路线复盘 |

### 1.5 内部能力建设:四个支柱

光"送人考试"不够,企业还需要建立长期内部生态:

1. **Center of Excellence (CoE)**
   一个 2–3 人的小组,负责 prompt library、最佳实践沉淀、新员工 onboarding。每月 demo day。
2. **内部 Prompt / Skill Library**
   把 production-grade 的 prompt、agent skill、Claude Code subagent 沉淀到内部 git 仓库,review 后复用。
3. **每周 "Claude Hour"**
   1 小时内部分享:可以是 Anthropic 官方 release notes 速读、内部踩坑、客户案例。
4. **Anthropic Office Hours 接入**
   Premier / Select 通常每周有 1 小时 Office Hour,排好轮值参与,把问题带回来。

### 1.6 治理与合规要点

| 维度 | 推荐做法 |
|---|---|
| **API key 管理** | 按项目分 key,Production / Staging / 教学 Lab 分离;Lab 设月度预算上限 |
| **HITL 边界** | 对外通讯、签署、生产部署强制人工审批;内部 draft 可放开 |
| **数据合规** | 客户数据进入 prompt 前必经过 PII 脱敏;敏感行业(医疗、金融)走专门 channel |
| **成本治理** | Partner Handbook、稳定 system prompt 一律走 Prompt Caching;月度 review token 消耗 Top 10 用例 |
| **审计** | 每次 agent 调用写 run log;production 有 trace ID 可追溯到 prompt 与模型版本 |
| **模型版本** | 锁定生产用模型 ID(如 `claude-opus-4-7`),升级走 staging 灰度 |

### 1.7 与 Anthropic 官方资源的关系

| 资源 | 用途 | 谁该用 |
|---|---|---|
| Anthropic Academy | 自学课程主入口 | 全员 |
| Partner Portal | 申请、tier 状态、官方课程目录 | Champion / Alliance |
| Solutions Engineer Office Hours | 真实问题答疑 | SA / Dev 主力 |
| Anthropic Cookbook(GitHub) | 代码示例 | Dev / SE |
| Claude Docs(docs.claude.com) | API、工具、Skills 参考 | 全员开发相关 |
| Anthropic Blog / Release Notes | 产品更新 | CoE 每周扫描 |

### 1.8 与 Expound 的关系

`partner-journey.md` 描述的是"端到端的 6–8 周流程",Expound 把它自动化。本指南补充的是 **"长期培训配比 + 内部生态"**,Expound 的角色:

- Eligibility Scout 给出**当前角色矩阵 vs 目标 tier**的 gap 报告
- Training Coach 把本指南的"角色 → 学习路径"映射到具体周计划
- Certification Prep 处理备考(详见第二部分 2.4)
- Compliance & Renewal 在认证到期前 45 天触发 Delta 学习

### 1.9 三个企业实战案例

#### 案例 A:BlueRiver Consulting — 30 人精品咨询从 0 到 Select tier

**背景**:30 人战略咨询,只有 1 位合伙人对 Claude 有兴趣,其余团队完全没用过。

**6 个月节奏**:
- M1–M2:全员 Business 速览(每周 1 次午餐分享),5 人启动 BA
- M3–M4:5 人完成 BA;3 人选定 SA 路径,1 人开始 Agent Dev
- M5:Anthropic 申请 + Lab 实战 + 模考冲刺
- M6:3 SA + 1 Agent Dev 通过,Partner Directory 上架

**结果**:6 个月达 Select,签下 2 单 Claude 实施项目,合计 80 万元。

**关键决策**:Q1 不急着考证,先让所有人理解"我们卖什么"。Champion 投入 30% 时间做内部推动。

#### 案例 B:NorthPole AI — 200 人 SaaS 不走 Partner,但建内部 CoE

**背景**:产品里要集成 Claude,8 人 AI 团队 + 60 人其他工程师。

**路径**:
- 8 名 AI 工程师全员考 Agent Developer(用了 4 个月)
- 通过后每人带 5 名"小弟",每周 1-on-1 + 月度 demo day
- 不申请 Partner Network,业务模型不需要

**治理**:Lab key 月度 2000 USD 上限;production key 由 CoE 集中管,所有 prompt review 后入仓。

**结果**:6 个月内 40% 工程师能独立交付 Claude 集成,产品 NPS 上升 12 分。

**踩的坑**:第一批"小弟"中有 3 人只看视频不动手,3 个月没长进。后来强制每月交 1 个 PR。

#### 案例 C:GlobalBank EMEA — 合规优先的内部部署

**背景**:大型银行,数据不出 SaaS,Claude 走 Bedrock 部署;只对内部 50 名工程师培训,不对外。

**路径**:
- 全员 Business 普及(8h),理解能干什么、不能干什么
- 25 人 Solutions Architect 培训(其中 10 人通过认证)
- 10 人 Agent Developer 进阶(5 人通过)

**治理**:每个 prompt 经 PII 脱敏流水线;模型版本锁 `claude-opus-4-7`,升级走 6 周灰度;审计日志保留 7 年。

**结果**:4 个 production agent 上线(KYC 辅助、合规问答、报告草稿、知识检索),月 token 1500 USD,Caching 命中率 92%。

---

## 第二部分:个人级培训指南(Individual Track)

### 2.1 自我定位:你属于哪一类?

| 你目前是 / 想成为 | 推荐主路径 | 目标认证 |
|---|---|---|
| 售前 / 销售 / PM / 行业顾问 | Business Track | Claude Business Associate |
| 解决方案架构师 / 资深前端 / Tech 售前 | Technical Track | Claude Solutions Architect |
| 后端 / Agent / 应用开发工程师 | Developer / Agent Track | Claude Agent Developer |
| 想全面发展(独立咨询、自由职业) | Business + Technical(分两阶段) | BA → SA |
| 学生 / 完全新手 | Business 入门,再决定 | Business Associate |

**判断方式**:看你日常 80% 时间在做什么。如果你写代码,选 Developer;如果你做方案设计,选 Technical;如果你跟客户谈需求,选 Business。

### 2.2 三种学习方式的取舍

| 方式 | 优点 | 缺点 | 适合 |
|---|---|---|---|
| 纯自学(Academy + 文档) | 免费 / 灵活 | 无人答疑、容易半途放弃 | 自驱强、有项目带动的人 |
| 自学 + Office Hours | 关键问题有人答 | 需要排到合适时段 | 大多数 SA / Dev 候选 |
| 加入企业 / Partner 培训 | 有同伴、有进度推动 | 受限于公司节奏 | 已在 Partner Org 工作 |
| 报付费训练营 / Bootcamp | 节奏紧、密度高 | 成本高、质量参差 | 想 4–6 周快速上岗的人 |

### 2.3 推荐学习时间投入(参考)

> 都按"业余时间学"估算,每周 5–8 小时。全职可压缩 60%。

| 目标认证 | 总时长 | 周数(业余) | 备注 |
|---|---|---|---|
| Business Associate | 30–40h | 4–5 周 | 有销售 / 商务背景的人可压缩到 3 周 |
| Solutions Architect | 80–120h | 10–14 周 | Lab 部分可能反复迭代 |
| Agent Developer | 120–180h | 14–20 周 | 需要至少完成 1 个端到端 agent 项目 |

### 2.4 三个认证的备考策略

#### 2.4.1 Claude Business Associate

**考试形式**:60 题选择 + 2 个场景题,在线监考。通过 75%。

**备考节奏**:
- 第 1–2 周:Anthropic Academy 的 Business 模块全过一遍
- 第 3 周:做官方 sample 题 + 速读 1 份案例研究
- 第 4 周:模拟 2 套全真模考,错题集中过

**易错点 Top 3**:
1. **价值主张表述**:Claude 不是"另一个 LLM",而是强调安全、长上下文、Agentic;答题时要从"客户场景 → Claude 的差异化价值"切入。
2. **定价 & packaging**:常考 Tier、Tokens、Caching 折扣,熟记官方文档表格。
3. **合规边界**:HIPAA、FedRAMP 之类的"什么场景下推荐什么部署形态"需要背基本框架。

#### 2.4.2 Claude Solutions Architect

**考试形式**:40 题选择 + 1 个 Lab(设计一个 Claude 解决方案)。通过 80% + Lab 评分通过。

**备考节奏**:
- 第 1–3 周:Messages API、Prompt Engineering、Tool Use(动手敲代码,不要只看)
- 第 4–6 周:Agent SDK、Memory、Compaction(做 1 个小 agent demo)
- 第 7–8 周:Prompt Caching、Extended Thinking、Evals
- 第 9–10 周:挑 2 个真实客户场景,自己做方案设计草稿
- 第 11–12 周:模考 + Lab 实战(限时 4 小时设计一个解决方案)

**Lab 通过的关键**:
- 不要堆功能,先讲清 **业务问题 + 评判标准**
- 必须包含:架构图、prompt 设计要点、HITL 边界、成本估算、风险与缓解
- 给出 evaluation 设计(如何衡量这套方案做得好不好)

**易错点 Top 3**:
1. **Tool Use 错误处理**:tool 调用失败、超时、返回格式错的处理,常见考点。
2. **长程 agent 的状态管理**:何时用 Memory tool、何时用结构化 state、何时压缩,这是评分重点。
3. **成本与延迟权衡**:Caching 命中率、Haiku vs Sonnet vs Opus 的选择,要能给数字。

#### 2.4.3 Claude Agent Developer

**考试形式**:实操 Lab,用 Agent SDK 构建一个指定 agent 并通过测试集。通过率 ≥ 85%。

**备考节奏**:
- 第 1–4 周:Agent SDK 基础,跟着官方 quickstart 全部跑通
- 第 5–8 周:深入 subagent、MCP、Skills、Hooks 这些高级特性
- 第 9–12 周:做 2 个端到端项目(选一个偏 coding agent,一个偏业务 agent)
- 第 13–16 周:模考 + 把项目重构到 production 级(写 evals、错误处理、observability)

**Lab 通过的关键**:
- 项目结构清晰,有 README、有 evals
- 错误处理覆盖率高(tool 失败、模型 timeout、context overflow)
- 有 observability(每次 agent 调用写日志)
- 有 cost awareness(用 Caching、合理的模型分层)

**易错点 Top 3**:
1. **Context 管理**:不会用 compaction、Memory、subagent 隔离上下文,很容易超限。
2. **Tool 设计**:tool description 写得不清,导致 agent 频繁误调用。
3. **Eval 设计**:没有 evals 直接上 production,几乎一定挂。

### 2.5 实战项目建议

考试只能验证基础能力。要真正能用,推荐做 1–2 个端到端项目:

| 难度 | 项目 | 学到 |
|---|---|---|
| ★ | 个人 PDF 问答 agent | Messages API、tool use 基础 |
| ★★ | 邮箱自动分类 + 草稿回复 agent | Tool use、外部 API 集成、HITL |
| ★★ | Slack 内部知识问答 bot | RAG、prompt caching、长上下文 |
| ★★★ | 代码 review 助手(GitHub Action) | Agent SDK、subagent、structured output |
| ★★★ | 多步骤研究 agent(像 Deep Research) | Subagent 编排、long-horizon、context engineering |
| ★★★★ | 你所在行业的垂直 agent(法律 / 医疗 / 财务) | 真实数据、合规、HITL 设计 |

挑一个能持续 4–8 周的项目,完成后开源 / 发博客,对求职和咨询机会都很有帮助。

### 2.6 常见误区与避坑

| 误区 | 后果 | 正确做法 |
|---|---|---|
| 跳过 Business 直接学 Tech | 不理解客户场景,设计不出好方案 | 至少花 1 周扫一遍 Business 模块 |
| 看视频不动手 | 考 Lab 直接挂 | 每个视频都要配 1 个动手练习 |
| 只学最新模型,不学基本面 | 模型一更新就废了 | Messages API、Prompt 设计这些基础永不过时 |
| 一次性想考三个证 | 战线拉太长,容易放弃 | 先 BA(快速胜利),再 SA / Dev(长期投入) |
| 忽略 evals | 项目"看起来能跑"但 production 一上就爆 | 每个 agent 都要有自己的 eval set |
| 一个人闷头学 | 容易卡死、动力不足 | 找 1–2 个学伴,每周 review 一次进度 |
| 不算成本 | 学习期 API bill 爆掉 | Lab 用 Haiku、上 Caching;月度看消耗 |

### 2.7 没通过怎么办?

第一次没过非常常见,不要灰心。建议:

1. 拿到错题报告(认证体系会给薄弱领域反馈)
2. 针对薄弱点专题补强 1–2 周(不要重学整个课程)
3. 模考 2 套,准备度评分 ≥ 85 再约下次
4. Solutions Architect 和 Agent Developer 的 Lab 不通过,通常是"工程实践不足",建议先做 1 个真实项目再考

### 2.8 通过认证之后

认证只是起点。建议接下来:

| 路径 | 怎么做 |
|---|---|
| 技术深耕 | 持续跟 Anthropic release notes,每个新特性写一篇拆解;贡献 Cookbook |
| 求职 / 跳槽 | 把项目放 GitHub + 写技术博客;关注 Partner Network 招聘 |
| 独立咨询 | 在 LinkedIn / X 持续输出案例;接小型 PoC 项目积累口碑 |
| 内部 Champion | 主动牵头公司里的 CoE 或 Claude Hour |
| 社区贡献 | Anthropic Discord、MCP 生态、开源 agent 项目 |

### 2.9 持续学习节奏

模型和工具迭代很快。建议把"学习"做成日常:

- **每周**:30 分钟扫 Anthropic Blog + Release Notes
- **每月**:1 个新特性的动手 demo(如新 Skills、新 MCP server)
- **每季**:1 个完整项目 / 一篇深度技术文章
- **认证到期前 45 天**:Delta 学习路径(只看过去 12 个月的变更)

### 2.10 三个个人成长案例

#### 案例 A:张涛 — 8 年 Java 后端 → Agent Developer

**起点**:对 LLM 一窍不通,公司也没用 Claude。完全靠业余时间。

**路径(8 个月)**:
- M1:Business 速读,搞清楚 Claude 能做什么
- M2–M3:Messages API + Tool Use,跟着官方 cookbook 全部敲一遍
- M4–M7:做 2 个开源 GitHub 项目(代码 review bot + 邮箱 agent),反复迭代
- M8:Lab 模考 + Agent Developer 认证

**踩的坑**:第 4 个月一上来就用 subagent + Memory,token 爆掉。回头补 context engineering 基础。

**结果**:跳槽到 AI 创业公司,涨薪 40%。两个开源项目共 800+ stars。

#### 案例 B:林佳 — PM 5 年 → Solutions Engineer

**起点**:无代码经验,目标公司要求 BA + SA 双认证。

**路径(5 个月)**:
- 并行 BA(每周 6h)+ SA(每周 6h)
- M3 报了一个 2 周动手 Bootcamp,把代码恐惧打掉
- M4 BA 通过;SA 第一次 Lab 没过(架构图缺成本估算)
- M5 针对错题专题补强,SA 二刷通过

**结果**:进入 Partner SE 团队,初期跟一位资深 SA 配对工作。

**反思**:不要因为是 PM 就跳过 Lab,Lab 是真正的差异化。

#### 案例 C:王雅 — 资深企业咨询 → 独立顾问加 Claude 服务

**起点**:5 年企业咨询经验,客户主要在金融与零售,想加 AI 服务条线。

**路径(3 个月,全职)**:
- M1:BA 全套(15 天通过)
- M2:SA 全套,中途接了一个客户 PoC 作为 Lab 实战
- M3:Agent Dev 入门,做了 1 个 demo(没考证)

**结果**:LinkedIn 更新认证后 1 个月内接到 3 个 PoC 询单;4 个月后第一个 30 万元订单落地。

**关键洞察**:认证 + 真实案例缺一不可。光有证没有 demo,客户不下单。

---

## 第三部分:个人 ↔ 企业 协同

### 3.1 个人在企业内做 Champion

如果你是个人贡献者,但公司想推 Claude,你可以主动承担"内部 Champion"角色:

- 帮 HR / Manager 设计角色矩阵(参考 1.2)
- 牵头每周 Claude Hour
- 维护内部 Prompt / Skill Library
- 与 Anthropic Partner Account Manager 对接

这通常会成为内部晋升的重要资本。

### 3.2 企业如何识别和支持有潜力的个人

| 信号 | 含义 |
|---|---|
| 主动问 API 问题、提 issue | 有钻研意愿 |
| 课外做 side project | 工程能力足 |
| 能给非技术同事讲清 Claude | 既懂技术也懂业务,稀缺 |
| 持续追 release notes | 长期投入信号强 |

建议给这些人:Lab 预算、Office Hour 优先权、参加行业会议的机会、以及把他们送进 SA / Agent Dev 认证。

### 3.3 三个个人 ↔ 企业协同案例

#### 案例 A:李工(NorthPole AI 内部 Champion → Tech Lead)

最初只是普通工程师,主动牵头公司"Claude Hour"。1 年内:
- 帮公司从无 Partner 关系到 Registered
- 自己升 Tech Lead,薪资上涨 35%
- 把内部 Prompt Library 开源,获得行业关注

**启示**:当公司还没明确方向时,愿意主动补位的人会被看见。

#### 案例 B:陈博士(企业出资考证 → 创业 → 反向合作)

在某跨国 SaaS 公司被资助考完 BA + SA + Agent Dev。1 年后离职创业,开了一家 5 人 AI 咨询。
- 前东家成为他第一个客户(他们正缺这种服务)
- 他成为前东家的 Sub-Partner,共享 referral
- 双方在 Partner Directory 互相引用,做联合 GTM

**启示**:企业培训人才"流失"未必是损失,可能转化为长期生态资产。

#### 案例 C:周亮(开源贡献者 → 多家 Partner 招手)

业余在 MCP 生态贡献了 3 个开源 server(GitHub、Notion、内部 wiki 集成)。
- 项目 1500+ stars,被 Anthropic 官方 awesome list 收录
- 3 家 Partner Org 主动联系合作
- 最终选择一家以 contractor + 期权方式加入,保留独立性

**启示**:在新生态(MCP / Skills / Subagents)持续贡献,是个人对企业的天然连接器。

---

## 附录

### A. 认证速查表

| 认证 | 形式 | 通过 | 有效期 | 推荐投入 |
|---|---|---|---|---|
| Business Associate | 60 选择 + 2 场景 | 75% | 12 个月 | 30–40h |
| Solutions Architect | 40 选择 + Lab | 80% + Lab | 12 个月 | 80–120h |
| Agent Developer | 实操 Lab | 测试集 ≥ 85% | 12 个月 | 120–180h |

### B. 学习资源清单(英文为主)

- Anthropic Academy — 主入口
- docs.claude.com — API / 工具 / Skills 参考
- Anthropic Cookbook(GitHub)— 代码示例
- Anthropic Blog / Release Notes — 产品更新
- Claude Code 文档 — 如果做 coding agent 必看
- MCP 协议文档(modelcontextprotocol.io)— Agent 生态扩展

### C. 推荐的"30 天最小可行学习计划"(个人,Tech Track)

| 天 | 目标 | 输出 |
|---|---|---|
| D1–D3 | 跑通 Messages API quickstart | 一个能对话的脚本 |
| D4–D7 | 学 Prompt Engineering | 给一个真实任务写 3 版 prompt 对比效果 |
| D8–D14 | Tool Use 深潜 | 一个能调外部 API 的小 agent |
| D15–D21 | Agent SDK + Memory | 一个跨多轮的研究 / 整理 agent |
| D22–D26 | Prompt Caching + Evals | 把上面那个 agent 加上 caching 和 evals |
| D27–D30 | 复盘 + 模考 1 套 | 准备度自评,决定下个月节奏 |

### D. 与 Expound 的对接

如果你的公司在用 Expound:
- 个人学习进度会自动同步到 Training Coach 看板
- 模考成绩进入 Certification Prep 评分
- 企业级看板能看到"团队整体准备度"

如果你是独立学习者:
- Expound 的开源代码本身就是一个 multi-agent 案例,推荐通读 `src/expound/`
- preview 页面(`preview/index.html`)是一个不错的"agentic 服务长什么样"的视觉参考

---

## 下一步

- 想看端到端 Partner 流程,跳到 [`partner-journey.md`](./partner-journey.md)
- 想看代码,跳到 [`../src/expound/`](../src/expound/)
- 想跑 demo,看 [`../README.md`](../README.md)
