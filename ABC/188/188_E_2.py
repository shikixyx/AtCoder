import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    A = [-1] + list(map(int, input().split()))

    E = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        E[y].append(x)

    visited = [False] * (N + 1)
    P = [-1] * (N + 1)

    @lru_cache(maxsize=None)
    def get_min(v):
        visited[v] = True
        t = -1
        for u in E[v]:
            if t == -1:
                t = A[u]
            else:
                t = min(t, A[u])

            a = get_min(u)

            if a == -1:
                pass
            else:
                t = min(a, t)

        P[v] = t

        return t

    for i in range(1, N + 1)[::-1]:
        if not visited[i]:
            get_min(i)

    ans = -(10 ** 10)
    for i in range(N + 1):
        if P[i] == -1:
            continue

        ans = max(ans, A[i] - P[i])

    print(ans)

    return


if __name__ == "__main__":
    main()
