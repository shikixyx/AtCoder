import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]


@lru_cache(maxsize=None)
def get_dist(u, v):
    a, b, c = XYZ[u]
    p, q, r = XYZ[v]

    d = abs(a - p) + abs(b - q) + max(0, r - c)
    return d


@lru_cache(maxsize=None)
def dfs(s, v):
    ## s が今の状態
    ## v は今いるところ

    if s == 1:
        return get_dist(0, v)

    t = 10 ** 10
    for i in range(1, N):
        if s & (1 << i):
            t = min(t, dfs(s & ~(1 << i), i) + get_dist(i, v))

    return t


ans = 10 ** 10
for i in range(1, N):
    ans = min(ans, dfs((1 << N) - 1, i) + get_dist(i, 0))


print(ans)

