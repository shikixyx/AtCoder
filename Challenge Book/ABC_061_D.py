import sys
sys.setrecursionlimit(10 ** 7)

# Bellman-Ford法
# ベルマンフォード法

N, M = map(int, input().split())
EDGES = []

for _ in range(M):
    a, b, c = map(int, input().split())
    EDGES.append((a, b, -c))

INF = 10 ** 18
d = [INF] * (N+1)
d[1] = 0

ans = 0
for k in range(N):
    update = False
    for i in range(M):
        a, b, c = EDGES[i]
        if d[a] != INF and d[b] > d[a] + c:
            d[b] = d[a] + c
            update = True

            if k == N-1 and b == N:
                print('inf')
                exit()

    if not update:
        break

print(-d[N])
