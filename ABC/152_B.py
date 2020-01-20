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

a, b = map(int, input().split())


big = 0
small = 0

if a > b:
    big = a
    small = b
else:
    big = b
    small = a

ans = [str(small)] * big
ans = ''.join(ans)

print(ans)
