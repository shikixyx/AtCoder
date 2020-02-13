import sys
import bisect
sys.setrecursionlimit(10 ** 7)

# TLE

# Xor
# ビット毎に独立
# k-bit目を二分探索


N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(29):
    NA = [a % 2 ** (i + 1) for a in A]
    NB = [b % 2 ** (i + 1) for b in B]
    NB.sort()

    T = 2 ** i
    cnt = 0
    for a in NA:
        # [T-a,2T-a)
        ta1 = T - a
        ta2 = T * 2 - a
        i1 = bisect.bisect_left(NB, ta1)
        i2 = bisect.bisect_left(NB, ta2) - 1
        cnt += i2 - i1

        # [3T-a,4T-a)
        ta3 = T * 3 - a
        ta4 = T * 4 - a
        i3 = bisect.bisect_left(NB, ta3)
        i4 = bisect.bisect_left(NB, ta4) - 1
        cnt += i4 - i3

    if cnt % 2 == 1:
        ans += 2 ** i

print(ans)
