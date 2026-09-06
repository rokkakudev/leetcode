# CLAUDE.md

このリポジトリは **面接対策のための訓練場** です。
目標はクラウド/プラットフォーム系ポジション (AWS SA, Google Cloud, 日経プロダクト企業のSRE/MLOps 等) の技術面接突破。

最優先事項は **作業効率ではなく、私自身の記憶と思考力の定着** です。
効率化してよい領域と、絶対に手を出してはいけない領域を以下に定義します。

---

## 1. エージェントの行動境界

### 絶対にやらないこと

- `problems/*/solution.py` に解法を書く・補完する・断片を示す
- **未解答の問題**について、アプローチ・データ構造・計算量のヒントを出す
  - (「ヒープを使うとよさそう」レベルもNG)
- `## なぜ最初に思いつかなかったか` 欄を代筆・要約する
- 私が聞いていないのに「より良い解法があります」と提示する

**解答済みかどうかの判定基準**: `git log` に該当問題の `solve:` コミットが存在すること。
存在しない問題については、上記の制約が全面的に適用されます。

### 明示的に依頼したときだけやること

| 依頼の言い方 | やること |
|---|---|
| 「レビューして」 | コミット済み解法の Python イディオム・可読性の指摘 |
| 「エッジケースを挙げて」 | テストケースの列挙（解法は書かない） |
| 「計算量を検証して」 | 私の自己申告が正しいか判定 |
| 「面接官として」 | **英語で**フォローアップ質問 → 私の説明の不明瞭な箇所を指摘 |
| 「類題を教えて」 | 同一パターンの問題番号のみ（解法は書かない） |

### 自由にやってよいこと

- `scripts/` 配下のツール実装・改善
- `notes/` のパターン別メモの構成整理・体裁統一
- README 索引の生成
- `progress.csv` の集計・可視化
- 環境構築、CI 設定、pytest の実行

---

## 2. 絶対の禁止事項（法務）

**LeetCode の問題文を複製しない。** 利用規約違反であり、DMCA 削除依頼の実例があります。

- 問題文の全文・部分コピー → 禁止
- 許容されるのは **問題 URL** と **自分の言葉での 1〜2 文の要約** のみ
- 公式エディトリアルの文章の転載も禁止

---

## 3. 環境

- Python **3.14**（LeetCode ジャッジと一致させる）
- パッケージ管理は **uv**。`.python-version` はコミット済み
- `python3` を直接叩かない（macOS の system Python 3.9.6 を踏むため）

```bash
uv run pytest                          # テスト実行
uv run python scripts/new.py 146 lru-cache Medium
```

**Copilot / インライン補完は必ず OFF**（`.vscode/settings.json` をコミット済み）。
LeetCode の問題は全て学習データに入っているため、`def twoSum(` と打った瞬間に
完成形がゴーストテキストで出ます。一度見たらその問題の訓練価値はゼロになります。

---

## 4. ディレクトリ構成

```
leetcode/
├── README.md              # 自動生成の索引（手で編集しない）
├── CLAUDE.md
├── .python-version
├── problems/
│   └── 0146-lru-cache/    # {4桁ゼロ埋めID}-{LeetCodeのURLスラッグ}
│       ├── README.md
│       ├── solution.py
│       └── test_solution.py
├── notes/                 # パターン別の横断メモ
├── scripts/
└── progress.csv           # 復習管理
```

**トピック別ディレクトリ（`arrays/`, `graphs/`）は作らない。**
1 問が複数トピックに跨るため必ず破綻します。トピックは frontmatter のメタデータとして持ち、索引から引く。

**ID は 4 桁ゼロ埋め。** `1-two-sum` だと辞書順が `1, 10, 100, 2` になります。

---

## 5. 問題 README のテンプレート

```markdown
---
id: 146
slug: lru-cache
difficulty: Medium
topics: [hash-table, linked-list, design]
first_solved: 2026-10-05
attempts: 2
confidence: 2
---

## 問題
https://leetcode.com/problems/lru-cache/
（1〜2 文で自分の言葉で要約）

## アプローチ

## 計算量
Time: / Space:

## なぜ最初に思いつかなかったか

## 類題
```

`## なぜ最初に思いつかなかったか` が **このリポジトリの本体** です。
解法は 3 ヶ月で忘れますが、自分の思考の癖は繰り返し出ます。ここを書かないなら
リポジトリを作る意味がありません。エージェントはこの欄に触れないこと。

`confidence` は 1〜3。復習間隔の算出に使う（1: 3日 / 2: 1週間 / 3: 3週間〜2ヶ月）。

---

## 6. Git 運用

**main に直コミット。** 1 問ごとのブランチ + PR は摩擦にしかならず、続きません。
代わりに **コミット粒度** で思考の変遷を残します。

```
solve:    0146 lru-cache (brute force, O(n))
refactor: 0146 lru-cache -> hashmap + dll, O(1)
note:     0146 add reflection on why DLL wasn't obvious
review:   0146 re-solved from scratch, 12min
```

プレフィックスは `solve:` / `refactor:` / `note:` / `review:` の 4 種に固定。

```bash
git log --oneline --grep="^review"   # 復習履歴だけ抽出
```

「素朴解」と「最適化後」を別コミットにすると、`git log` がそのまま学習ログになります。

---

## 7. 自動化ロードマップ

**先に作り込まない。ツール整備は立派な先延ばしです。**

| 時点 | やること |
|---|---|
| 〜3 問 | **手作業のみ**。テンプレートが自分に馴染むか検証する |
| 20 問 | `scripts/new.py`（雛形生成）を書く |
| 50 問 | `scripts/build_index.py`（README 索引生成）+ `progress.csv` 運用開始 |
| 100 問 | GitHub Actions で `uv run pytest` |

各段階に達する前に着手しない。特に 3 問の壁を守ること。

### scripts/new.py の仕様（20 問時点で実装）

```
uv run python scripts/new.py <id> <slug> <difficulty>
  → problems/{id:04d}-{slug}/ を作成
  → README.md（frontmatter + 見出しのみ、中身は空）
  → solution.py（空の Solution クラス）
  → test_solution.py（空のテスト）
  → 標準出力に solution.py のパスを表示（エディタで即開くため）
```

### scripts/build_index.py の仕様（50 問時点）

各 `problems/*/README.md` の frontmatter を読み、ルート README に
難易度・トピック・最終解答日つきの表を生成。**索引を手で書くと必ず更新が止まる。**

### progress.csv の仕様（50 問時点）

```csv
id,slug,difficulty,last_solved,confidence,next_review
```

`confidence` に応じて `next_review` を 3日 / 1週間 / 3週間 / 2ヶ月 と伸ばす。
「今日復習すべき問題」を出力するスクリプトを添える。
1 回解いただけの問題は 3 週間で消えるため、これが最大のリターン源。

---

## 8. 英語との一本化

面接で評価されるのは「解けたか」ではなく **「考えを声に出して説明できたか」**、
しかも英語です。解いた直後にこう依頼します。

> 「LRU Cache を解きました。面接官として、英語でフォローアップ質問を 3 つしてください。
> 私が英語で答えるので、説明が不明瞭な箇所を指摘してください。」

これで LeetCode の復習と英語のスピーキング訓練が同時に進みます。

---

## 9. このリポジトリの価値についての認識

**採用担当者はこのリポジトリを読みません。** LeetCode のソリューション集は全員が
持っており、ポートフォリオとしての加点はほぼゼロです。

このリポジトリの価値は **自分の復習インフラ** としてのみ存在します。
外向けの体裁を整える提案（README のバッジ、スター獲得の工夫、見栄えの改善など）は不要です。

採用選考で実際に効くのは、 **ポートフォリオとして作成するAWS SDKや個人アプリ、業務効率化ツールなど**
リポジトリの方。そちらは記憶の訓練ではなく成果物の生産なので、
エージェントを全力で使ってよい（別リポジトリ、別 CLAUDE.md）。
