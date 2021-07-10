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
    for k in range(1, N + 1):
        for n in range(1, N + 1):
            dist = [0] * (N + 10)
            h = [(0, n)]

            while h:
                d, u = heapq.heappop(h)
                if d > dist[u]:
                    continue

                for v, cost in PATH[u]:
                    if v == n:
                        continue

                    t = d + cost

                    if dist[v] == 0:
                        dist[v] = t

                        if v <= k:
                            heapq.heappush(h, (t, v))
                    else:
                        if t < dist[v]:
                            dist[v] = t

                            if v <= k:
                                heapq.heappush(h, (t, v))

            ans += sum(dist)

    print(ans)

    return


if __name__ == "__main__":
    main()
