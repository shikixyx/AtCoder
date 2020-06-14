import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Python TLE
# Pypy AC

N, K = map(int, input().split())
A = list(map(int, input().split()))

K = min(K, 50)

for _ in range(K):
    imos = [0] * (N + 1)

    for i in range(N):
        a = A[i]
        s = max(0, i - a)
        e = min(N, i + a + 1)
        imos[s] += 1
        imos[e] -= 1

    nxt = [0] * N
    t = 0
    for i in range(N):
        t += imos[i]
        nxt[i] = t

    A = nxt

print(" ".join(map(str, A)))
