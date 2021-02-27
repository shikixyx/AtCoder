import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]

D = [[0] * N for _ in range(N)]


def get_dist(u, v):
    a, b, c = XYZ[u]
    p, q, r = XYZ[v]

    d = abs(a - p) + abs(b - q) + max(0, r - c)
    return d


for i in range(N):
    for j in range(N):
        if i == j:
            continue

        D[i][j] = get_dist(i, j)


DP = [[10 ** 10] * N for _ in range(1 << N)]


DP[1][0] = 0

for i in range(1, (1 << N) - 1):
    ## 今uの状態
    for u in range(N):
        ## 行ったことがなければNG
        if not i & (1 << u):
            continue

        # 次vの状態
        for v in range(N):
            if u == v:
                continue

            ## 行ったことなければ
            if not i & (1 << v):
                DP[i | (1 << v)][v] = min(DP[i | (1 << v)][v], DP[i][u] + D[u][v])


ans = 10 ** 10
for i in range(1, N):
    ans = min(DP[(1 << N) - 1][i] + D[i][0], ans)

print(ans)

