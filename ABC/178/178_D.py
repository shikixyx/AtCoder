import sys
import numpy as np

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = int(input())
MOD = 10 ** 9 + 7

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


U = 10 ** 4
fact, fact_inv = make_fact(U * 2 + 10, MOD)
fact, fact_inv = fact.tolist(), fact_inv.tolist()


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod


N = S // 3

if S <= 2:
    print(0)
    exit()

ans = 0
for i in range(1, N + 1):
    P = S - 3 * i
    if P < 0:
        break

    ans += mod_comb_k(P + i - 1, i - 1, MOD)
    ans %= MOD

print(ans)
