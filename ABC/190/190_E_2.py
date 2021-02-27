import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())

    # 1-index
    PATH = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        PATH[a] += [b]
        PATH[b] += [a]

    K = int(input())
    C = list(map(int, input().split()))

    MIN_DIST = {}
    for c in C:
        MIN_DIST[c] = {}
        for k in C:
            if c == k:
                continue
            MIN_DIST[c][k] = -1

    for c in C:
        VISIT = [False] * (N + 1)
        DIST = [-1] * (N + 1)
        Q = deque()
        Q.append((c, 0, -1))

        while Q:
            u, d, parent = Q.popleft()

            for v in PATH[u]:
                if v == parent or VISIT[v]:
                    continue

                VISIT[v] = True
                DIST[v] = d + 1
                Q.append((v, d + 1, u))

        for c2 in C:
            if c == c2:
                continue
            MIN_DIST[c][c2] = DIST[c2]

    INF = 10 ** 10 + 10
    DP = [[INF] * K for _ in range(1 << K)]
    for i in range(K):
        DP[1 << i][i] = 0

    for i in range(1 << K):
        for u in range(K):
            if not i & (1 << u):
                continue

            for v in range(K):
                if u == v:
                    continue

                if i & (1 << v):
                    continue

                if MIN_DIST[C[u]][C[v]] == -1:
                    continue

                if DP[i][u] == INF:
                    continue

                DP[i | (1 << v)][v] = min(
                    DP[i | (1 << v)][v], DP[i][u] + MIN_DIST[C[u]][C[v]]
                )

    ans = -1
    for c in range(K):
        if DP[(1 << K) - 1][c] == INF:
            continue

        if ans == -1:
            ans = DP[(1 << K) - 1][c] + 1
        else:
            ans = min(ans, DP[(1 << K) - 1][c] + 1)

    print(ans)

    return


if __name__ == "__main__":
    main()
