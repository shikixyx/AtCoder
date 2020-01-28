import sys
sys.setrecursionlimit(10 ** 7)

# カーマイケル数
# Carmichael Numbers
# 累乗の高速化

P = int(input())
N = int(input())

F = [0]*P
MOD = P


def myPow(x, n, MOD):
    if n == 0:
        return 1

    res = 1
    while(n > 0):
        if n & 1 == 1:
            res = res * x % MOD

        x = x * x % MOD
        n = n >> 1

    return res


for i in range(P):
    r = myPow(i, N, MOD)
    F[r] += 1

cnt = [0]*P
for x in range(P):
    for y in range(P):
        z = (x+y) % MOD
        cnt[z] += F[x] * F[y] * F[z]

print(sum(cnt))
