import sys
import numpy as np

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M, K = map(int, input().split())
MOD = 998244353

# 階乗、Combinationコンビネーション(numpyを使う)


def cumprod(arr, MOD):
    L = len(arr)
    Lsq = int(L ** 0.5 + 1)
    arr = np.resize(arr, Lsq ** 2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n - 1]
        arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n - 1, -1]
        arr[n] %= MOD
    return arr.ravel()[:L]


def make_fact(U, MOD):
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), MOD - 2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv


U = (10 ** 5) * 2 + 100
fact, fact_inv = make_fact(U, MOD)


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod


ans = 0
t = M

if K == (N - 1):
    ans += M

for i in range(1, N):
    kumi = N - i - 1
    t *= M - 1
    t %= MOD
    if K < kumi:
        continue

    c = mod_comb_k(N - 1, i, MOD)
    ans += c * t
    ans %= MOD

print(ans)
