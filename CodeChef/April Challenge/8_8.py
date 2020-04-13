import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Partial AC [40pt]
# 非再帰化
# default dictを取り除く(pypyだと遅い)
# pypyでもRE出なくなる

# 初期化を速くする

# ref. [https://qiita.com/Pro_ktmr/items/4e1e051ea0561772afa3]

T = int(readline())

MOD = 10 ** 9 + 7


class SegmentTree:
    '''
    初期化処理
    f : SegmentTreeにのせるモノイド
    default : fに対する単位元

    親      = i // 2
    左側の子 = i * 2
    右側の子 = i * 2 + 1
    注意)1-indexで実装
    '''

    def __init__(self, size, f=lambda x, y: x+y, default=0):
        self.size = 2**(size-1).bit_length()  # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2)  # 要素を単位元で初期化
        self.f = f

    # 未確認
    def setArr(self, arr):
        L = len(arr)
        self.dat[self.size:self.size+L] = arr

        for i in range(self.size - 1, 0, -1):
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                # モノイドでは可換律は保証されていないので演算の方向に注意
                rres = self.f(self.dat[r], rres)
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res

# {素因数:数}を出力


def fctr_dic(n):
    f = {}
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
    ret = {}
    for dic in [s, factors]:
        for k, v in dic.items():
            if k in ret:
                ret[k] += v
            else:
                ret[k] = v
    return ret


# Prepare To Heavy-Light Decomposition
# get Child Element Amount and Parent

def prepareHLD(u, root, PATH, s, A, parents):
    stack = [(u, root)]
    order = []
    N = len(s) - 1
    used = [False] * (N+1)

    while stack:
        x, root = stack.pop()
        order.append(x)

        # child
        s[x] += 1
        parents[x] = root

        for v in PATH[x]:
            if v == parents[x] or used[v]:
                continue

            stack.append((v, x))
            used[v] = True

    L = len(order)
    for i in range(L - 1, -1, -1):
        x = order[i]
        p = parents[x]

        if p != -1:
            s[p] += s[x]

    return


# Heavy-Light Decomposition
def HLD(u, parent, root, TOP, PATH, s, F, order, A):
    stack = [(u, parent, root)]
    used = [False] * (len(s))
    idx = 0

    while stack:
        u, parent, root = stack.pop()

        TOP[u] = root

        order[u] = idx
        factors = fctr_dic(A[u])
        F[idx] = factors

        idx += 1

        if s[u] == 1:
            continue

        M = 0
        nxt = -1

        for v in PATH[u]:
            if v == parent:
                continue

            if M < s[v]:
                M = s[v]
                nxt = v

        for v in PATH[u]:
            if v == parent or v == nxt or used[v]:
                continue

            stack.append((v, u, v))
            used[v] = True

        stack.append((nxt, u, root))

    return


def depth(u, DPT, parents):
    if DPT[u]:
        return DPT[u]
    if u == 1:
        return 0

    DPT[u] = depth(parents[u], DPT, parents) + 1

    return DPT[u]


def query(u, v, seg, order, TOP, DPT, parents, MEMO):
    ret = {}
    while TOP[u] != TOP[v]:
        if depth(TOP[u], DPT, parents) <= depth(TOP[v], DPT, parents):
            l = order[TOP[v]]
            r = order[v] + 1
            if not MEMO[l][r]:
                MEMO[l][r] = seg.query(l, r)
            q = MEMO[l][r]
            ret = merge(ret, q)
            v = parents[TOP[v]]
        else:
            l = order[TOP[u]]
            r = order[u] + 1
            if not MEMO[l][r]:
                MEMO[l][r] = seg.query(l, r)
            q = MEMO[l][r]
            ret = merge(ret, q)
            u = parents[TOP[u]]

    l = min(order[u], order[v])
    r = max(order[u], order[v]) + 1
    if not MEMO[l][r]:
        MEMO[l][r] = seg.query(l, r)
    q = MEMO[l][r]
    ret = merge(ret, q)

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
    seg = SegmentTree(N, merge, {})
    order = [None] * (N+1)
    parents = [None] * (N+1)
    prepareHLD(1, -1, PATH, s, A, parents)

    # Heavy-Light Decomposition
    TOP = [-1] * (N + 1)  # most small depth num
    F = [None] * N
    HLD(1, -1, 1, TOP, PATH, s, F, order, A)
    seg.setArr(F)

    # Query
    DPT = [None] * (N + 1)
    MEMO = [[None] * (N + 1) for _ in range(N+1)]

    ans = [cnt(query(u, v, seg, order, TOP, DPT, parents, MEMO))
           for u, v in UV]

    return '\n'.join(map(str, ans))


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
