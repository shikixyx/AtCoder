import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

MAX_P = 0
MIN_P = 10 ** 10
MAX_M = -(10 ** 10)
MIN_M = 10 ** 10

for x, y in XY:
    P = x + y
    M = x - y

    MAX_P = max(MAX_P, P)
    MIN_P = min(MIN_P, P)

    MAX_M = max(MAX_M, M)
    MIN_M = min(MIN_M, M)

ans = max(MAX_P - MIN_P, MAX_M - MIN_M)

print(ans)

