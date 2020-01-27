import sys

sys.setrecursionlimit(10 ** 7)

H, N = map(int, input().split())

MAGIC = []
for _ in range(N):
    a, b = map(int, input().split())
    MAGIC.append((a, b))

INF = 10 ** 10
dp = [INF] * 20000
dp[0] = 0

for i in range(N):
    for h in range(H):
        a, b = MAGIC[i]

        if dp[h+a] > (dp[h] + b):
            dp[h+a] = dp[h] + b

print(min(dp[H:]))
