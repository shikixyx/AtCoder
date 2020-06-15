import sys
import numpy as np
from collections import Counter

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

VALID = np.ones((10 ** 6) + 10, dtype=np.bool)

A.sort()
C = Counter(A)

multi = []
for k, v in C.items():
    if v > 1:
        multi.append(k)

for x in multi:
    VALID[x::x] = False


ans = 0
for a in A:
    if VALID[a]:
        ans += 1
        VALID[a::a] = False

print(ans)
