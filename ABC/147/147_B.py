
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


S = input()
l = len(S) - 1
h = len(S) // 2
ans = 0

for i in range(h):
    if S[i] == S[l-i]:
        continue

    ans += 1

print(ans)
