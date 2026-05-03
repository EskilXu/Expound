# Expound

> 企業が **Anthropic Partner Network** に参加し、トレーニングと認定の旅程を完了するのを支援するエージェント型サービス。

Expound はマルチエージェントでオーケストレーションされる onboarding サービスです。本来は職種・部門・6〜8 週間にまたがるパートナー申請とトレーニングのプロセスを、エージェント主導 + 人間の確認(HITL)を経るパイプラインに圧縮します。

> 🌐 他言語: [简体中文](./README.md) · [English](./README.en.md)

## クイックツアー

| 見たいもの | 開く |
|---|---|
| 旅程の全体像(5 ステージ / ティア / トレーニング行列 / 認定) | [`docs/partner-journey.ja.md`](./docs/partner-journey.ja.md) |
| トレーニング配分 & 個人の受験戦略(企業 + 個人) | [`docs/training-guide.ja.md`](./docs/training-guide.ja.md) |
| ビジュアルプレビューページ | [`preview/index.ja.html`](./preview/index.ja.html) — ローカルでブラウザで開く |
| コードのスケルトン | [`src/expound/`](./src/expound/) |

プレビューページは静的ファイルとしてそのまま開けます(ビルド不要):

```bash
open preview/index.ja.html        # macOS
xdg-open preview/index.ja.html    # Linux
```

## アーキテクチャ概要

```
             ┌───────────────────────────────┐
Slack/Web ─▶ │   Orchestrator (Opus 4.7)     │ ◀── HITL 承認
             └──────────────┬────────────────┘
                            │  delegate · aggregate
  ┌────────────┬────────────┼────────────┬────────────┐
  ▼            ▼            ▼            ▼            ▼
Eligibility Application  Training   Certification Enablement
  Scout     Packager      Coach    Proctor-Prep     / GTM
```

- **Orchestrator**: Claude Opus 4.7 — ルーティング、集約、HITL のオーケストレーション。
- **サブエージェント**: Claude Sonnet 4.6 — それぞれが 1 つのステージを担当。
- **高頻度な小タスク**: Claude Haiku 4.5(タグ付け、分類、進捗の書き戻し)。
- **長期にわたる状態**: 構造化 state + Memory、週をまたいで永続化。
- **コスト最適化**: Partner Handbook や認定大綱など、大容量で安定した知識は Prompt Caching を利用。

## MVP の範囲

v0.1(本リポジトリの現状)は **Orchestrator + Eligibility Scout + Training Coach** の CLI デモにフォーカスし、マルチエージェントの委譲と HITL フローをデモします。その他のサブエージェントはインターフェースだけ用意し、段階的に組み込みます。

| Agent | 状態 | 説明 |
|---|---|---|
| Orchestrator | ✅ MVP | tool use を用いたマルチエージェント・オーケストレーション |
| Eligibility Scout | ✅ MVP | 企業プロフィールを与えると、ギャップレポートとティア提案を出力 |
| Training Coach | ✅ MVP | 役割に応じて 4 週間の学習パスを生成 |
| Application Packager | 🚧 stub | インターフェースのみ定義、テンプレートを返す |
| Certification Prep | 🚧 stub | インターフェースのみ定義、テンプレートを返す |
| Enablement / GTM | 🚧 stub | インターフェースのみ定義、テンプレートを返す |

## ローカルで動かす

```bash
# 1. クローンしてディレクトリに入る
cd Expound

# 2. uv または venv を推奨
python -m venv .venv && source .venv/bin/activate
pip install -e .

# 3. API キーを設定
export ANTHROPIC_API_KEY=sk-ant-...

# 4. デモを実行
expound demo
```

デモは架空の企業「ACME Consulting」を Partner Org として、以下を順に実行します:
1. Eligibility Scout がスキャンしてギャップレポートを出力
2. Training Coach がサンプル受講者の学習パスを生成
3. (申請送信前の) HITL 承認カードをシミュレーション

## Provider の切り替え(Anthropic / DeepSeek)

Expound は `EXPOUND_PROVIDER` 環境変数で 2 つの provider を切り替えます:

| Provider | 既定モデル(orchestrator / sub-agent / fast) | 必須 env | Orchestrator 利用可? |
|---|---|---|---|
| `anthropic`(既定) | `claude-opus-4-7` / `claude-sonnet-4-6` / `claude-haiku-4-5` | `ANTHROPIC_API_KEY` | ✅ |
| `deepseek` | `deepseek-reasoner` / `deepseek-chat` / `deepseek-chat` | `DEEPSEEK_API_KEY` | ❌ sub-agent のみ直接呼び出し可 |

```bash
# 既定: Anthropic
export ANTHROPIC_API_KEY=sk-ant-...
expound demo

# DeepSeek へ切り替え(注: orchestrator が依存する Anthropic ベータ機能 ──
# tool_runner / adaptive thinking ── は DeepSeek の Anthropic 互換 shim では
# 未実装のため、その経路では明示的にエラーになります)
export EXPOUND_PROVIDER=deepseek
export DEEPSEEK_API_KEY=sk-...
expound demo  # sub-agent 部分は動作;orchestrator 段階で明確なエラー
```

ロールごとにモデル名を上書きする場合:

- `EXPOUND_MODEL_ORCHESTRATOR`
- `EXPOUND_MODEL_SUB_AGENT`
- `EXPOUND_MODEL_FAST`

## 設計原則

- **HITL がデフォルト**: 対外的なコミュニケーション、署名、提出はすべて人間の確認を必要とし、自動承認は設けない。
- **Prompt Caching 優先**: Partner Handbook など、安定した大容量コンテンツは `cache_control` に入れる。
- **構造化された出力**: サブエージェントは Pydantic モデルを返し、オーケストレーション層が集約・監査しやすい形にする。
- **可観測性**: エージェント呼び出しごとに run log を書き、後段の Dashboard で消費しやすくする。

## ロードマップ

- シングルテナントの CLI MVP をマルチテナント + Slack Bot に拡張
- Anthropic Academy / 公式 Partner Portal との接続(モックインターフェースを準備済み)
- 永続化ストレージの導入(Postgres + オブジェクトストレージ)
- run log を消費する Dashboard(Next.js)

## ライセンス

未定。リポジトリは現在、設計フェーズです。
