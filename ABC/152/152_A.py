import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop


#read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
a = N - M
if N - M > 0:
    ans = 'No'
else:
    ans = 'Yes'

print(ans)
