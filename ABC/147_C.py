import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop
import itertools


#read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = [[] for _ in range(N)]

for i in range(N):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        A[i].append((x-1, y))

seq = (0, 1)

# print(A)

ans = 0
for pos in itertools.product(seq, repeat=N):
    # print(pos)
    isValid = True
    for i in range(N):
        if pos[i] == 0:
            continue

        for prop in A[i]:
            #print("i", i, prop)
            x, y = prop
            if pos[x] == y:
                continue
            else:
                isValid = False
                break

        if not isValid:
            break

    if isValid:
        a = sum(pos)
        if a > ans:
            ans = a


print(ans)
