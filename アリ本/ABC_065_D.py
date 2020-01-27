import sys
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

# 最小全域木
# プリム法 #
# 部分木から、最小コストの辺を貪欲に追加

# Kruskal法 #
# クラスカル法 #
# 辺でソートして、最小コストの辺から、ループにならないよう貪欲に追加
# UnionFindを使う


N = int(input())

# x,yでそれぞれソート
POINT_x = []
POINT_y = []
for _ in range(N):
    x, y = map(int, input().split())
    POINT_x.append((x, y))
    POINT_y.append((x, y))

POINT_x = sorted(POINT_x, key=lambda x: x[0])
POINT_y = sorted(POINT_y, key=lambda x: x[1])

EDGE = defaultdict(list)
for i in range(N):
    p = POINT_x[i]

    if i != 0:
        prev = POINT_x[i-1]
        EDGE[p].append((abs(p[0]-prev[0]), prev))

    if i != N-1:
        nxt = POINT_x[i+1]
        EDGE[p].append((abs(p[0]-nxt[0]), nxt))

for i in range(N):
    p = POINT_y[i]

    if i != 0:
        prev = POINT_y[i-1]
        EDGE[p].append((abs(p[1]-prev[1]), prev))

    if i != N-1:
        nxt = POINT_y[i+1]
        EDGE[p].append((abs(p[1]-nxt[1]), nxt))


INF = 10 ** 12
mincost = [INF] * N
used = defaultdict(lambda: False)

point = POINT_x[0]
used[point] = True
q = []
ans = 0

for e in EDGE[point]:
    heapq.heappush(q, e)

while(True):
    update = False
    for _ in range(len(q)):
        cost, point = heapq.heappop(q)
        if used[point]:
            continue

        update = True
        ans += cost
        used[point] = True

        for e in EDGE[point]:
            if not used[e[1]]:
                heapq.heappush(q, e)

    if not update:
        break

print(ans)
