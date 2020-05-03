import sys
import math

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, N = map(int, input().split())

ans = 0

if N < B - 1:
    ans = math.floor(A * N / B) - A * math.floor(N / B)
else:
    c = B - 1
    cnt = 1
    while c <= N:
        cnt += 1
        t = math.floor(A * c / B) - A * math.floor(c / B)
        ans = max(ans, t)
        c += B
        if B < cnt:
            break

print(ans)
