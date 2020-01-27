import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop


sys.setrecursionlimit(10 ** 7)

H = int(input())

a = 0
h = H
while(h > 0):
    h = h // 2
    a += 1

ans = (1-2**a) * (-1)
print(ans)
