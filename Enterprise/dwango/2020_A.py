import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappop, heappush

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

M = int(input())
PList = [""] * M
Num = [0] * M

for i in range(M):
    s, t = input().split()
    t = int(t)
    PList[i] = s
    Num[i] = t

X = input()
x = PList.index(X)

print(sum(Num[x+1:]))
