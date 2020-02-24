import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
MOD = 10 ** 9 + 7

# 階乗、Combinationコンビネーション(numpyを使う)


def cumprod(arr, MOD):
    L = len(arr)
    Lsq = int(L**.5+1)
    arr = np.resize(arr, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n-1]
        arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n-1, -1]
        arr[n] %= MOD
    return arr.ravel()[:L]


def make_fact(U, MOD):
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv


U = 10**6
fact, fact_inv = make_fact(N * 2 + 10, MOD)
fact, fact_inv = fact.tolist(), fact_inv.tolist()


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod


ans = 0
for i in range(N):
    if K < i:
        continue

    if N - 1 <= K:
        ans = mod_comb_k(N + N - 1, N - 1, MOD)
        break

    if i == 0:
        ans += 1
        continue

    a = int(mod_comb_k(N - 1, i, MOD)) * int(mod_comb_k(N, i, MOD))
    a %= MOD
    ans += a
    ans %= MOD

    '''
    a = int(fact[N]) * int(fact_inv[i]) % MOD * int(fact_inv[N - 1])
    a = a * int(fact[N-1]) % MOD * int(fact_inv[i]) % MOD * \
        int(fact_inv[N-i-1]) % MOD
    ans = (a + ans) % MOD
    '''

print(ans)
