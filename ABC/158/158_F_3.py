import sys
import bisect
from collections import deque
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N = int(readline())
MOD = 998244353

XD = [[int(x) for x in readline().split()] for _ in range(N)]
XD.sort()
#X = [x for x, _ in XD]

NXT = deque()
E = [[] for _ in range(N)]

for i in range(N - 1, -1, -1):
    x, d = XD[i]

    while NXT:
        j, nx = NXT.pop()

        if nx < x + d:
            E[i].append(j)
        else:
            NXT.append((j, nx))
            break

    NXT.append((i, x))


def dfs(i):
    rtn = 1
    for v in E[i]:
        rtn *= dfs(v)
        rtn %= MOD
    return rtn + 1


ans = 1
for i, x in NXT:
    ans *= dfs(i)
    ans %= MOD

print(ans % MOD)
