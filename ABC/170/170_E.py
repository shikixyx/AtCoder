import sys
import heapq

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, Q = map(int, readline().split())
AB = [list(map(int, readline().split())) for _ in range(N)]
QUERY = [list(map(int, readline().split())) for _ in range(Q)]


class SegmentTree:
    """
    引数：
        N: 処理する区間の長さ
        operator: モノイド演算 (max, min, __add__,ラムダ式,関数定義など)
        UNIT: 単位元
        a: 長さNの配列 a で初期化（a を与えない場合、単位元で初期化）
    注意: 内部的には 1-indexed
    """

    def __init__(self, N, operator, unit, a=None):
        self.op = operator
        self.UNIT = unit

        self.N0 = 2 ** (N - 1).bit_length()
        self.tree = [self.UNIT] * (2 * self.N0)
        if a != None:
            self.tree[self.N0 : self.N0 + N] = a[:]
            for k in range(self.N0 - 1, 0, -1):
                self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    # a_k の値を x に更新
    def update(self, k, x):
        k += self.N0
        self.tree[k] = x
        k //= 2
        while k:
            self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])
            k //= 2

    # 区間[l,r)をopでまとめる
    def query(self, l, r):
        L = l + self.N0
        R = r + self.N0
        s = self.UNIT
        while L < R:
            if R & 1:
                R -= 1
                s = self.op(self.tree[R], s)
            if L & 1:
                s = self.op(s, self.tree[L])
                L += 1
            L >>= 1
            R >>= 1
        return s

    def get(self, k):  # k番目の値を取得。query[k,k]と同じ
        return self.tree[k + self.N0]

    def all(self):
        return self.tree[1]


PLACE = [[] for _ in range(2 * (10 ** 5) + 10)]
CHILD = [0] * (N + 1)

for i, x in enumerate(AB, 1):
    a, b = x[0], x[1]
    heapq.heappush(PLACE[b], [-a, i])
    CHILD[i] = b

# セグ木作る
T = []

for i in range(2 * (10 ** 5) + 1):
    if PLACE[i]:
        x = -PLACE[i][0][0]
        T.append(x)
    else:
        T.append(10 ** 10)

SEG = SegmentTree(2 * (10 ** 5) + 1, min, 10 ** 10, T)


# クエリの処理

ANS = []
for n, to in QUERY:
    # 所属を変更
    f = CHILD[n]
    CHILD[n] = to

    # 元いた
    while PLACE[f]:
        # 最大値のやつをみる
        if CHILD[PLACE[f][0][1]] != f:
            heapq.heappop(PLACE[f])
        else:
            break

    if PLACE[f]:
        f_mx = -PLACE[f][0][0]
    else:
        f_mx = 10 ** 10

    SEG.update(f, f_mx)

    # 行った先
    a, b = AB[n - 1]
    heapq.heappush(PLACE[to], [-a, n])
    to_mx = -PLACE[to][0][0]
    SEG.update(to, to_mx)

    ANS.append(SEG.all())

print("\n".join(map(str, ANS)))
