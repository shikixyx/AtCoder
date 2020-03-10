import sys
import math
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B = map(int, input().split())

ans = -1
for i in range(1, 1263):
    if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
        ans = i
        break

print(ans)
