import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

# Xor
# ビット毎に独立
# k-bit目を二分探索


N = int(input())

A = np.array(input().split(), dtype=np.int64)
B = np.array(input().split(), dtype=np.int64)


mask = 1

ans = 0
for i in range(29):
    NA = A & mask
    NB = B & mask
    NA.sort()
    NB.sort()

    T = 2 ** i
    x1, x2, x3 = [np.searchsorted(NB, t - NA).sum() for t in [T, 2 * T, 3 * T]]
    zero_cnt = x1 + (x3 - x2)
    if (N*N - zero_cnt) % 2 == 1:
        ans += 2 ** i

    mask = mask * 2 + 1

print(ans)
