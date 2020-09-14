import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c, d = map(int, input().split())

ans = max(a * c, a * d, b * c, b * d)
print(ans)
