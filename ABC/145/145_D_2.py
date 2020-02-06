import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

X, Y = map(int, input().split())

# 移動回数
if (X + Y) % 3 != 0:
    print(0)
    exit()

nm = (X + Y) // 3
n = X - nm
m = Y - nm

if n < 0 or m < 0:
    print(0)
    exit()


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


# def mod_comb_k(n, k, mod):
    # return fact[n] * fact_inv[k] % mod * fact_inv[n-k] % mod

MOD = 10 ** 9 + 7
U = 10**6
fact, fact_inv = make_fact(U, MOD)
ans = fact[nm] * fact_inv[n] % MOD * fact_inv[nm-n] % MOD
print(ans)
