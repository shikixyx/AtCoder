import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Partial AC[10pt]
# 累積和から求められるようにした
# SegTreeよりも遅い

# ref. [https://qiita.com/Pro_ktmr/items/4e1e051ea0561772afa3]

T = int(readline())

MOD = 10 ** 9 + 7


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


def unmerge(s, factors):
    ret = {}
    for k, v in s.items():
        ret[k] = v
    for k, v in factors.items():
        ret[k] -= v

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
def HLD(u, parent, root, TOP, PATH, s, F, order,  A):
    stack = [(u, parent, root)]
    N = len(s) - 1
    used = [False] * (len(s))
    idx = 1

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


def query_range(F, ACCUM_F, l, r):
    left = ACCUM_F[l]
    right = ACCUM_F[r]
    ret = unmerge(right, left)
    ret = merge(ret, F[l])
    return ret


def query(u, v, F, ACCUM_F, order, TOP, DPT, parents, MEMO, N):
    ret = {}
    while TOP[u] != TOP[v]:
        if depth(TOP[u], DPT, parents) <= depth(TOP[v], DPT, parents):
            l = order[TOP[v]]
            r = order[v]
            if not MEMO[l][r]:
                MEMO[l][r] = query_range(F, ACCUM_F, l, r)
            q = MEMO[l][r]
            ret = merge(ret, q)
            v = parents[TOP[v]]
        else:
            l = order[TOP[u]]
            r = order[u]
            if not MEMO[l][r]:
                MEMO[l][r] = query_range(F, ACCUM_F, l, r)
            q = MEMO[l][r]
            ret = merge(ret, q)
            u = parents[TOP[u]]

    l = min(order[u], order[v])
    r = max(order[u], order[v])
    if not MEMO[l][r]:
        MEMO[l][r] = query_range(F, ACCUM_F, l, r)
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
    s = [0] * (N + 1)
    F = [{}] * (N + 1)
    order = [None] * (N+1)
    parents = [None] * (N+1)
    prepareHLD(1, -1, PATH, s, A, parents)

    # Heavy-Light Decomposition
    TOP = [-1] * (N+1)  # most small depth num
    HLD(1, -1, 1, TOP, PATH, s, F, order, A)

    order_inv = {a: i for i, a in enumerate(order)}

    ACCUM_F = [{}] * (N + 1)
    t = {}
    prev = -1
    for i in range(1, N + 1):
        u = order_inv[i]
        if TOP[u] != prev:
            t = F[i]
        else:
            t = merge(F[i], t)

        prev = TOP[u]
        ACCUM_F[i] = t

    # Query
    DPT = [None] * (N + 1)
    MEMO = [[None] * (N + 1) for _ in range(N+1)]

    ans = []
    for u, v in UV:
        ret = query(u, v, F, ACCUM_F, order, TOP, DPT, parents, MEMO, N)
        ans.append(cnt(ret))

    return '\n'.join(map(str, ans))


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
