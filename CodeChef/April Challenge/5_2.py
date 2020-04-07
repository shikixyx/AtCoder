import math
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())

# TLE


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


def solve():
    DEBUG = False
    N = int(readline())
    A = list(map(int, readline().split()))
    A += [-1]

    INF = 10 ** 6

    cnt = 0
    EVEN = SegmentTree(N+10, min, INF)
    FOUR = SegmentTree(N+10, min, INF)

    # only odd
    odd_cnt = 0
    for i in range(N+1):
        a = A[i]

        if a == -1:
            cnt += odd_cnt * (odd_cnt + 1) // 2
            break

        if a % 2 == 0:
            EVEN.update(i, i)
            if a % 4 == 0:
                FOUR.update(i, i)
            cnt += odd_cnt * (odd_cnt + 1) // 2
            odd_cnt = 0
        else:
            odd_cnt += 1

    for i in range(N):
        a = A[i]

        # odd
        # two Even or one Four
        if a % 2 == 1:
            # two Even
            nxt1 = EVEN.query(i + 1, N)
            nxt2 = EVEN.query(nxt1 + 1, N)

            # four
            nxt4 = FOUR.query(i + 1, N)

            idx = min(nxt2, nxt4)
            if idx == INF:
                continue

            cnt += N - idx
        # div by four
        elif a % 4 == 0:
            # any will do
            cnt += N - i
        # even
        else:
            # next even
            nxt = EVEN.query(i + 1, N)

            if nxt == INF:
                continue
            cnt += N - nxt

    return cnt


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
