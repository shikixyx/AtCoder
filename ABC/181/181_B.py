import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for a, b in AB:
    ans += (a + b) * (b - a + 1) // 2

print(ans)
