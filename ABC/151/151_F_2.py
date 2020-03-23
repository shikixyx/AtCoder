import math
import sys
import itertools
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 最小包含円
# 2点と外接円
# EPSに気をつける

N = int(input())
XY = [[float(x) for x in input().split()] for _ in range(N)]

ans = 1500.
eps = 10. ** -8


def circumcenter(A, B, C):
    ax = A[0]
    ay = A[1]
    bx = B[0]
    by = B[1]
    cx = C[0]
    cy = C[1]
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))

    if d == 0.:
        return None

    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by)
          * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by)
          * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return (ux, uy)


def check(center_x, center_y, R2):
    ok = True
    for x, y in XY:
        d = (center_x - x) ** 2. + (center_y - y) ** 2.
        if R2 + eps < d:
            ok = False
            break

    return ok


# 2点
for i, j in itertools.combinations(range(N), 2):
    ax, ay = XY[i]
    bx, by = XY[j]

    center_x = (ax + bx) / 2.
    center_y = (ay + by) / 2.
    R2 = (ax - center_x) ** 2 + (ay - center_y) ** 2
    R = math.sqrt(R2)

    if check(center_x, center_y, R2):
        ans = min(R, ans)


# 3点
for a, b, c in itertools.combinations(range(N), 3):
    d = circumcenter(XY[a], XY[b], XY[c])

    if d is None:
        continue

    center_x = d[0]
    center_y = d[1]

    ax = XY[a][0]
    ay = XY[a][1]
    R2 = (ax - center_x) ** 2. + (ay - center_y) ** 2.
    R = math.sqrt(R2)

    ok = check(center_x, center_y, R2)

    if check(center_x, center_y, R2):
        ans = min(ans, R)

print(ans)
