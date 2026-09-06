---
id: 1
slug: two-sum
difficulty: Easy
topics: [junior, array, hash-table]
first_solved: 2026-10-05
attempts: 1
confidence: 1
---

## 問題
https://leetcode.com/problems/two-sum/description/

入力は、整数を格納する配列 `nums` と整数型の `target` 変数が与えられる。
出力は、`nums` の2つのインデックスを返して、その要素の合計が `target` の値になるようにする。
入力値は必ず1つの解が与えられて、同じ要素は1つしか使えない。

## アプローチ

* `nums` の配列を順番に評価する。
* `target` - n番目の要素 `nums[n]` の差分が `nums[n+1]` 以上の要素にあるかどうかを評価する。
* なければ `nums` の評価を+1する。

## 計算量

solve: Time: O(n²) / Space: O(n)
refactor: Time: O(n) / Space: O(n)

## なぜ最初に思いつかなかったか

1. ファイル冒頭に `from typing import List` をつけ忘れた
2. `nums[i+1:]` で配列で差分を探索する方式から、ハッシュマップを使って1回で探索する形式に更新した。
    * この記法をそもそも知らなかった
3. 計算量の書き方をそもそも間違っていた

## 類題