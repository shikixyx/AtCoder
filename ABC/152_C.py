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

N = int(input())
A = list(map(int, input().split()))

mn = N+1
cnt = 0
for i in range(N):
    #print(i, mn, cnt)
    a = A[i]

    if a < mn:
        mn = a
        cnt += 1

print(cnt)
