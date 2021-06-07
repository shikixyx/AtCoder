import sys
import heapq

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def calc(now, c, d):
    nxt = now + c + (d // (now + 1))

    mid = int(d ** 0.5) + 1
    if now >= mid:
        return nxt

    ## 最小の時間がある場合
    mid = int(d ** 0.5) - now
    ret = 10 ** 12
    for x in [-1, 0, 1]:
        wait = max(mid + x, 0)
        t = now + wait + c + (d // (now + wait + 1))
        ret = min(ret, t)

    return ret


def main():
    N, M = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(M)]
    PATH = [[] for _ in range(N + 1)]

    for a, b, c, d in ABCD:
        if a == b:
            continue
        PATH[a].append((b, c, d))
        PATH[b].append((a, c, d))

    COST = [-1] * (N + 10)

    COST[1] = 0

    q = [(0, 1)]
    while q:
        now, u = heapq.heappop(q)
        if COST[u] != -1 and COST[u] < now:
            continue

        if u == N:
            break

        for v, c, d in PATH[u]:
            t = calc(now, c, d)
            if COST[v] == -1 or (t < COST[v]):
                COST[v] = t
                heapq.heappush(q, (t, v))

    print(COST[N])

    return


if __name__ == "__main__":
    main()
