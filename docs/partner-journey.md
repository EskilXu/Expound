# Anthropic Partner Network — 培训与认证旅程总体说明

> **范围**:本文档描述一家希望加入 Anthropic Partner Network 的企业(系统集成商、咨询公司、ISV、Reseller),从零到成为"认证合作伙伴"并持续运营所需经历的完整旅程。**Expound** 的 agentic 服务围绕这条旅程来编排、辅助和加速每一步。
>
> **声明**:本文档给出的是**参考旅程模型**。实际的 tier 名称、课程目录、认证科目以 Anthropic 官方 Partner Portal 的最新说明为准。Expound 的 Eligibility Scout agent 会在运行时从官方页面拉取最新要求并覆盖本地知识。

---

## 一、旅程全景(5 个阶段)

```
     ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
 ──▶ │ 1.发现   │──▶│ 2. 启用  │──▶│ 3. 认证  │──▶│ 4. 上市  │──▶│ 5. 成长  │
     │ Discover │   │ Enable   │   │ Certify  │   │ Launch   │   │  Grow    │
     └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
       ~1 周           2–3 周          2 周            2 周          持续
```

| 阶段 | 时长(参考) | 关键产物 | Expound 主责 agent |
|---|---|---|---|
| **1. Discover** 发现 & 申请 | 3–7 天 | 差距报告、Business Plan、Tier 目标、已签署 MSA | Eligibility Scout + Application Packager |
| **2. Enable** 启用 & 培训 | 2–3 周 | 团队学习路径、完成率 ≥ 90%、讲师直播回放 | Training Coach |
| **3. Certify** 认证 | 1–2 周 | 至少 N 名已认证的 Solutions Architect / Business Associate | Certification Proctor-Prep |
| **4. Launch** 上市 & 联合 GTM | 2 周 | Demo/POC 脚手架、案例白皮书、Partner Directory 上架 | Enablement / GTM Agent |
| **5. Grow** 成长与续期 | 持续 | 季度业务回顾(QBR)、Tier 升级、年度再认证 | Compliance & Renewal(轻量守护进程) |

---

## 二、合作伙伴层级(参考三层模型)

实际命名以 Anthropic 官方为准。本文以通用三层为例:

| Tier | 画像 | 典型门槛 | 权益 |
|---|---|---|---|
| **Registered** | 初入门、尚未产生收入 | 1 名 Business Associate 认证 | 技术文档、社区、Dev 信用额度 |
| **Select** | 已有 Claude 落地案例 | 2+ Solutions Architect + 已成交 2 单 | 折扣、联合营销预算、NFR 账号 |
| **Premier** | 战略级合作、行业标杆 | 年收入阈值 + 专属行业认证 + 客户参考 | 专属 PAM、Co-sell、EBC 通道 |

Eligibility Scout 会读取企业画像,给出 **"当前满足 Registered,距离 Select 差 2 个认证 + 1 个参考案例"** 这样的差距报告。

---

## 三、培训矩阵(Curriculum)

Expound 按**角色**映射课程,每位学员得到个性化学习路径,而不是"一个大纲塞给所有人"。

### 3.1 三类核心学习路径

| 路径 | 目标角色 | 课程模块(示例) | 目标认证 |
|---|---|---|---|
| **Business Track** | 售前、销售、PM、Alliance | Claude 价值主张、定价 & packaging、安全与合规常识、竞品对比、发现式销售、案例研读 | Claude Business Associate |
| **Technical Track** | Solutions Architect、技术售前 | Messages API 基础、Prompt Engineering、Tool Use、Agent SDK、Evals、Prompt Caching、Extended Thinking | Claude Solutions Architect |
| **Developer / Agent Track** | 应用开发工程师 | Claude Agent SDK 深潜、Managed Agents、MCP、Memory、Compaction、Skills、长程 Agent 设计模式 | Claude Agent Developer |

### 3.2 可选的行业专项(Specializations)

- Financial Services(合规、KYC、RAG on filings)
- Healthcare & Life Sciences(HIPAA、去标识化)
- Public Sector(FedRAMP、数据主权)
- Software & Code(Coding agents、review、migration)

达成 Premier 通常需要 1–2 个行业专项。

### 3.3 交付形态

- **自学**:视频 + 动手实验(Academy)
- **直播**:每月 cohort 直播 + 答疑
- **Lab**:真实沙盒项目(例如"为 ACME 银行构建合规问答 Agent")
- **Office Hours**:Anthropic Solutions Engineer 每周一小时开放答疑

Training Coach 负责把这些异构资源排进每个学员的周计划,并每周推进度 + 提醒逾期。

---

## 四、认证(Certification)

### 4.1 科目与形式

| 认证 | 考试形式 | 通过标准(参考) | 有效期 |
|---|---|---|---|
| **Claude Business Associate** | 60 题选择题 + 2 个场景题,在线监考 | 75% | 12 个月 |
| **Claude Solutions Architect** | 40 题选择题 + 1 个实操 Lab(设计一个 Claude 解决方案) | 80% + Lab 评分通过 | 12 个月 |
| **Claude Agent Developer** | 动手实操 Lab:用 Agent SDK 构建一个指定 Agent 并通过测试集 | 测试集通过率 ≥ 85% | 12 个月 |

### 4.2 备考流程(Proctor-Prep Agent)

1. **诊断测验**:学完课程后自动出 20 题,定位薄弱点
2. **薄弱点专题**:针对弱项生成讲解 + 追加题目
3. **3 轮模考**:每轮后 Claude 出详细错题解析
4. **准备度评分 ≥ 85** 时推送 "可以报考" 通知
5. 考后失败自动生成补救计划

### 4.3 年度再认证

到期前 45 天自动触发 Delta 学习路径(只覆盖过去 12 个月的产品变更),显著低于首次学习成本。

---

## 五、旅程详细时间线(MVP 视角)

下表是 Expound 为单一 Partner Org 运行一次端到端旅程的典型节奏:

| 周 | 阶段 | Agent 自动化动作 | 人工检查点 |
|---|---|---|---|
| W1.D1 | Discover | Eligibility Scout 扫描公司官网 + 既有 AI 案例,产出差距报告与 tier 建议 | 合作伙伴 Champion 确认目标 tier |
| W1.D3 | Discover | Application Packager 生成申请表草稿 + Business Plan | 法务审核 MSA,Champion 签署 |
| W1.D5 | Discover | 提交申请、追踪 Anthropic 侧审核 | — |
| W2.D1 | Enable | Training Coach 根据花名册分发学习路径,创建每周日历 | Manager 批准路径 |
| W2–W4 | Enable | 每周一推送本周计划、每周五汇总完成率与风险项 | 逾期超过 3 天触发 escalation |
| W4.D5 | Certify | 诊断测验 + 薄弱点补强 | — |
| W5 | Certify | 3 轮模考 | — |
| W6 | Certify | 推送 "准备度达标、可报考" | 学员预约正式考试 |
| W7 | Launch | 基于 Agent SDK 生成第一个 Demo / POC 脚手架 | 技术 Lead review |
| W7.D4 | Launch | 起草联合方案白皮书 + 案例 1-pager | Marketing 审核 |
| W8 | Launch | Partner Directory listing + Co-marketing kit 发送 | — |
| 持续 | Grow | 每月 QBR 数据包、每季度 tier 进度 | Partner Success Manager 主持 QBR |

---

## 六、人机协作 / HITL 原则

以下动作**必须**经 Champion 或对应 owner 人工确认后才执行,不设"默认放行":

1. 向 Anthropic 提交正式申请
2. 签署任何协议(MSA、NDA、Co-sell Addendum)
3. 对外发送邮件或 Slack 消息
4. 在 Partner Directory 上架/下架
5. 修改 CRM 内的 account 字段或 deal 阶段

对于低风险的内部动作(生成文档草稿、排课、发送内部 reminder),默认自动执行,但日志全部可审计。

---

## 七、衡量 Expound 成功的指标

| 指标 | Baseline(人工) | Expound 目标 |
|---|---|---|
| 从申请到 Registered 认证完成 | 6–8 周 | **≤ 3 周** |
| 每名学员完成培训所需 Partner Success 人工投入 | 4 小时 / 人 | **≤ 30 分钟 / 人** |
| 首次认证通过率 | 60–70% | **≥ 85%** |
| 认证到期前 30 天完成再认证比例 | 40% | **≥ 80%** |
| Champion 满意度 (CSAT) | — | **≥ 4.5 / 5** |

---

## 八、下一步阅读

- `preview/index.html` —— 这条旅程的可视化预览
- `src/expound/` —— MVP 代码骨架(Orchestrator + Eligibility Scout + Training Coach)
- `README.md` —— 如何在本地跑起来
