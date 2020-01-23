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

a, b, c = map(int, input().split())

r = a + b
r += c
if r >= 22:
    ans = 'bust'
else:
    ans = 'win'

print(ans)
