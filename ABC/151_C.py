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

acs = 0
wro = 0

PROB = [0] * N
WRON = [0] * N

for _ in range(M):
    p, s = input().split()
    p = int(p) - 1

    if PROB[p] == 1:
        continue

    if s == 'AC':
        PROB[p] = 1
        acs += 1
    elif s == 'WA':
        WRON[p] += 1

for i in range(N):
    if PROB[i] == 1:
        wro += WRON[i]

print(str(acs)+" "+str(wro))
