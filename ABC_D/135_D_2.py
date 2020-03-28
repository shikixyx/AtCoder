import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 30min
# 桁DP
# pypy3

S = input()
S = S[::-1]
LS = len(S)

MOD = 10 ** 9 + 7


dp = [[0] * 13 for _ in range(LS+1)]
dp[0][0] = 1

for i in range(LS):
    if S[i] != '?':
        d = int(S[i])
        md = (d * pow(10, i, 13)) % 13

        if md == 0:
            dp[i + 1] = dp[i]
        else:
            dp[i + 1][md:] = dp[i][:-md]
            dp[i + 1][:md] = dp[i][-md:]
    else:
        t = pow(10, i, 13)
        for k in range(10):
            md = (k * t) % 13

            for j in range(13):
                nj = (j + md) % 13
                dp[i + 1][nj] += dp[i][j]
                dp[i + 1][nj] %= MOD

print(dp[LS][5])
