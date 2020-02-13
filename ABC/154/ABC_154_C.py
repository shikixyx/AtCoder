import sys

sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))

A.sort()

prev = -1
ans = 'YES'
for a in A:
    if a == prev:
        ans = 'NO'
        break

    prev = a

print(ans)
