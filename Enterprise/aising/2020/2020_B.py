import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if i % 2 == 0 and A[i] % 2 == 1:
        ans += 1

print(ans)

