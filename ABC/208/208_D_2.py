import sys
import heapq

sys.setrecursionlimit(10 ** 7)


def main():
    N, M = map(int, input().split())

    PATH = [[] for _ in range(N + 10)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        PATH[a].append((b, c))

    ans = 0
    dist = [[0] * (N + 10) for _ in range(N + 10)]

    for u in range(1, N + 1):
        for v, cost in PATH[u]:
            dist[u][v] = cost

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    continue

                if dist[i][k] == 0 or dist[k][j] == 0:
                    continue

                if dist[i][j] == 0 or dist[i][j] > (dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]

        for row in dist:
            ans += sum(row)

    print(ans)

    return


if __name__ == "__main__":
    main()
