import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop
import math

# WA

#read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
C = []

for _ in range(N):
    x, y = map(int, input().split())
    C.append((x, y))

r_large = 800.
r_small = 0.
r = (r_large + r_small) / 2.

for _ in range(30):
    isValid = True
    r2 = (r * 2.)**2.
    for i in range(N):
        for j in range(N):
            l = (C[i][0] - C[j][0]) ** 2 + (C[i][1] - C[j][1]) ** 2
            if l > r2:
                isValid = False
                break

            nx, ny = (C[i][0]+C[j][0])/2., (C[i][1]+C[j][1])/2.

            for k in range(N):
                l2 = (C[k][0] - nx) ** 2 + (C[k][1] - ny) ** 2
                if l2 > r2:
                    isValid = False
                    break

        if not isValid:
            break

    if isValid:
        r_large = r
    else:
        r_small = r

    r = (r_large + r_small) / 2.

print(r)

#print(math.sqrt(lm) / 2.)
