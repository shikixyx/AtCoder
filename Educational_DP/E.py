import numpy as np
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, W = map(int, input().split())
WV = [[int(x) for x in input().split()] for _ in range(N)]

INF = 10 ** 12
dp = [np.ones(10 ** 5 + 10, dtype=np.int64)*INF for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    w, v = WV[i]
    dp[i + 1][v:] = np.minimum(dp[i][v:], dp[i][:-v] + w)
    dp[i + 1][:v] = np.minimum(dp[i][:v], dp[i + 1][:v])

    # print(dp[i+1][:20])

r = dp[N]
ans = np.where(r <= W)[0].max()

print(ans)
