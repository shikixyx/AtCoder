import sys
import heapq

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M, X, Y = map(int, input().split())
    E = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B, T, K = map(int, input().split())
        E[A].append((B, T, K))
        E[B].append((A, T, K))

    COST = [-1] * (N + 1)
    VISITED = [False] * (N + 1)

    COST[X] = 0
    # VISITED[X] = True

    Q = [(0, X)]
    while Q:
        now, u = heapq.heappop(Q)

        if VISITED[u]:
            continue

        VISITED[u] = True

        for v, t, k in E[u]:
            if VISITED[v]:
                continue

            nxt = -(-now // k) * k
            nxt += t

            if COST[v] == -1 or nxt < COST[v]:
                COST[v] = nxt
                heapq.heappush(Q, (nxt, v))

    if COST[Y]:
        print(COST[Y])
    else:
        print(-1)

    return


if __name__ == "__main__":
    main()
