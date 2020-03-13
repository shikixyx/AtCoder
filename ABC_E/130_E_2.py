import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

MOD = 10 ** 9 + 7

dp = [[0] * (M+1) for _ in range(N+1)]
dp_cum = [[0] * (M+1) for _ in range(N+1)]

for x in range(N):
    for y in range(M):
        if S[x] == T[y]:
            dp[x + 1][y + 1] += dp_cum[x][y] + 1
            dp[x + 1][y + 1] %= MOD

        dp_cum[x + 1][y + 1] = (dp_cum[x+1][y] % MOD) \
            + (dp_cum[x][y + 1] % MOD) \
            - (dp_cum[x][y] % MOD) \
            + (dp[x + 1][y + 1] % MOD)

        dp_cum[x + 1][y + 1] %= MOD

        #print("---x,y", x, y, "----")
        #print("dp:", dp)
        #print("dp_cum", dp_cum)


ans = dp_cum[N][M] + 1
print(ans)
