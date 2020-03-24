import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, input().split())
A = np.array(input().split(), np.int64)

A = np.sort(A)
zero = A[A == 0]
pos = A[A > 0]
neg = A[A < 0]


def test(x):
    cnt = 0

    if x >= 0:
        cnt += len(zero) * N

    cnt += np.searchsorted(A, x // pos, side='right').sum()
    cnt += (N - np.searchsorted(A, (-x - 1) // -neg, side='right')).sum()
    cnt -= np.count_nonzero(A * A <= x)

    cnt //= 2

    return K <= cnt


l = -(10 ** 19)  # NG
r = 10 ** 19  # OK

while l + 1 != r:
    mid = (l + r) // 2

    if test(mid):
        r = mid
    else:
        l = mid

print(r)
