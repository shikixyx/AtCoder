import numpy as np
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# TLE

S = input()
S = S[::-1]
LS = len(S)

MOD = 10 ** 9 + 7


dp = [np.zeros(13, dtype=np.int64) for _ in range(LS + 1)]
dp[0][0] = 1

for i in range(LS):
    #print("i == ", i, "S[i]==", S[i])
    # print(dp[i])
    if S[i] != '?':
        d = int(S[i])
        md = (d * pow(10, i, 13)) % 13

        if md == 0:
            dp[i + 1] = dp[i]
        else:
            dp[i + 1][md:] = dp[i][:-md]
            dp[i + 1][:md] = dp[i][-md:]
        dp[i + 1] %= MOD
    else:
        t = pow(10, i, 13)
        for k in range(10):
            md = (k * t) % 13

            if md == 0:
                dp[i + 1] += dp[i]
            else:
                dp[i + 1][md:] += dp[i][:-md]
                dp[i + 1][:md] += dp[i][-md:]
            dp[i + 1] %= MOD

#print("i == LS")
# print(dp[LS])
print(dp[LS][5])
