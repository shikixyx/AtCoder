import sys
import numpy as np

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10 ** 9 + 7

H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]

K = 0

NS = []
for r in range(H):
    N = []
    for c in range(W):
        if S[r][c] == "#":
            N.append(0)
        else:
            N.append(1)
            K += 1

    NS.append(N)

S = np.array(NS)

R_CNT = []
for r in range(H):
    row = S[r]

    tmp = np.arange(W)
    tmp[row > 0] = 0
    np.maximum.accumulate(tmp, out=tmp)
    left = tmp

    r_row = row[::-1]
    tmp = np.arange(W)
    tmp[r_row > 0] = 0
    np.maximum.accumulate(tmp, out=tmp)
    right = W - tmp[::-1] - 1

    y = right
    y -= left + 1
    y[row == 0] = 0

    R_CNT.append(y)

print(R_CNT)

C_CNT = []
for c in range(W):
    col = S[:, c]

    print(col)

    tmp = np.arange(H)
    tmp[col > 0] = 0
    np.maximum.accumulate(tmp, out=tmp)
    left = tmp

    r_col = col[::-1]
    tmp = np.arange(H)
    tmp[r_col > 0] = 0
    np.maximum.accumulate(tmp, out=tmp)
    right = H - tmp[::-1] - 1

    print(left, right)

    y = right
    y -= left + 1
    y[col == 0] = 0

    C_CNT.append(y)

print(C_CNT)


exit()


ans = 0
for r in range(H):
    for c in range(W):
        if S[r][c] == "#":
            continue

        cnt = R_CNT[r][c] + C_CNT[r][c] - 1

        t = pow(2, cnt, MOD) - 1
        t %= MOD
        t *= pow(2, K - cnt, MOD)
        t %= MOD

        ans += t
        ans %= MOD

print(ans)

