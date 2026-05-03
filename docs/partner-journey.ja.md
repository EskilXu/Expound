# Anthropic Partner Network — トレーニング & 認定の旅程概要

> **対象範囲**: 本ドキュメントは、Anthropic Partner Network への参加を希望する企業(システムインテグレーター、コンサルティング会社、ISV、リセラー)が、ゼロから「認定パートナー」となり、その後継続的に運営していくまでの完全な旅程を説明します。**Expound** のエージェントサービスは、この旅程に沿って各ステップをオーケストレーション・支援・加速します。
>
> **注記**: 本ドキュメントが示すのは **参考となる旅程モデル** です。実際のティア名称、コースカタログ、認定科目は、Anthropic 公式 Partner Portal の最新情報を正とします。Expound の Eligibility Scout エージェントは、実行時に公式ページから最新の要件を取得し、ローカル知識を上書きします。

---

## 1. 旅程の全体像(5 ステージ)

```
     ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
 ──▶ │ 1.       │──▶│ 2.       │──▶│ 3.       │──▶│ 4.       │──▶│ 5.       │
     │ Discover │   │ Enable   │   │ Certify  │   │ Launch   │   │  Grow    │
     └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
       〜1 週間        2〜3 週間       2 週間           2 週間         継続
```

| ステージ | 期間(参考) | 主要成果物 | Expound 主担当エージェント |
|---|---|---|---|
| **1. Discover** 発見 & 申請 | 3〜7 日 | ギャップレポート、Business Plan、目標ティア、署名済 MSA | Eligibility Scout + Application Packager |
| **2. Enable** 有効化 & トレーニング | 2〜3 週間 | チームの学習パス、完了率 ≥ 90%、講師ライブの録画 | Training Coach |
| **3. Certify** 認定 | 1〜2 週間 | 少なくとも N 名の認定 Solutions Architect / Business Associate | Certification Proctor-Prep |
| **4. Launch** ローンチ & 共同 GTM | 2 週間 | Demo / POC スキャフォールド、事例ホワイトペーパー、Partner Directory 掲載 | Enablement / GTM Agent |
| **5. Grow** 成長 & 更新 | 継続 | 四半期業績レビュー(QBR)、ティア昇格、年次再認定 | Compliance & Renewal(軽量デーモン) |

---

## 2. パートナーティア(参考 3 階層モデル)

実際の名称は Anthropic 公式に従います。本書では汎用的な 3 階層を例として用います:

| ティア | プロフィール | 典型的な要件 | 特典 |
|---|---|---|---|
| **Registered** | これから始める段階、まだ収益なし | Business Associate 認定 1 名 | 技術ドキュメント、コミュニティ、開発クレジット |
| **Select** | Claude 導入実績あり | Solutions Architect 2 名以上 + 成約案件 2 件 | 割引、共同マーケティング予算、NFR アカウント |
| **Premier** | 戦略的パートナー、業界の代表格 | 年間収益の閾値 + 業界特化認定 + カスタマーリファレンス | 専属 PAM、Co-sell、EBC チャネル |

Eligibility Scout は企業プロフィールを読み、**「現状は Registered を満たすが、Select までは認定 2 件 + リファレンス事例 1 件が不足」** のようなギャップレポートを返します。

---

## 3. カリキュラム(トレーニング行列)

Expound はコースを **役割** にマッピングし、各受講者にパーソナライズされた学習パスを提供します。「全員に同じ大綱を流し込む」ことはしません。

### 3.1 3 つのコア学習パス

| パス | 対象ロール | コースモジュール(例) | 目標認定 |
|---|---|---|---|
| **Business Track** | プリセールス、セールス、PM、Alliance | Claude のバリュープロポジション、価格 & パッケージング、セキュリティとコンプライアンスの基本、競合比較、ディスカバリー型営業、事例研究 | Claude Business Associate |
| **Technical Track** | Solutions Architect、技術プリセールス | Messages API 基礎、Prompt Engineering、Tool Use、Agent SDK、Evals、Prompt Caching、Extended Thinking | Claude Solutions Architect |
| **Developer / Agent Track** | アプリケーション開発者 | Claude Agent SDK 深掘り、Managed Agents、MCP、Memory、Compaction、Skills、長期エージェントの設計パターン | Claude Agent Developer |

### 3.2 任意の業界スペシャリゼーション

- Financial Services(コンプライアンス、KYC、開示書類への RAG)
- Healthcare & Life Sciences(HIPAA、匿名化)
- Public Sector(FedRAMP、データ主権)
- Software & Code(コーディングエージェント、レビュー、マイグレーション)

Premier 到達には通常、業界スペシャリゼーション 1〜2 件が必要です。

### 3.3 提供形態

- **自学自習**: 動画 + ハンズオンラボ(Academy)
- **ライブ**: 月次コホートのライブ + Q&A
- **Lab**: 実サンドボックスプロジェクト(例: 「ACME 銀行向けコンプライアンス Q&A エージェントを構築する」)
- **Office Hours**: Anthropic Solutions Engineer による週 1 時間のオープン Q&A

Training Coach は、これらの異種リソースを各受講者の週次プランに組み込み、毎週の進捗をプッシュし、遅延をリマインドします。

---

## 4. 認定(Certification)

### 4.1 科目と形式

| 認定 | 試験形式 | 合格基準(参考) | 有効期間 |
|---|---|---|---|
| **Claude Business Associate** | 多肢選択 60 問 + シナリオ問題 2 問、オンライン監督 | 75% | 12 か月 |
| **Claude Solutions Architect** | 多肢選択 40 問 + 実機 Lab 1 件(Claude ソリューションを設計) | 80% + Lab 評価合格 | 12 か月 |
| **Claude Agent Developer** | 実機 Lab: Agent SDK で指定エージェントを構築しテストセットを通過 | テストセット合格率 ≥ 85% | 12 か月 |

### 4.2 受験準備フロー(Proctor-Prep Agent)

1. **診断テスト**: コース完了後、自動で 20 問を出題し、弱点を特定
2. **弱点深掘り**: 弱点に的を絞った解説 + 追加問題
3. **3 ラウンドの模試**: 各ラウンド後に Claude が詳細な誤答解析を提供
4. **準備度スコア ≥ 85** で「受験可能」通知をプッシュ
5. 不合格時は自動で挽回プランを生成

### 4.3 年次再認定

有効期限の 45 日前に、自動で Delta 学習パス(過去 12 か月の製品変更だけをカバー)をトリガー。初回学習に比べ大幅に低コストです。

---

## 5. 詳細タイムライン(MVP 視点)

下表は、Expound が単一の Partner Org に対してエンドツーエンドの旅程を 1 回実行する典型的なリズムです:

| 週 | ステージ | エージェントの自動アクション | 人間のチェックポイント |
|---|---|---|---|
| W1.D1 | Discover | Eligibility Scout が会社サイト + 既存 AI 事例をスキャンし、ギャップレポートとティア提案を出力 | パートナーの Champion が目標ティアを承認 |
| W1.D3 | Discover | Application Packager が申請書ドラフト + Business Plan を生成 | 法務が MSA をレビュー、Champion が署名 |
| W1.D5 | Discover | 申請を提出、Anthropic 側のレビューを追跡 | — |
| W2.D1 | Enable | Training Coach が名簿に基づき学習パスを配布、週次カレンダーを作成 | Manager がパスを承認 |
| W2〜W4 | Enable | 毎週月曜に当週プランをプッシュ、毎週金曜に完了率とリスクを集計 | 3 日以上の遅延でエスカレーション |
| W4.D5 | Certify | 診断テスト + 弱点強化 | — |
| W5 | Certify | 3 ラウンドの模試 | — |
| W6 | Certify | 「準備度達成・受験可能」をプッシュ | 受講者が本試験を予約 |
| W7 | Launch | Agent SDK ベースで最初の Demo / POC スキャフォールドを生成 | 技術リードがレビュー |
| W7.D4 | Launch | 共同ソリューションのホワイトペーパー + 事例 1-pager を起案 | Marketing がレビュー |
| W8 | Launch | Partner Directory への掲載 + Co-marketing kit の送付 | — |
| 継続 | Grow | 月次 QBR データパック、四半期ティア進捗 | Partner Success Manager が QBR を主催 |

---

## 6. 人と機械の協働 / HITL の原則

以下のアクションは Champion または対応する owner の人間による確認を経た上でしか実行 **しません**。「デフォルト承認」は設けません:

1. Anthropic への正式申請の送信
2. 各種契約への署名(MSA、NDA、Co-sell Addendum)
3. 対外メールや Slack メッセージの送信
4. Partner Directory への掲載 / 取り下げ
5. CRM 内の account フィールドや deal ステージの変更

低リスクの内部アクション(ドキュメント草稿、スケジューリング、内部リマインダーの送信)は既定で自動実行され、ログは全て監査可能です。

---

## 7. Expound の成功指標

| 指標 | ベースライン(人手) | Expound の目標 |
|---|---|---|
| 申請 → Registered 認定完了 | 6〜8 週間 | **≤ 3 週間** |
| 受講者 1 人のトレーニング完了に要する Partner Success の人手投入 | 4 時間 / 人 | **≤ 30 分 / 人** |
| 初回認定合格率 | 60〜70% | **≥ 85%** |
| 有効期限 30 日前までに再認定完了する比率 | 40% | **≥ 80%** |
| Champion 満足度(CSAT) | — | **≥ 4.5 / 5** |

---

## 8. 次に読むもの

- `preview/index.ja.html` — この旅程のビジュアルプレビュー
- `src/expound/` — MVP のコードスケルトン(Orchestrator + Eligibility Scout + Training Coach)
- `README.ja.md` — ローカル実行方法
