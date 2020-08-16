import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

L, R, D = map(int, input().split())

ans = 0
for x in range(L, R + 1):
    if (x % D) == 0:
        ans += 1

print(ans)
