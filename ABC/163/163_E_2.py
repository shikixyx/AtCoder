import numpy as np
import sys
sys.setrecursionlimit(10 ** 7)

# WA

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))
ACM = np.cumsum(A)


i_to_a = [[a, -i] for i, a in enumerate(A)]
i_to_a.sort(reverse=True)

ans = 0
l = 0
r = N-1

for a, i in i_to_a:
    i = -i
    left = a * abs(i - l)
    right = a * abs(r - i)
    for j in range(N):
        b = A[j]
        if a < b or (a == b and j < i):
            continue

        to_l = j - l
        to_r = r - j

        if to_l == to_r:
            left -= b
            right -= b
        elif to_l < to_r:
            right -= b
        elif to_r < to_l:
            left -= b

    if right < left:
        ans += a * abs(i - l)
        l += 1
    else:
        ans += a * abs(r - i)
        r -= 1


print(ans)
