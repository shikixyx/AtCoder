import sys
import numpy as np
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 愚直解
# TLE

N = int(readline())
VW = [0] + [list(map(int, readline().split())) for _ in range(N)]

Q = int(readline())
ul = [list(map(int, readline().split())) for _ in range(Q)]

ul_s = sorted(ul, reverse=True)

cache = [None] * (N + 1)
S = 10 ** 5 + 10
TABLE = defaultdict(int)


def solve(q, l):
    q = q[::-1]

    mi = -1
    for i in range(len(q)):
        x = q[i]
        if type(cache[x]) is np.ndarray:
            mi = i
        else:
            break

    x = q[mi]
    dp = cache[x] if mi != -1 else np.zeros(S, dtype=np.int64)

    q = q[mi + 1 :] if mi != -1 else q
    ans = calc(q, l, dp)
    return ans


def calc(q, l, dp):

    for u in q:
        v, w = VW[u]
        tmp = np.zeros(S, dtype=np.int64)
        tmp[w:] = dp[:-w] + v

        dp = np.maximum(dp, tmp)
        # cache[u] = np.copy(dp)
        cache[u] = dp

    return max(dp[: l + 1])


ans = []
for u, l in ul_s:
    q = []
    v = u
    while v != 1:
        q.append(v)
        v //= 2
    q.append(1)

    t = solve(q, l)
    TABLE[(u, l)] = t

for u, l in ul:
    ans.append(TABLE[(u, l)])


print("\n".join(map(str, ans)))
