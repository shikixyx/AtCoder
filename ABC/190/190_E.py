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
        VISIT = [False] * (N + 1)
        DIST = [-1] * (N + 1)
        Q = deque()
        Q.append((c, 0, -1))

        while Q:
            u, d, parent = Q.popleft()

            for v in PATH[u]:
                if v == parent or VISIT[v]:
                    continue

                DIST[v] = d + 1
                Q.append((v, d + 1, u))

        for c2 in C:
            if c == c2:
                continue
            MIN_DIST[c2] = DIST[c2]

    

    return


if __name__ == "__main__":
    main()
