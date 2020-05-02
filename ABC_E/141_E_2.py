import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 文字列アルゴリズム
# Z-Algorithm
# ZAlgorithm

# AC
# 753ms PyPy

N = int(input())
S = list(input())

ans = 0


def Z_Algorithm(S):
    L = len(S)
    Z = [0] * L
    Z[0] = L

    i = 1
    j = 0

    while i < L:
        # 同じなら引き伸ばす
        # 前回のjを引き継ぐ
        while i + j < L and S[j] == S[i + j]:
            j += 1
        Z[i] = j

        # j = 0なら次
        if j == 0:
            i += 1
            continue

        # 同じ数字分横にずらす
        # 右にそれ以上の文字があればcontinue
        k = 1
        while k < j and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1

        i += k
        j -= k

    return Z


ans = 0
for i in range(N):
    Z = Z_Algorithm(S[i:])

    L = len(Z)
    for j in range(1, L):
        l = min(Z[j], j)
        ans = max(l, ans)

print(ans)
