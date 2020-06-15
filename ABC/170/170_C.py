import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

X, N = map(int, input().split())

if N == 0:
    print(X)
    exit()

P = list(map(int, input().split()))

DIFF = 200
ans = 200

for p in range(0, 102):
    if p in P:
        continue

    d = abs(X - p)

    if d == DIFF:
        ans = min(p, ans)
    elif d < DIFF:
        DIFF = d
        ans = p

print(ans)
