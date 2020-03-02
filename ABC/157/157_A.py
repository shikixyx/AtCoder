import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())

if N % 2 == 0:
    ans = N // 2
else:
    ans = (N + 1) // 2

print(ans)
