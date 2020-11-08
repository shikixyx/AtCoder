import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = False

for A in itertools.combinations(xy, 3):
    p = A[0]
    q = A[1]
    r = A[2]

    dx1 = q[0] - p[0]
    dx2 = r[0] - q[0]
    dy1 = q[1] - p[1]
    dy2 = r[1] - q[1]

    if dx1 * dy2 == dx2 * dy1:
        ans = True

if ans:
    print("Yes")
else:
    print("No")

