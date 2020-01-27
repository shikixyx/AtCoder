import sys
sys.setrecursionlimit(10 ** 7)

H, N = map(int, input().split())

A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[10**12] * (H+1) for _ in range(N+1)]

# dp[i][0]はコスト0
for i in range(N+1):
    dp[i][0] = 0

# i個の魔法
for i in range(N):
    # hの体力
    for h in range(H+1):
        # 最後に倒すとき
        if h == H:
            # 攻撃力がHを超える時
            if A[i] > H:
                dp[i+1][h] = min(dp[i][h], B[i])
            # 超えてない時
            else:
                m = min(dp[i+1][h-A[i]:h])
                dp[i+1][h] = min(dp[i][h], m + B[i])
        # 魔法の攻撃力が足らない
        elif h < A[i]:
            dp[i+1][h] = dp[i][h]
        # 通常時
        else:
            dp[i+1][h] = min(dp[i][h], dp[i+1][h-A[i]] + B[i])


print(dp[N][H])
