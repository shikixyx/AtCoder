import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]

    PATH = [[] for _ in range(N + 1)]

    for a, b, c in ABC:
        PATH[a].append((b, c))

    ANS = [-1] * (N + 1)
    VISIT = [-1] * (N + 1)

    for i in range(1, N + 1):
        if VISIT[i] == -1:
            start = (i, [i], 0)
            VISIT[i] = i
            Q = deque([start])
            cnt = 0
            while Q:
                # print(Q)
                now, route, cost = Q.popleft()

                # 閉路あるなら更新
                if now == i and cost != 0:
                    for x in route:
                        if ANS[x] == -1:
                            ANS[x] = cost
                        else:
                            ANS[x] = min(cost, ANS[x])
                    continue

                for nxt, c in PATH[now]:
                    print(nxt, VISIT[nxt])
                    if VISIT[nxt] == -1 or VISIT[nxt] == i:
                        VISIT[nxt] = i
                        new_route = route[:]
                        new_route.append(nxt)
                        Q.append((nxt, new_route, cost + c))

    print("\n".join(map(str, ANS[1:])))

    return


if __name__ == "__main__":
    main()
