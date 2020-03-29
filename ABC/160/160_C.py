import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

K, N = map(int, input().split())
A = list(map(int, input().split()))

ans = K
for i in range(1, N):
    r = K - (A[i] - A[i - 1])
    ans = min(r, ans)

r = A[N - 1] - A[0]
ans = min(r, ans)

print(ans)
