import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, input().split())
lst = list(range(N + 1))

MOD = 10 ** 9 + 7

small = 0
for i in range(K-1):
    small += lst[i]

big = 0
for i in range(1, K):
    big += lst[-i]

ans = 0
for i in range(K, N + 2):
    small += lst[i - 1]
    big += lst[-i]

    ans += big - small + 1
    ans %= MOD


print(ans % MOD)
