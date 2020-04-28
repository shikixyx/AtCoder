from heapq import heappop, heappush
import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M, S = map(int, input().split())
S = min(2500, S)

# INPUT
PATH = [[] for _ in range(N + 1)]
CHANGES = [None] * (N + 1)

for _ in range(M):
    U, V, A, B = map(int, input().split())
    PATH[U].append((V, A, B))
    PATH[V].append((U, A, B))

for i in range(N):
    C, D = map(int, input().split())
    CHANGES[i + 1] = (C, D)

Q = []
INF = float("inf")
TIME = [[INF] * 2501 for _ in range(N + 1)]
USED = [[False] * 2501 for _ in range(N + 1)]

Q.append((0, 1, S))
TIME[1][S] = 0

while Q:
    t, u, g = heappop(Q)

    # そこで銀貨を増やす
    # 2500枚未満の場合
    if g < 2500:
        c, d = CHANGES[u]
        ng = min(g + c, 2500)
        nt = t + d

        if nt < TIME[u][ng]:
            TIME[u][ng] = nt
            heappush(Q, (nt, u, ng))

    # 次の頂点に進む
    for v, a, b in PATH[u]:
        if g < a:
            continue

        ng = g - a
        nt = t + b
        if nt < TIME[v][ng]:
            TIME[v][ng] = nt
            heappush(Q, (nt, v, ng))

ANS = [min(x) for x in TIME[2:]]
print("\n".join(map(str, ANS)))
