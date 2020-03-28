import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 回答見た
# ベルマンフォード法
# 1-Nまでの経路の中での負閉路検出(大体セット)


N, M, P = map(int, readline().split())

EDGES = []
TO = [[] for _ in range(N + 1)]
RTO = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, readline().split())
    EDGES.append((a, b, c))
    TO[a].append(b)
    RTO[b].append(a)

# 1から到達可能な点
REACH_FROM_1 = [False] * (N+1)
q = [1]
while q:
    u = q.pop()
    if REACH_FROM_1[u]:
        continue
    REACH_FROM_1[u] = True
    for v in TO[u]:
        q.append(v)

# Nから到達可能な点
REACH_TO_N = [False] * (N + 1)
q = [N]
while q:
    u = q.pop()
    if REACH_TO_N[u]:
        continue
    REACH_TO_N[u] = True
    for v in RTO[u]:
        q.append(v)

STATE = [REACH_FROM_1[i] & REACH_TO_N[i] for i in range(N + 1)]


INF = 10 ** 12
POINT = [INF] * (N + 1)

POINT[1] = 0

for i in range(N):
    update = False
    for j in range(M):
        a, b, c = EDGES[j]
        if not STATE[a]:
            continue
        pt = - (c - P)
        if POINT[a] != INF and POINT[a] + pt < POINT[b]:
            POINT[b] = POINT[a] + pt
            update = True

            if i == N-1:
                print(-1)
                exit()

    if not update:
        break

# print(POINT)
pt = -POINT[N]

ans = pt if pt > 0 else 0
print(ans)
