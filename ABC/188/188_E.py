import sys

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
        E[x].append(y)

    P = [-1] * (N + 1)

    visited = [False] * (N + 1)
    for i in range(1, N + 1):

        if visited[i]:
            continue

        Q = [(i, -1)]
        while Q:
            v, c = Q.pop()
            visited[v] = True

            if c == -1:
                c = 10 ** 9 + 10
                pass
            else:
                if P[v] == -1:
                    P[v] = c
                else:
                    P[v] = min(P[v], c)

            c = min(c, A[v])

            for u in E[v]:
                Q.append((u, c))

    ans = -(10 ** 10)
    for i in range(N + 1):
        if P[i] == -1:
            continue

        ans = max(ans, A[i] - P[i])

    print(ans)

    return


if __name__ == "__main__":
    main()
