import sys
import bisect
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# WA
# 倒せる最大を求めた


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


N = int(readline())
MOD = 998244353

XD = [[int(x) for x in readline().split()] for _ in range(N)]
XD.sort()
X = [x for x, _ in XD]

B = [bisect.bisect_left(X, x + d) for x, d in XD] + [0]
seg = SegmentTree(N+1, max, 0, B)
#seg.update(N, N)

# print(X)
# print(B)
CNT = [0] * (N)
for i in range(N-1, -1, -1):
    m = seg.query(i, B[i])
    c = max(B[i], m)
    CNT[i] = c - i
    seg.update(i, c)


# print(CNT)
print(0)
exit()

s = 0
for c in CNT:
    m = pow(2, c - 1, MOD) - 1
    m %= MOD
    s += m
    s %= MOD

al = pow(2, N, MOD)
ans = al - s
ans %= MOD

print(ans)
