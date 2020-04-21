import numpy as np
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))
ACM = np.cumsum(A)


# A1 ... AnのBIT(1-indexed)
BIT = [0]*(N+1)


# A1 ~ Aiまでの和 O(logN)
def BIT_query(idx):
    res_sum = 0
    while idx > 0:
        res_sum += BIT[idx]
        idx -= idx & (-idx)
    return res_sum


# Ai += x O(logN)
def BIT_update(idx, x):
    while idx <= N:
        BIT[idx] += x
        idx += idx & (-idx)
    return


i_to_a = [[a, -i] for i, a in enumerate(A)]
i_to_a.sort(reverse=True)

ans = 0
l = 0
r = N-1

for a, i in i_to_a:
    i = -i
    left = ACM[i] - a
    left -= BIT_query(i+1)
    left += a * abs(i - l)

    right = ACM[N - 1] - ACM[i]
    right -= BIT_query(N) - BIT_query(i + 1)
    right += a * abs(r - i)

    if right < left:
        ans += a * abs(i - l)
        BIT_update(l+1, a)
        l += 1
    else:
        ans += a * abs(r - i)
        BIT_update(r+1, a)
        r -= 1

print(ans)
