import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 桁DPで解いてみる

L = input()
N = len(L)
MOD = 10 ** 9 + 7

dp = [[0] * 2 for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    # a + b = 0 にするやり方
    if L[i] == '0':
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][1]
    elif L[i] == '1':
        #dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = (dp[i][0] + dp[i][1]) % MOD

    # a + b = 1 にするやり方
    if L[i] == '0':
        # 小さいやつから出ないとこれは作れない
        dp[i + 1][1] += dp[i][1] * 2 % MOD
        dp[i + 1][1] %= MOD
    elif L[i] == '1':
        dp[i + 1][0] += dp[i][0] * 2 % MOD
        dp[i + 1][0] %= MOD
        dp[i + 1][1] += dp[i][1] * 2 % MOD
        dp[i + 1][1] %= MOD

ans = (dp[N][0] + dp[N][1]) % MOD
print(ans)
