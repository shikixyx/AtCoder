import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop
import itertools


# read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

A, B, X = map(int, input().split())

n = 10**9
m = n * A
m += len(str(n)) * B

if X >= m:
    print(10**9)
    exit()

n = 1
m = n * A
m += len(str(n)) * B

if X < m:
    print(0)
    exit()


big = 10 ** 9
sml = 1

while((big - sml) != 1):
    #print("big", big, "sml", sml)
    mdl = (big + sml) // 2
    m = mdl * A
    m += len(str(mdl)) * B

    if m > X:
        big = mdl
    else:
        sml = mdl

print(sml)


'''
x = X // A
x = X - len(str(x)) * B
x = x // A

if x >= (10**9 + 1):
    print(10**9)
    exit()
elif x < 0:
    print(0)
    exit()

ans = 1
m = A * x
m += B * (len(str(x)))


for a in range(x, 10**9):
    m = A * a
    d = len(str(a))
    m += B * d
    # print("x", x, "m", m)

    if m > X:
        ans = a-1
        break

print(ans)
'''
