import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

ACC = list(accumulate(A))

max_point = []

c = 0
k = -1
mp = 0
for i in range(N):
    a = A[i]
    c += a

    if c > mp:
        k = i
        mp = c

    max_point.append(k)

ans = 0
x = 0
for i in range(N):
    x += ACC[i]
    k = max_point[i]

    if k == -1 or k == i:
        ans = max(x, ans)
        continue

    ans = max(ans, x - (ACC[i] - ACC[k]))

print(ans)

