import sys

sys.setrecursionlimit(10 ** 7)

H, N = map(int, input().split())

MAGIC = []
for _ in range(N):
    a, b = map(int, input().split())
    MAGIC.append((a, b))

dp = [[10**20] * (20000) for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = 0


for i in range(N):
    for h in range(H+1):
        if h < MAGIC[i][0]:
            dp[i+1][h] = dp[i][h]
        elif h == H:
            m = min(dp[i+1][h-MAGIC[i][0]:])
            dp[i+1][h] = min(dp[i][h], m+MAGIC[i][1])
        else:
            dp[i+1][h] = min(dp[i][h], dp[i+1][h-MAGIC[i][0]]+MAGIC[i][1])


print(dp[N][H])
