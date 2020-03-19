from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 20min
# 尺取り法 while

N, K = map(int, input().split())
A = list(map(int, input().split()))

s = 0
ans = 0
r = 0

for l in range(N):
    while s < K and r < N:
        s += A[r]
        r += 1

    if K <= s:
        ans += N - r + 1
        s -= A[l]
    else:
        break


print(ans)
