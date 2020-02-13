import sys

sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
P = list(map(int, input().split()))

sk = sum(P[:K])
n = sum(P[:K])
for i in range(N):
    if i < K:
        continue

    n -= P[i - K]
    n += P[i]

    sk = max(sk, n)
    prev = n

ans = sk / 2. + K / 2.
print(ans)
