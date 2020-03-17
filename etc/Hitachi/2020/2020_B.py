import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, M = map(int, input().split())

AS = list(map(int, input().split()))
BS = list(map(int, input().split()))

xyc = [[int(x) for x in input().split()] for _ in range(M)]

ans = min(AS) + min(BS)

for x, y, c in xyc:
    r = AS[x - 1] + BS[y - 1] - c
    ans = min(ans, r)

print(ans)
