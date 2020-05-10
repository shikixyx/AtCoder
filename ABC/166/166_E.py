import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

CNT = [0] * (10 ** 7)

ans = 0
for i in range(N):
    a = A[i]
    p = i - a

    if 0 <= p <= (10 ** 7):
        ans += CNT[p]

    if 0 <= i + a <= (10 ** 7):
        CNT[i + a] += 1

print(ans)
