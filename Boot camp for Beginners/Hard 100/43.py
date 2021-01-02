from collections import Counter
from heapq import heappush, heappop

H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]

A = [list(map(int, input().split())) for _ in range(H)]

COST = [10 ** 4 + 10] * 10
COST[1] = 0

Q = [(0, 1)]

t = 0

while Q:
    c, u = heappop(Q)

    for v in range(10):
        if v == 1 or v == u:
            continue

        nc = c + C[v][u]
        if COST[v] > nc:
            COST[v] = nc
            heappush(Q, (nc, v))
            t += 1

print("t", t)


cnt = Counter([])
for a in A:
    cnt += Counter(a)

ans = 0
for i in range(10):
    ans += cnt[i] * COST[i]

print(ans)

