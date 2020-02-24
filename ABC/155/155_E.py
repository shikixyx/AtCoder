import sys
sys.setrecursionlimit(10 ** 7)

N = input()

# TLE (Python3 3.4.3)
# AC  (PyPy3 (2.4.0)) 1147 ms

# DP
INF = pow(10, 8)
L = len(N)
dp = [[INF] * 2 for _ in range(L+2)]
dp[0][0] = 0

# reverse
N = N[::-1] + '0'


for i in range(L+1):
    for j in range(2):
        # 繰り下がりも加味
        n = int(N[i])
        n += j

        # 更新後のdp
        ni = i + 1

        # 10通りから探索
        for a in range(10):
            nj = 0
            b = a - n

            # 繰り下がりあり
            if b < 0:
                b += 10
                nj = 1

            dp[ni][nj] = min(dp[i][j] + a + b, dp[ni][nj])

print(dp)
ans = min(dp[L+1][0], dp[L+1][1])

print(ans)
