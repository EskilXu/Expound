# Expound

> Agentic service that helps enterprises join the **Anthropic Partner Network** and complete the training & certification journey.

Expound 是一个多 Agent 编排的 onboarding 服务,把原本需要跨角色、跨部门、跨 6–8 周的合作伙伴申请与培训流程,压缩为由 Agent 主导、人在环(HITL)审批的流水线。

## 快速导览

| 我想看… | 打开 |
|---|---|
| 旅程总体说明(5 阶段 / 层级 / 培训矩阵 / 认证) | [`docs/partner-journey.md`](./docs/partner-journey.md) |
| 可视化预览页 | [`preview/index.html`](./preview/index.html) —— 本地用浏览器打开 |
| 代码骨架 | [`src/expound/`](./src/expound/) |

预览页直接打开即可(无需构建步骤):

```bash
open preview/index.html        # macOS
xdg-open preview/index.html    # Linux
```

## 架构一览

```
             ┌───────────────────────────────┐
Slack/Web ─▶ │   Orchestrator (Opus 4.7)     │ ◀── HITL 审批
             └──────────────┬────────────────┘
                            │  delegate · aggregate
  ┌────────────┬────────────┼────────────┬────────────┐
  ▼            ▼            ▼            ▼            ▼
Eligibility Application  Training   Certification Enablement
  Scout     Packager      Coach    Proctor-Prep     / GTM
```

- **Orchestrator**:Claude Opus 4.7,路由、聚合、HITL 编排。
- **子 Agent**:Claude Sonnet 4.6,各自负责一个阶段的工作。
- **高频小任务**:Claude Haiku 4.5(打标、分类、进度回写)。
- **长程状态**:结构化 state + Memory,跨周持久化。
- **成本优化**:大体量稳定知识(Partner Handbook、认证大纲)用 Prompt Caching。

## MVP 能力边界

v0.1(本仓库当前状态)聚焦在 **Orchestrator + Eligibility Scout + Training Coach** 的 CLI demo,演示多 Agent 委派与 HITL 流程。其他子 Agent 预留接口,逐步接入。

| Agent | 状态 | 说明 |
|---|---|---|
| Orchestrator | ✅ MVP | 基于 tool use 做多 Agent 编排 |
| Eligibility Scout | ✅ MVP | 给定公司画像,产出差距报告与 tier 建议 |
| Training Coach | ✅ MVP | 根据角色生成 4 周学习路径 |
| Application Packager | 🚧 stub | 已定义接口,返回模板 |
| Certification Prep | 🚧 stub | 已定义接口,返回模板 |
| Enablement / GTM | 🚧 stub | 已定义接口,返回模板 |

## 本地运行

```bash
# 1. 克隆并进入目录
cd Expound

# 2. 建议用 uv 或 venv
python -m venv .venv && source .venv/bin/activate
pip install -e .

# 3. 配置 API Key
export ANTHROPIC_API_KEY=sk-ant-...

# 4. 跑 demo
expound demo
```

Demo 会以一个虚构公司 "ACME Consulting" 作为 Partner Org,依次触发:
1. Eligibility Scout 扫描并产出差距报告
2. Training Coach 为一个示例学员生成学习路径
3. 模拟一个 HITL 审批卡片(提交申请前)

## 设计原则

- **人在环是默认**:对外通讯、签署、提交统统需要人工确认,不设默认放行。
- **Prompt Caching 优先**:Partner Handbook 等稳定体量大的内容放进 `cache_control`。
- **结构化输出**:子 Agent 返回 Pydantic 模型,便于编排层聚合与审计。
- **可观测性**:每次 Agent 调用写 run log,方便后续 Dashboard 消费。

## 下一步(Roadmap)

- 将 MVP 的单租户 CLI 扩展为多租户 + Slack Bot
- 接入 Anthropic Academy / 官方 Partner Portal(模拟接口已预留)
- 引入持久化存储(Postgres + 对象存储)
- Dashboard(Next.js)消费 run log

## 许可证

待定。仓库目前处于设计阶段。
