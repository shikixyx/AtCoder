import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N = int(input())

points = {}

for _ in range(N):
    c = input()

    if c in points:
        points[c] += 1
    else:
        points[c] = 1

M = int(input())

for _ in range(M):
    c = input()

    if c in points:
        points[c] -= 1
    else:
        points[c] = -1

ans = 0

# print(points)

for v in points.values():
    if ans < v:
        ans = v

if ans < 0:
    ans = 0

print(ans)
