import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# WA

N, X, Y = map(int, input().split())

for i in range(1, N):
    DIST = [0] * (N+1)

    USED = [False] * (N+2)

    q = [(1, 0)]
    while q:
        u, d = q.pop()
        DIST[d] += 1
        USED[u] = True

        if u != N and not USED[u + 1]:
            q.append((u + 1, d + 1))

        if u == X and not USED[Y]:
            q.append((Y, d+1))

    print(DIST)
