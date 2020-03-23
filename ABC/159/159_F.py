import numpy as np
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 998244353

N, S = map(int, input().split())
A = list(map(int, input().split()))


dp = [np.zeros(S + 10, dtype=np.int64) for _ in range(N+1)]
#dp[0][0] = 1

# print(dp[0])
ans = 0
for i in range(N):
    a = A[i]

    dp[i][0] += 1
    dp[i + 1] += dp[i]
    dp[i + 1] %= MOD

    # a足す
    dp[i + 1][a:] += dp[i][:-a]
    dp[i + 1] %= MOD

    #print(dp[i + 1])
    ans += dp[i + 1][S]
    ans %= MOD

print(ans)
