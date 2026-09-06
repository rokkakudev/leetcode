# leetcode

クラウド/プラットフォーム系ポジションの技術面接対策として LeetCode を解く訓練場。
詳細なルールは [CLAUDE.md](./CLAUDE.md) を参照。

## 構成

```
problems/   # {4桁ID}-{スラッグ} ごとの解法・振り返り
notes/      # パターン別の横断メモ
scripts/    # 雛形生成・索引生成ツール（問題数に応じて段階的に整備）
```

トピック別ディレクトリは作らない。トピックは各問題の frontmatter で管理する。

## 環境

- Python 3.14 / パッケージ管理は uv
- `python3` は直接叩かない（macOS system Python を踏むため）

```bash
uv run pytest
```

## 進捗

このセクションは `problems/` が増えたら `scripts/build_index.py` で自動生成する（50問時点）。
それまでは手動更新しない。
