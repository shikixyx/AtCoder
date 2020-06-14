import sys
import numpy as np
import math

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
VW = [0] + [list(map(int, readline().split())) for _ in range(N)]

Q = int(readline())
ul = [list(map(int, readline().split())) for _ in range(Q)]

MID = int(math.sqrt(N))

cache = [None] * (N + 1)
S = 10 ** 5 + 10


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
for u, l in ul:
    q = []
    v = u
    while v != 1:
        q.append(v)
        v //= 2
    q.append(1)

    t = solve(q, l)
    ans.append(t)


print("\n".join(map(str, ans)))
