import sys
import math
sys.setrecursionlimit(10 ** 7)

# 桁DP
# 非再帰

S = input()
K = int(input())
N = len(S)

# dp[n桁目まで決まってる][Non-Zeroの個数][Nと一致? 0:一致している 1:一致していない]
dp = [[[0] * 2 for _ in range(4)] for _ in range(N + 1)]

# n=0 桁目の値は、0として、それはKの値には関係なく、Nと一致している
dp[0][0][0] = 1

# i,j,kのうち、小さい方から埋めていく
for i in range(N):
    for j in range(4):
        for k in range(2):
            # 今決めようとしているの桁の値
            d = int(S[i])

            # 次の桁の値のループ(0-9)
            for nextd in range(10):
                # 次の桁を決めたあとのj,k
                nextj = j
                nextk = k

                # 次の桁がNon-Zero
                if nextd != 0:
                    nextj += 1
                # K個を超えたらいらない
                if nextj > K:
                    continue

                # 前の桁までNと一致していた場合
                # 使える数に制限あり
                if k == 0:
                    if d < nextd:
                        continue
                    elif nextd < d:
                        nextk = 1

                        # 前までの個数と同じ分の場合の数
                dp[i + 1][nextj][nextk] += dp[i][j][k]


ans = dp[N][K][0] + dp[N][K][1]
print(ans)
