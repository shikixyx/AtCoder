import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappop, heappush

# ダイクストラ法
# dijkstra

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


def dijkstra(s, mode):
    INF = 10 ** 15
    dist = [INF] * (N+1)
    dist[s] = 0
    que = [(0, s)]

    while que:
        d, v = heappop(que)
        if dist[v] < d:
            continue

        for u, *a in PATH[v]:
            dv = d + a[mode]

            if dv < dist[u]:
                dist[u] = dv
                heappush(que, (dv, u))

    return dist


da = dijkstra(S, 0)
db = dijkstra(T, 1)

score = [10**15 - (da[i]+db[i]) for i in range(1, N+1)]

ans = [10**15] * N
ans[-1] = score[-1]

for i in range(N-2, -1, -1):
    ans[i] = max(ans[i+1], score[i])

for i in range(N):
    print(ans[i])
