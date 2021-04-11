import sys
import networkx as nx
from networkx.algorithms import bipartite

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M, Q = map(int, input().split())
    WV = [0] + [list(map(int, input().split())) for _ in range(N)]
    X = [0] + list(map(int, input().split()))
    QUERY = [list(map(int, input().split())) for _ in range(Q)]

    ans = []

    for i in range(Q):
        p = 0
        L, R = QUERY[i]
        box = [X[i] for i in range(1, M+1) if not L <= i <= R]
        box.sort()

        USED = [False] * (N+1)
        for x in box:
            t = []
            for i in range(1, N+1):
                if USED[i]:
                    continue

                w, v = WV[i]
                if w <= x:
                    t.append((v, i))

            if t:
                v, i = max(t)
                USED[i] = True
                p += v

        ans.append(p)

    print("\n".join(map(str, ans)))

    return


if __name__ == "__main__":
    main()
