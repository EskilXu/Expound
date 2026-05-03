# Claude トレーニング & 認定ガイド

> **本ガイドは 2 種類の読者向け**:
> - **企業 / チーム**: Anthropic Partner Network への加入有無に関わらず、組織として体系的に Claude を習得したい
> - **個人**: 自学で Claude を学び、公式認定を取得し、キャリアの資産にしたいエンジニア / プリセールス / PM
>
> **Partner Network のエンドツーエンドのフロー**(申請 → トレーニング → 認定 → ローンチ → 更新)だけ知りたい場合は [`partner-journey.ja.md`](./partner-journey.ja.md) を参照。本ガイドはより **トレーニング配分と受験戦略** に焦点を当てます。
>
> **注記**: 本ドキュメントは 2026 年 5 月時点で公開されている Anthropic のコース構造と認定フレームワークに基づきます。実際のコースカタログ、試験形式、有効期間は公式 Partner Portal / Anthropic Academy の最新情報を正とします。

---

## 第 1 部: 企業向けトレーニングガイド(Enterprise Track)

### 1.1 対象

| 組織タイプ | 典型的な動機 | 目標 |
|---|---|---|
| システムインテグレーター / コンサル | Partner Network 加入、NFR と割引、Claude 実装ビジネス | 1〜3 か月で Registered、3〜6 か月で Select |
| ISV / SaaS | プロダクトに Claude を統合、社内能力の支え | エンジニアの 80% が Tech Track 完了、Agent Developer 1〜2 名 |
| 大企業の社内 AI 部門 | 社内ユースケース推進、部門横断トレーニング | 社内 CoE を構築、認定者を継続的に輩出 |
| 教育機関 / 大学 | Claude 関連科目や実習班を開講 | 教員全員 Tech Track、受講生は Business / Dev で振り分け |

### 1.2 ロール別マトリクスとトレーニング配分

「全員に同じ研修」はやめる。まずロールを棚卸しし、責務に応じて学習パスを割り当てる。

| 社内ロール | 推奨パス | 目標認定 | 投入(1 人あたり) | 完了期間 |
|---|---|---|---|---|
| プリセールス / ソリューションコンサル | Business + Technical | Business Associate + Solutions Architect | 〜80h | 6〜8 週 |
| 営業 / Alliance | Business | Business Associate | 〜30h | 2〜3 週 |
| PM / プロダクト | Business + Tech 選択 | Business Associate(+ Tech 1 モジュール) | 〜40h | 3〜4 週 |
| バックエンド / アプリ開発 | Developer / Agent | Agent Developer | 〜120h | 8〜12 週 |
| Solutions Engineer | Technical + Developer | Solutions Architect + Agent Developer | 〜150h | 10〜14 週 |
| データ / ML エンジニア | Technical(深掘り) | Solutions Architect | 〜80h | 6〜8 週 |
| 法務 / コンプライアンス | Business の「セキュリティ・コンプライアンス」モジュール | 認定不要 | 〜8h | 1 週 |
| マーケ / コンテンツ | Business 概観 | 認定不要 | 〜6h | 1 週 |

### 1.3 チームの認定目標(参考ティア配分)

例: 30 名規模のコンサル会社、目標 Select tier:

```
        Business Associate × 5 ─────────────────────  プリセ / PM / Alliance をカバー
        Solutions Architect × 3 ────────────────────  SE / プリセ主力をカバー
        Agent Developer × 2 ────────────────────────  デリバリーのコアエンジニアをカバー
        + 業界スペシャリゼーション × 1(Financial / Healthcare 等)── 注力業界を支える
```

冗長性: 各重要認定は最低 2 名持ちにし、単一障害点を避ける。

### 1.4 四半期運用リズム(参考)

| 四半期 | テーマ | 主要成果 |
|---|---|---|
| Q1 | **棚卸し + Business リテラシー** | 全員 Business 概観完了; 3〜5 人が BA 開始 |
| Q2 | **Tech 主力研修** | SA / Dev 候補の Tech コアモジュール完了; ハッカソン 2 回 |
| Q3 | **認定スプリント** | 模試 + Office Hours、目標人数の認定取得 |
| Q4 | **振り返り + GTM 落とし込み** | 事例ホワイトペーパー、リファレンス顧客、来年の学習ロードマップ |

### 1.5 社内能力構築: 4 本の柱

「人を試験に送る」だけでは足りない。長期の社内エコシステムが要る:

1. **Center of Excellence (CoE)**
   2〜3 名のチームが prompt library、ベストプラクティスの蓄積、新人 onboarding を担当。月次 demo day。
2. **社内 Prompt / Skill ライブラリ**
   production グレードの prompt、agent skill、Claude Code subagent をレビュー後に内部 git に蓄積し再利用。
3. **週次「Claude Hour」**
   1 時間の社内共有: Anthropic 公式 release notes 速読、社内の落とし穴、顧客事例。
4. **Anthropic Office Hours の活用**
   Premier / Select は通常週 1 時間の Office Hours を持つ。当番制で参加し、課題を持ち帰る。

### 1.6 ガバナンスとコンプライアンスの要点

| 観点 | 推奨プラクティス |
|---|---|
| **API キー管理** | プロジェクト別キー; production / staging / 教育 lab を分離; lab キーは月次予算上限あり |
| **HITL 境界** | 対外コミュニケーション、署名、production デプロイは必ず人間承認; 社内ドラフトは自動可 |
| **データコンプライアンス** | 顧客データは prompt 投入前に PII 除去; 機微業界(医療、金融)は専用チャネル経由 |
| **コスト管理** | Partner Handbook、安定 system prompt は必ず Prompt Caching; 月次で token 消費 Top 10 をレビュー |
| **監査** | 各 agent 呼び出しで run log を出力; production は trace ID から prompt + モデル版数まで遡れる |
| **モデルバージョン** | production モデル ID(例: `claude-opus-4-7`)を固定; アップグレードは staging で段階適用 |

### 1.7 Anthropic 公式リソースとの対応

| リソース | 用途 | 利用者 |
|---|---|---|
| Anthropic Academy | 自学メイン入口 | 全員 |
| Partner Portal | 申請、ティア状況、公式コースカタログ | Champion / Alliance |
| Solutions Engineer Office Hours | 実問題の Q&A | SA / Dev 主力 |
| Anthropic Cookbook(GitHub) | コードサンプル | Dev / SE |
| Claude Docs(docs.claude.com) | API、ツール、Skills のリファレンス | 開発関連の全員 |
| Anthropic Blog / Release Notes | 製品更新 | CoE が週次でスキャン |

### 1.8 Expound との関係

`partner-journey.ja.md` は「エンドツーエンドの 6〜8 週間フロー」を記述し、Expound はそれを自動化します。本ガイドが補うのは **「長期のトレーニング配分 + 社内エコシステム」** です。Expound の役割:

- Eligibility Scout が **現状ロールマトリクス vs 目標ティア** のギャップレポートを出力
- Training Coach が本ガイドの「ロール → 学習パス」を具体的な週次計画にマッピング
- Certification Prep が受験準備を担当(第 2 部 §2.4)
- Compliance & Renewal が認定期限の 45 日前に Delta 学習をトリガー

### 1.9 企業実践 3 ケース

#### ケース A: BlueRiver Consulting — 30 名のブティックコンサルがゼロから Select tier へ

**背景**: 30 名の戦略コンサル。Claude に興味があるのは創業パートナー 1 名のみ、他のチームは未経験。

**6 か月リズム**:
- M1〜M2: 全員 Business 概観(週 1 回ランチセッション)、5 人が BA を開始
- M3〜M4: 5 人が BA 完了; 3 人が SA 路線、1 人が Agent Dev 開始
- M5: Anthropic 申請 + Lab 実戦 + 模試スプリント
- M6: 3 SA + 1 Agent Dev 合格、Partner Directory 掲載

**結果**: 6 か月で Select 到達、Claude 実装案件 2 件・計 80 万元を獲得。

**重要決定**: Q1 は急いで認定を取らせず、まず全員に「自分たちが何を売るか」を理解させる。Champion が時間の 30% を社内推進に投じた。

#### ケース B: NorthPole AI — 200 名 SaaS、Partner には行かないが社内 CoE を建てる

**背景**: 製品に Claude を統合する必要。AI チーム 8 名 + 他のエンジニア 60 名は LLM 未経験。

**経路**:
- 8 名の AI エンジニア全員が Agent Developer を取得(4 か月)
- 取得後、各人が 5 名の「弟子」を持ち、週 1 回 1-on-1 + 月次 demo day
- 業務モデル上 Partner Network には申請しない

**ガバナンス**: lab キーは月 2000 USD 上限; production キーは CoE が集中管理し、すべての prompt はレビュー後に格納。

**結果**: 6 か月で 40% のエンジニアが Claude 統合を独力で出荷可能、製品 NPS が 12 ポイント上昇。

**踏んだ落とし穴**: 最初の「弟子」のうち 3 名が動画視聴のみで手を動かさず、3 か月成長なし。以降「月 1 PR 提出」を必須化。

#### ケース C: GlobalBank EMEA — コンプラ最優先の社内デプロイ

**背景**: 大手銀行。データは SaaS から外に出せず、Claude は Bedrock デプロイ。社内 50 名のみ研修、対外活動なし。

**経路**:
- 全員 Business 概観(8h)、できる/できないを理解
- 25 名が SA 路線(うち 10 名認定取得)
- 10 名が Agent Developer 上級(うち 5 名取得)

**ガバナンス**: 各 prompt は PII マスキングパイプラインを経由; モデルバージョンを `claude-opus-4-7` に固定し、アップグレードは 6 週間の段階展開; 監査ログは 7 年保管。

**結果**: 4 つの production agent をリリース(KYC アシスト、コンプラ Q&A、レポート草稿、知識検索)。月間 token 消費 1500 USD、キャッシュヒット率 92%。

---

## 第 2 部: 個人向けトレーニングガイド(Individual Track)

### 2.1 自己ポジショニング: あなたはどのタイプ?

| 現在 / 目指す姿 | 推奨メイン路線 | 目標認定 |
|---|---|---|
| プリセ / 営業 / PM / 業界コンサル | Business Track | Claude Business Associate |
| ソリューションアーキテクト / シニアフロント / Tech プリセ | Technical Track | Claude Solutions Architect |
| バックエンド / Agent / アプリ開発 | Developer / Agent Track | Claude Agent Developer |
| 全方位を目指す(独立コンサル、フリーランス) | Business + Technical(2 段階) | BA → SA |
| 学生 / 完全初心者 | Business 入門、その後判断 | Business Associate |

**判断方法**: 日々の 80% の時間を何に使っているかを見る。コードを書くなら Developer、ソリューション設計なら Technical、顧客と要件を話すなら Business。

### 2.2 3 つの学習スタイルの比較

| スタイル | 長所 | 短所 | 向いている人 |
|---|---|---|---|
| 純自学(Academy + ドキュメント) | 無料 / 柔軟 | 質問先がない、途中離脱しやすい | 自走力強・牽引するプロジェクトがある人 |
| 自学 + Office Hours | 重要な疑問は答えられる | 時間枠に合わせる必要 | 多くの SA / Dev 候補 |
| 企業 / Partner 研修への参加 | 仲間がいる、推進力 | 会社のペースに依存 | すでに Partner Org 所属 |
| 有料 Bootcamp | テンポが速く密度が高い | コスト高、品質ばらつき | 4〜6 週で立ち上げたい人 |

### 2.3 推奨投入時間(参考)

> いずれも「業余時間に学習、週 5〜8 時間」前提。フルタイムなら 60% 短縮可。

| 目標認定 | 総時間 | 週数(業余) | 備考 |
|---|---|---|---|
| Business Associate | 30〜40h | 4〜5 週 | 営業 / 商務バックグラウンドあれば 3 週まで圧縮可 |
| Solutions Architect | 80〜120h | 10〜14 週 | Lab 部分は反復が必要なことがある |
| Agent Developer | 120〜180h | 14〜20 週 | エンドツーエンドの agent プロジェクト最低 1 つ必要 |

### 2.4 各認定の受験戦略

#### 2.4.1 Claude Business Associate

**形式**: 多肢選択 60 問 + シナリオ問題 2 問、オンライン監督。合格 75%。

**リズム**:
- 第 1〜2 週: Anthropic Academy の Business モジュールを通読
- 第 3 週: 公式サンプル問題 + 事例研究 1 本
- 第 4 週: フル模試 2 セット、誤答を集中復習

**よくある落とし穴 Top 3**:
1. **バリュープロポジションの言い方**: Claude は「もう一つの LLM」ではなく、安全性、長コンテキスト、Agentic を強調。「顧客シナリオ → Claude の差別化価値」から答える。
2. **価格 & パッケージング**: Tier、Token、Caching 割引が頻出。公式ドキュメントの表を暗記。
3. **コンプラ境界**: HIPAA、FedRAMP 等の「どのシナリオにどのデプロイ形態を勧めるか」は基本フレームを暗記。

#### 2.4.2 Claude Solutions Architect

**形式**: 多肢選択 40 問 + Lab 1 件(Claude ソリューションを設計)。合格 80% + Lab 合格。

**リズム**:
- 第 1〜3 週: Messages API、Prompt Engineering、Tool Use(コードを叩く、見るだけ NG)
- 第 4〜6 週: Agent SDK、Memory、Compaction(小さな agent demo を 1 つ)
- 第 7〜8 週: Prompt Caching、Extended Thinking、Evals
- 第 9〜10 週: 実顧客シナリオ 2 つを選び、自分でソリューション設計の草案を作る
- 第 11〜12 週: 模試 + Lab 実戦(4 時間でソリューション設計)

**Lab 合格の鍵**:
- 機能を盛らない、まず **業務課題 + 評価基準** を明確化
- 必須要素: アーキ図、prompt 設計、HITL 境界、コスト見積、リスクと緩和策
- evaluation 設計を提示(良し悪しをどう測るか)

**よくある落とし穴 Top 3**:
1. **Tool Use のエラー処理**: tool 呼び出し失敗、タイムアウト、フォーマット不正の処理は頻出。
2. **長期 agent の状態管理**: Memory ツール、構造化 state、圧縮の使い分けは配点重大。
3. **コストとレイテンシのトレードオフ**: キャッシュヒット率、Haiku / Sonnet / Opus の選択。数字で答えられること。

#### 2.4.3 Claude Agent Developer

**形式**: 実機 Lab、Agent SDK で指定 agent を構築しテストセットを通過。合格率 ≥ 85%。

**リズム**:
- 第 1〜4 週: Agent SDK 基礎、公式 quickstart を全て動かす
- 第 5〜8 週: subagent、MCP、Skills、Hooks の上級機能に深入り
- 第 9〜12 週: エンドツーエンドプロジェクトを 2 つ(coding agent 寄り 1 つ、業務 agent 寄り 1 つ)
- 第 13〜16 週: 模試 + プロジェクトを production グレードへリファクタ(evals、エラー処理、observability)

**Lab 合格の鍵**:
- プロジェクト構成が明快、README + evals あり
- エラー処理のカバレッジ高(tool 失敗、モデル timeout、context overflow)
- observability あり(各 agent 呼び出しのログ)
- コスト意識(Caching 使用、合理的なモデル階層)

**よくある落とし穴 Top 3**:
1. **Context 管理**: compaction / Memory / subagent の隔離を使えず、すぐ context オーバー。
2. **Tool 設計**: tool description が曖昧で agent が誤呼び出し連発。
3. **Eval 設計**: evals なしで production 化するとほぼ確実に失敗。

### 2.5 実戦プロジェクトの提案

試験は基礎の検証のみ。実用化には 1〜2 個のエンドツーエンドプロジェクトを推奨:

| 難度 | プロジェクト | 学べるもの |
|---|---|---|
| ★ | 個人用 PDF Q&A agent | Messages API、Tool Use 基礎 |
| ★★ | メール自動分類 + 返信草案 agent | Tool use、外部 API 統合、HITL |
| ★★ | Slack 社内ナレッジ Q&A bot | RAG、prompt caching、長コンテキスト |
| ★★★ | コードレビュー助手(GitHub Action) | Agent SDK、subagent、structured output |
| ★★★ | 多段リサーチ agent(Deep Research 風) | Subagent オーケストレーション、長期、context engineering |
| ★★★★ | 自業界の垂直 agent(法務 / 医療 / 財務) | 実データ、コンプラ、HITL 設計 |

4〜8 週続けられるものを 1 つ選び、完了後 OSS 化 / ブログ化。求職にも案件獲得にも非常に有利。

### 2.6 よくある誤解と対策

| 誤解 | 結果 | 正しいやり方 |
|---|---|---|
| Business を飛ばして Tech だけ | 顧客シナリオが分からず良い設計ができない | 最低 1 週は Business を通読 |
| 動画だけ見て手を動かさない | Lab で落ちる | 動画 1 本ごとに練習 1 つ |
| 最新モデルだけ追って基礎を学ばない | モデル更新で陳腐化 | Messages API、Prompt 設計など基礎は陳腐化しない |
| 一気に 3 つ受験 | 戦線が伸び挫折しやすい | まず BA(早い勝利)、その後 SA / Dev(長期投入) |
| evals を軽視 | 「動くように見えて」production で炎上 | 各 agent に専用 eval セット |
| 一人で抱え込む | 停滞しやすい | 学習仲間 1〜2 名、週次で進捗レビュー |
| コスト計算しない | 学習期に API 請求が爆発 | Lab は Haiku、Caching 必須、月次レビュー |

### 2.7 不合格だったら?

初回不合格は珍しくない、落ち込まなくて良い。

1. 誤答レポートを取得(認定システムが弱点領域をフィードバック)
2. 弱点に絞って 1〜2 週補強(コース全体の再学習はしない)
3. 模試を 2 セット、準備度 ≥ 85 で再予約
4. SA / Agent Dev の Lab 不合格は通常「エンジニアリング実践不足」、実プロジェクトを 1 つ作ってから再挑戦推奨

### 2.8 合格後

認定はスタート地点。次の一歩:

| 路線 | 進め方 |
|---|---|
| 技術深堀り | Anthropic release notes を継続フォロー、新機能ごとに分析記事を書く; Cookbook に貢献 |
| 求職 / 転職 | プロジェクトを GitHub に公開 + 技術ブログ; Partner Network 求人を注視 |
| 独立コンサル | LinkedIn / X で事例継続発信; 小型 PoC で評判を作る |
| 社内 Champion | 会社の CoE や Claude Hour を主導 |
| コミュニティ貢献 | Anthropic Discord、MCP エコシステム、OSS agent プロジェクト |

### 2.9 継続学習リズム

モデルとツールの反復が早い。学習を日常化:

- **週次**: 30 分で Anthropic Blog + Release Notes
- **月次**: 新機能の動かしてみる demo 1 本(新 Skills、新 MCP server 等)
- **四半期**: フルプロジェクト 1 本 / 深い技術記事 1 本
- **認定期限 45 日前**: Delta 学習パス(直近 12 か月の変更のみ)

### 2.10 個人成長の 3 ケース

#### ケース A: 張涛 — 8 年 Java バックエンド → Agent Developer

**起点**: LLM 未経験、会社でも Claude 未使用。完全に業余時間で学習。

**経路(8 か月)**:
- M1: Business 速読、Claude にできることを把握
- M2〜M3: Messages API + Tool Use、公式 cookbook を全て写経
- M4〜M7: OSS GitHub プロジェクト 2 件(コードレビュー bot + メール agent)、反復改善
- M8: Lab 模試 + Agent Developer 認定取得

**踏んだ落とし穴**: M4 でいきなり subagent + Memory に手を出して token 爆発。context engineering の基礎を補習。

**結果**: AI スタートアップに転職、年収 40% アップ。OSS 2 件で計 800+ stars。

#### ケース B: 林佳 — PM 5 年 → Solutions Engineer

**起点**: コーディング経験ゼロ、目標会社が BA + SA の両方を要求。

**経路(5 か月)**:
- BA(週 6h)+ SA(週 6h)を並行
- M3: 2 週間ハンズオン Bootcamp に参加、コード恐怖症を克服
- M4: BA 合格、SA は初回 Lab 不合格(アーキ図にコスト見積がなかった)
- M5: 弱点を集中補強、SA 二回目で合格

**結果**: Partner SE チームに加入、当初はシニア SA とペア勤務。

**振り返り**: PM だからと Lab を飛ばさない、Lab こそが差別化。

#### ケース C: 王雅 — シニア企業コンサル → 独立 + Claude サービス追加

**起点**: 企業コンサル 5 年(金融・小売中心)、AI サービスラインを追加したい。

**経路(3 か月、フルタイム)**:
- M1: BA フルカリキュラム(15 日で合格)
- M2: SA フル、途中で顧客 PoC 案件を Lab 実戦に活用
- M3: Agent Dev 入門、demo 1 件作成(認定は未受験)

**結果**: LinkedIn の認定更新後 1 か月以内に PoC 引合いを 3 件獲得; 4 か月後に最初の 30 万元案件を成約。

**重要洞察**: 認定 + 実事例の両方が必須。証明書だけで demo がないと顧客は契約しない。

---

## 第 3 部: 個人 ↔ 企業の協働

### 3.1 個人として社内で Champion になる

IC でも会社が Claude 推進したいなら、社内 Champion を主動で引き受けると良い:

- HR / マネージャに役割マトリクス設計を支援(§1.2 参照)
- 週次 Claude Hour を主導
- 社内 Prompt / Skill ライブラリの維持
- Anthropic Partner Account Manager との窓口

これは社内昇進の重要な資本になることが多い。

### 3.2 企業として高潜在の個人を見極め支援する

| シグナル | 含意 |
|---|---|
| API 質問を主動で出す、issue を立てる | 探究意欲あり |
| 業余で side project | エンジニア能力十分 |
| 非技術同僚にも Claude を分かりやすく説明できる | 技術 + ビジネス両刀、希少 |
| release notes を継続フォロー | 長期コミット信号強 |

これらの人には: lab 予算、Office Hour 優先、業界カンファレンス参加機会を与え、SA / Agent Dev 認定に送る。

### 3.3 個人 ↔ 企業協働の 3 ケース

#### ケース A: 李エンジニア(NorthPole AI 社内 Champion → Tech Lead)

最初は普通のエンジニア、社内「Claude Hour」を主動で立ち上げ。1 年で:
- 会社を Partner 関係なし → Registered に
- 自身は Tech Lead 昇進、給与 35% アップ
- 社内 Prompt Library を OSS 化、業界の注目を獲得

**示唆**: 会社の方向がまだ定まっていないとき、空白を埋めに行く人は見られる。

#### ケース B: 陳博士(企業出資で認定取得 → 起業 → 逆向きパートナーシップ)

ある多国籍 SaaS で BA + SA + Agent Dev を出資取得。1 年後に独立、5 名の AI コンサルを起業。
- 元雇用主が最初の顧客に(まさにこのサービスを必要としていた)
- 元雇用主の Sub-Partner となり referral を共有
- Partner Directory 上で互いに参照、共同 GTM を実施

**示唆**: 育てた人材の「離脱」は必ずしも損失ではない、長期エコシステム資産に転換し得る。

#### ケース C: 周亮(OSS 貢献者 → 複数 Partner からのオファー)

業余で MCP エコシステムに OSS server を 3 件貢献(GitHub、Notion、社内 wiki 統合)。
- プロジェクトは 1500+ stars、Anthropic 公式 awesome list に収録
- Partner Org 3 社から協業オファー
- 最終的にコントラクター + ストックオプションで 1 社に参加、独立性を維持

**示唆**: 新エコシステム(MCP / Skills / Subagents)で継続貢献することは、個人と企業の天然の接続装置。

---

## 付録

### A. 認定チートシート

| 認定 | 形式 | 合格 | 有効期間 | 推奨時間 |
|---|---|---|---|---|
| Business Associate | 多肢選択 60 問 + シナリオ 2 問 | 75% | 12 か月 | 30〜40h |
| Solutions Architect | 多肢選択 40 問 + Lab | 80% + Lab 合格 | 12 か月 | 80〜120h |
| Agent Developer | 実機 Lab | テストセット ≥ 85% | 12 か月 | 120〜180h |

### B. 学習リソース一覧(主に英語)

- Anthropic Academy — メイン入口
- docs.claude.com — API / ツール / Skills のリファレンス
- Anthropic Cookbook(GitHub)— コードサンプル
- Anthropic Blog / Release Notes — 製品更新
- Claude Code ドキュメント — coding agent を作るなら必読
- MCP プロトコルドキュメント(modelcontextprotocol.io)— Agent エコシステムの拡張

### C. 推奨「30 日 MVP 学習プラン」(個人、Tech Track)

| 日 | ゴール | 成果物 |
|---|---|---|
| D1〜D3 | Messages API quickstart を動かす | 対話できるスクリプト |
| D4〜D7 | Prompt Engineering 学習 | 1 つのタスクに対し 3 バージョンの prompt 比較 |
| D8〜D14 | Tool Use 深掘り | 外部 API を呼べる小 agent |
| D15〜D21 | Agent SDK + Memory | 多ターンに渡るリサーチ / 整理 agent |
| D22〜D26 | Prompt Caching + Evals | 上記 agent に caching と evals を追加 |
| D27〜D30 | 振り返り + 模試 1 セット | 自己評価、来月のペース決定 |

### D. Expound との接続

会社が Expound を使う場合:
- 個人の学習進捗が Training Coach ダッシュボードに自動同期
- 模試スコアが Certification Prep の準備度に反映
- 企業ダッシュボードで「チーム全体の準備度」を確認可能

独立学習者の場合:
- Expound の OSS コード自体がマルチエージェントの事例研究、`src/expound/` の通読を推奨
- プレビューページ(`preview/index.ja.html`)は「agentic サービスの見え方」のビジュアル参考に好適

---

## 次のステップ

- エンドツーエンドの Partner フローは [`partner-journey.ja.md`](./partner-journey.ja.md)
- コードは [`../src/expound/`](../src/expound/)
- demo を動かすなら [`../README.ja.md`](../README.ja.md)
