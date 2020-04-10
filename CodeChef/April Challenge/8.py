from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Partial AC 10pt
# 愚直に回す

T = int(readline())

MOD = 10 ** 9 + 7


# [[素因数,数]]を出力
def fctr1(n):
    f = []
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f


def cnt(dic):
    cnt = 1
    for k, v in dic.items():
        if v == 0:
            continue
        cnt *= v + 1
        cnt %= MOD
    return cnt


def merge(s, factors, isPlus=True):
    for k, v in factors:
        if isPlus:
            s[k] += v
        else:
            s[k] -= v
    return s


def dfs(now, goal, PATH, A, parent, s, MEMO):
    if not MEMO[now]:
        a = A[now]
        MEMO[now] = fctr1(a)
    factors = MEMO[now]
    s = merge(s, factors)

    if now == goal:
        return True, s

    for v in PATH[now]:
        if v == parent:
            continue

        hasGoal, s = dfs(v, goal, PATH, A, now, s, MEMO)

        if hasGoal:
            return True, s

    s = merge(s, factors, False)

    return False, s


def solve():
    N = int(readline())
    PATH = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        x, y = map(int, readline().split())
        PATH[x].append(y)
        PATH[y].append(x)

    A = [-1] + list(map(int, readline().split()))
    Q = int(readline())
    UV = [[int(x) for x in readline().split()] for _ in range(Q)]

    MEMO = [None] * (N+1)

    ans = []
    for u, v in UV:
        _, s = dfs(u, v, PATH, A, -1, defaultdict(int), MEMO)
        ans.append(cnt(s))

    return '\n'.join(map(str, ans))


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
