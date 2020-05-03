import sys
import itertools


sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# WA

N, M, Q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

NUM = list(range(1, M + 1))

ans = 0

for XS in itertools.product(NUM, repeat=N):
    XS = list(XS)
    XS.sort()
    p = 0
    for a, b, c, d in ABCD:
        if XS[b - 1] - XS[a - 1] == c:
            p += d

    ans = max(ans, p)

print(ans)
