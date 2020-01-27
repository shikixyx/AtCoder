import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop


sys.setrecursionlimit(10 ** 7)

A, B = map(int, input().split())

if (A % B) == 0:
    a = A // B
else:
    a = (A//B)+1

print(a)
