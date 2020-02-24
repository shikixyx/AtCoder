import sys
sys.setrecursionlimit(10 ** 7)

N = input()

# TLE (Python3 3.4.3)
# AC  (PyPy3 (2.4.0)) 563 ms

# DP
INF = pow(10, 8)
L = len(N)
dp = [[INF] * 2 for _ in range(L+2)]
dp[0][0] = 0

# reverse
N = N[::-1] + '0'


for i in range(L+1):
    n = int(N[i])

    # 更新後のdp
    ni = i + 1

    # 前の桁で繰り下がりなし
    # 同じだけ払う
    dp[ni][0] = min(dp[ni][0], dp[i][0] + n)

    # 繰り下がりあり
    if n > 0:
        dp[ni][1] = min(dp[ni][1], dp[i][0] + (10 - n))
    else:
        dp[ni][0] = min(dp[ni][0], dp[i][0])

    # 前の桁で繰り下がりあり
    n += 1

    # 同じだけ払う
    if n == 10:
        dp[ni][1] = min(dp[ni][1], dp[i][1])
    else:
        dp[ni][0] = min(dp[ni][0], dp[i][1] + n)

    # 繰り下がりあり
    dp[ni][1] = min(dp[ni][1], dp[i][1] + (10 - n))


ans = min(dp[L+1][0], dp[L+1][1])

print(ans)
