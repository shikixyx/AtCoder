# 競プロ用

## Python

### 変数や関数に値を渡す場合すべて参照渡し

- [Pythonの値渡しと参照渡し](http://amacbee.hatenablog.com/entry/2016/12/07/004510)

```c.f.txt
渡された値を変更した際に元の値自体も変更されてしまうかどうかは，オブジェクトの型に依存します．

変更不可（Immutable）な型
int, float, str, tuple, bytes, frozenset 等
変更可能（Mutable）な型
list, dict, set, bytearray 等
変更可能な型では，渡された値が変更されると元の値も変更されてしまいます．（新しく領域が確保されません）
```

## メモ

- 探索の基本は二分探索を使う
- 困難は分割せよ
- 10^5 以上のインプットはreadする
