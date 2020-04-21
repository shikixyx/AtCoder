import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
ans = N - total

if ans >= 0:
    print(ans)
else:
    print(-1)

