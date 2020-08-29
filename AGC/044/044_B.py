import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
P = list(map(int, input().split()))

DIST = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        d = min(i, N - i - 1, j, N - j - 1)
        DIST[i][j] = d


def update(x, y):
    for a, b in itertools.product([-1, 0, 1], repeat=2):
        if abs(a) + abs(b) != 1:
            continue

        

    return


ans = 0
for p in P:
    ans += DIST[p // N][p % N]
    update(p // N, p % N)


print(DIST)
