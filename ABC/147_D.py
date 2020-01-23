import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop
import itertools

N = int(input())
A = np.array(input().split(), np.int64)

MOD = 10**9 + 7

ans = 0
for i in range(64):
    B = (A >> i) & 1
    x = np.count_nonzero(B)
    y = N - x
    x *= y

    for _ in range(i):
        x *= 2
        x %= MOD

    ans += x
ans %= MOD
print(ans)
