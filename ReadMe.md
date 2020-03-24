# 競プロ用

## Python

### 変数や関数に値を渡す場合すべて参照渡し

- [Python の値渡しと参照渡し](http://amacbee.hatenablog.com/entry/2016/12/07/004510)

```txt
渡された値を変更した際に元の値自体も変更されてしまうかどうかは，オブジェクトの型に依存します．

変更不可（Immutable）な型
int, float, str, tuple, bytes, frozenset 等
変更可能（Mutable）な型
list, dict, set, bytearray 等
変更可能な型では，渡された値が変更されると元の値も変更されてしまいます．（新しく領域が確保されません）
```

## 二分探索

- `bisect_left(A,x)`
  - x __より小さい__ 個数
  - x __以上__ の最初のindex
- `bisect_right(A,x)`
  - x __以下__ の個数
  - x __より大きい__ 最初のindex

## メモ

- 探索の基本は二分探索を使う
- 困難は分割せよ
- 10^5 以上のインプットは read する
- 構築問題は色々と試して、良い性質の物を見つける
  - 上限、下限も気にしてみる
