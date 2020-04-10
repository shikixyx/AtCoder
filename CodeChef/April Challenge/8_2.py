from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Partial AC[10pt]
# HL分解
# 毎回segtreeに問合せ


# ref. [https://qiita.com/Pro_ktmr/items/4e1e051ea0561772afa3]

T = int(readline())

MOD = 10 ** 9 + 7


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


# {素因数:数}を出力
def fctr_dic(n):
    f = defaultdict(int)
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f[i] = c
            c = 0
    if n != 1:
        f[n] = 1
    return f


# 答えを出力
def cnt(dic):
    cnt = 1
    for k, v in dic.items():
        if v == 0:
            continue
        cnt *= v + 1
        cnt %= MOD
    return cnt


# 因子をmerge
def merge(s, factors):
    ret = defaultdict(int)
    for dic in [s, factors]:
        for k, v in dic.items():
            ret[k] += v
    return ret


# Prepare To Heavy-Light Decomposition
# get Child Element Amount and Parent

def prepareHLD(u, root, PATH, s,  A, parents):
    # child
    s[u] += 1
    parents[u] = root

    for v in PATH[u]:
        if v == root:
            continue

        s[u] += prepareHLD(v, u, PATH, s,  A, parents)

    return s[u]


# Heavy-Light Decomposition
def HLD(u, parent, root, TOP, PATH, s, seg, order, idx, A):
    TOP[u] = root

    order[u] = idx
    factors = fctr_dic(A[u])
    seg.update(idx, factors)

    idx += 1

    if s[u] == 1:
        return idx

    M = 0
    nxt = -1

    for v in PATH[u]:
        if v == parent:
            continue

        if M < s[v]:
            M = s[v]
            nxt = v

    idx = HLD(nxt, u, root, TOP, PATH, s, seg, order, idx, A)

    for v in PATH[u]:
        if v == parent or v == nxt:
            continue

        idx = HLD(v, u, v, TOP, PATH, s, seg, order, idx, A)

    return idx


def depth(u, DPT, parents):
    if DPT[u]:
        return DPT[u]
    if u == 1:
        return 0

    DPT[u] = depth(parents[u], DPT, parents) + 1

    return DPT[u]


def query(u, v, seg, order, TOP, DPT, parents):
    ret = defaultdict(int)
    while TOP[u] != TOP[v]:
        if depth(TOP[u], DPT, parents) <= depth(TOP[v], DPT, parents):
            q = seg.query(order[TOP[v]], order[v]+1)
            ret = merge(ret, q)
            v = parents[TOP[v]]
        else:
            q = seg.query(order[TOP[u]], order[u] + 1)
            ret = merge(ret, q)
            u = parents[TOP[u]]

    ret = merge(ret, seg.query(
        min(order[u], order[v]), max(order[u], order[v]) + 1))

    return ret


def solve():
    # Get INPUT
    N = int(readline())
    PATH = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        x, y = map(int, readline().split())
        PATH[x].append(y)
        PATH[y].append(x)

    # Get Query
    A = [-1] + list(map(int, readline().split()))
    Q = int(readline())
    UV = [[int(x) for x in readline().split()] for _ in range(Q)]

    # Prepare To Heavy-Light Decomposition
    s = [0] * (N+1)
    seg = SegmentTree(N, merge, defaultdict(int))
    order = [None] * (N+1)
    parents = [None] * (N+1)
    prepareHLD(1, -1, PATH, s, A, parents)

    # Heavy-Light Decomposition
    TOP = [-1] * (N+1)  # most small depth num
    HLD(1, -1, 1, TOP, PATH, s, seg, order, 0, A)

    # Query
    DPT = [None] * (N + 1)

    ans = []
    for u, v in UV:
        ret = query(u, v, seg, order, TOP, DPT, parents)
        ans.append(cnt(ret))

    return '\n'.join(map(str, ans))


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
