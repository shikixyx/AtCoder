import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

ACC = accumulate(A)

total = 0
for i in range(N):
    total += A[i] * (i + 1)

ans = total
for a in list(ACC)[::-1]:
    total -= a
    ans = max(ans, total)

print(ans)

