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

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)
b = N*M - s

if b > K:
    print("-1")
    exit()
elif b < 0:
    b = 0

print(b)
