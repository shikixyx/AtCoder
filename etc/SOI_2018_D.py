import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)


N, M, S, T = map(int, input().split())
PATH = [[] for _ in range(N+1)]


for _ in range(M):
    u, v, a, b = map(int, input().split())
    PATH[u].append((v, a, b))
    PATH[v].append((u, a, b))

INF = 10 ** 15

da = [INF] * (N+1)
db = [INF] * (N+1)

usedA = [False] * (N+1)
usedB = [False] * (N+1)

da[S] = 0
for _ in range(N+2):
    d = -1
    v = -1
    for i in range(1, N+1):
        if not usedA[i]:
            if d == -1 or da[i] < d:
                v = i
                d = da[i]

    if d == -1:
        break

    usedA[v] = True

    for u, a, _ in PATH[v]:
        da[u] = min(da[u], da[v]+a)

db[T] = 0
for _ in range(N+2):
    d = -1
    v = -1
    for i in range(1, N+1):
        if not usedB[i]:
            if d == -1 or db[i] < d:
                v = i
                d = db[i]

    if d == -1:
        break

    usedB[v] = True

    for u, _, b in PATH[v]:
        db[u] = min(db[u], db[v]+b)

dist = [(i, da[i]+db[i]) for i in range(1, N+1)]
dist.sort(key=lambda x: x[1])
idx = 0

for i in range(N):
    while(dist[idx][0] <= i):
        idx += 1

    print(10**15 - dist[idx][1])
