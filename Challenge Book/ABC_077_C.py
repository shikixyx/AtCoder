import numpy as np
import sys
import bisect
sys.setrecursionlimit(10 ** 7)

# 二分探索

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

cntB = [0] * (N+1)

# Cを超えないBの累積和
for i in range(N):
    b = bisect.bisect_right(C, B[i])
    cntB[i+1] = cntB[i] + N - b


ans = 0
for i in range(N):
    a = bisect.bisect_right(B, A[i])
    c = cntB[N] - cntB[a]
    ans += c

print(ans)
