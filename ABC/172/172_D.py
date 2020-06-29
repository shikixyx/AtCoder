"""
import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
"""

N = int(input())

CNT = [1] * (N + 1)

ans = 1
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        CNT[j] += 1
    ans += i * CNT[i]

print(ans)
