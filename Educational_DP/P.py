import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# TLE

N = int(readline())
PATH = [[] for _ in range(N + 1)]
MOD = 10 ** 9 + 7

for _ in range(N - 1):
    x, y = map(int, readline().split())
    PATH[x].append(y)
    PATH[y].append(x)


dp = [[1] * 2 for _ in range(N+1)]


def dfs(x, parent):
    for v in PATH[x]:
        if v == parent:
            continue
        dfs(v, x)

        dp[x][0] *= (dp[v][0] + dp[v][1])
        dp[x][0] %= MOD
        dp[x][1] *= dp[v][0]
        dp[x][1] %= MOD

    return 0


'''
@lru_cache(maxsize=None)
def dfs(x, parent, isBlack=True):
    ret = 1
    for v in PATH[x]:
        if v == parent:
            continue

        cnt = dfs(v, x, False)

        if not isBlack:
            cnt += dfs(v, x, True)

        ret *= cnt
        ret %= MOD

    ret %= MOD
    return ret
'''

dfs(1, -1)
ans = sum(dp[1])
ans %= MOD
print(ans)
