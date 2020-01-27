import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop


sys.setrecursionlimit(10 ** 7)

H, N = map(int, input().split())
A = list(map(int, input().split()))

a = sum(A)

if a >= H:
    print('Yes')
else:
    print('No')
