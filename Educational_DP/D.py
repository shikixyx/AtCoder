import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, W = map(int, input().split())

WV = [[int(x) for x in input().split()] for _ in range(N)]

dp = [np.zeros(W*2 + 10, dtype=np.int64) for _ in range(N+1)]

for i in range(N):
    w, v = WV[i]
    dp[i + 1][w:] = np.maximum(dp[i][w:], dp[i][:-w] + v)
    dp[i + 1][:w] = np.maximum(dp[i][:w], dp[i+1][:w])
    # print(dp[i+1])

# print(dp)
ans = dp[N][W]

print(ans)
