from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# でも解答見た
# BFS + グラフ拡張(頂点+状態)
# 長さ3での最短経路

N, M = map(int, readline().split())
UV = [[int(x) for x in readline().split()] for _ in range(M)]
S, T = map(int, readline().split())

PATH = [[] for _ in range(N + 1)]

for u, v in UV:
    PATH[u].append(v)

dist = [[-1] * 3 for _ in range(N+1)]

q = deque()
q.append((S, 0))
dist[S][0] = 0

while q:
    u, mod = q.popleft()
    d = dist[u][mod]

    nmod = (mod + 1) % 3
    for v in PATH[u]:
        if dist[v][nmod] != -1:
            continue
        dist[v][nmod] = d + 1
        q.append((v, nmod))


if dist[T][0] == -1:
    ans = -1
else:
    ans = dist[T][0] // 3

print(ans)
