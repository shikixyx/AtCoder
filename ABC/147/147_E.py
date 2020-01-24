
import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop
import itertools
import math
import copy


#read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())

A = []
B = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)

for _ in range(H):
    b = list(map(int, input().split()))
    B.append(b)

C = []
for i in range(H):
    cs = []
    for j in range(W):
        c = abs(A[i][j] - B[i][j])
        cs.append(c)

    C.append(cs)


def calc(arr):
    # print(arr)
    arr.sort(reverse=True)
    a = 0
    b = 0

    for i in range(len(arr)):
        if a > b:
            b += arr[i]
        else:
            a += arr[i]

    return abs(a-b)


def dfs(x, y, arr):
    # print(arr)
    arr.append(C[y][x])

    if x == W-1 and y == H-1:
        return calc(arr)

    xs = [0, 1]
    ys = [1, 0]

    mn = 10**4
    for i in range(2):
        if x+xs[i] <= W-1 and y+ys[i] <= H-1:
            arr2 = copy.copy(arr)
            a = dfs(x+xs[i], y+ys[i], arr2)

            if a < mn:
                mn = a

    return mn


ans = dfs(0, 0, [])
print(ans)
