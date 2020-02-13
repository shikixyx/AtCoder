import sys
sys.setrecursionlimit(10 ** 7)

# segment tree
# セグメント木


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

        self.N0 = 2**(N-1).bit_length()
        self.tree = [self.UNIT]*(2*self.N0)
        if a != None:
            self.tree[self.N0:self.N0+N] = a[:]
            for k in range(self.N0-1, 0, -1):
                self.tree[k] = self.op(self.tree[2*k], self.tree[2*k+1])

    # a_k の値を x に更新
    def update(self, k, x):
        k += self.N0
        self.tree[k] = x
        k //= 2
        while k:
            self.tree[k] = self.op(self.tree[2*k], self.tree[2*k+1])
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


N, M = map(int, input().split())
QUERY = [[f(x) for f, x in zip([int, float, float], input().split())]
         for _ in range(M)]

x_to_i = {x: i for i, x in enumerate(sorted(set(x for x, _, _ in QUERY)))}
l = len(x_to_i)
#l = 1 << 17
arr = [(1, 0)] * l
# seg = SegmentTree(arr, segfunc=lambda x, y: (
#    x[0] * y[0], x[1] * y[0] + y[1]), ide_ele = (1., 0.))
seg = SegmentTree(l, lambda x, y: (x[0] * y[0], x[1] * y[0] + y[1]), (1, 0))


min_val = 1
max_val = 1
for p, a, b in QUERY:
    seg.update(x_to_i[p], (a, b))
    na, nb = seg.query(0, l-1)
    #na, nb = seg.tree[1]
    x = na + nb

    if x < min_val:
        min_val = x
    if max_val < x:
        max_val = x

print(min_val)
print(max_val)
