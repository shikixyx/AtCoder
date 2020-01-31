import sys
import bisect
import numpy as np
sys.setrecursionlimit(10 ** 7)

# 巨大ナップサック
# 半分全列挙


N, WM = map(int, input().split())
VW = [[int(x) for x in input().split()] for _ in range(N)]
V, W = zip(*VW)


# N <= 30
# 半分全列挙
def case1():
    h1 = N // 2
    h2 = N - h1
    S1 = 2 ** h1 - 1
    HALF1 = []
    S2 = 2 ** h2 - 1
    HALF2 = []
    for i in range(S1+1):
        v = 0
        w = 0
        n = 0
        while i > 0:
            if i & 1:
                v += VW[n][0]
                w += VW[n][1]
            i >>= 1
            n += 1

        if w > WM:
            continue
        HALF1.append((v, w))

    for i in range(S2+1):
        v = 0
        w = 0
        n = h1
        while i > 0:
            if i & 1:
                v += VW[n][0]
                w += VW[n][1]
            i >>= 1
            n += 1

        if w > WM:
            continue
        HALF2.append((v, w))

    HALF1.sort(key=lambda x: x[1])
    HALF2.sort(key=lambda x: x[1])

    def remove_ele(H):
        tmp = []
        p_v = -1
        for h in H:
            if h[0] > p_v:
                tmp.append(h)
                p_v = h[0]

        return tmp

    HALF1 = remove_ele(HALF1)
    HALF2 = remove_ele(HALF2)

    HALF3 = [x[1] for x in HALF2]

    ans = 0
    for v, w in HALF1:
        w2 = WM - w
        i = bisect.bisect_right(HALF3, w2) - 1
        ans = max(ans, v + HALF2[i][0])

    return ans


# w <= 10 ** 3
# DP
def case2():
    L = N * 10 ** 3 + 1
    # 重さwの時の価値の最大値
    dp = np.zeros(L, dtype=np.int64)

    for v, w in VW:
        dp[w:] = np.maximum(dp[w:], dp[:-w] + v)

    return max(dp[:WM+1])


# v <= 10 ** 3
# DP
def case3():
    L = N * 10 ** 3 + 1
    INF = 10 ** 18

    # 価値vの時の重さの最小値
    dp = np.zeros(L, dtype=np.int64)
    dp[1:] = INF

    for v, w in VW:
        # np.minimum は　２つのarrayを比較して最小を返す
        dp[v:] = np.minimum(dp[v:], dp[:-v] + w)

    dp = dp <= WM
    dp = dp.nonzero()

    return max(dp[0])


if N <= 30:
    ans = case1()
else:
    w = max(W)
    if w <= 1000:
        ans = case2()
    else:
        ans = case3()

print(ans)
