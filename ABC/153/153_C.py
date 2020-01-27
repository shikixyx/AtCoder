import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop


sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort(reverse=True)

if N == K:
    print(0)
else:
    a = sum(H[K:])
    print(a)
