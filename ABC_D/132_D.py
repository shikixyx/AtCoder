import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 20min
# 数え上げ問題

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


U = 10**4
fact, fact_inv = make_fact(U, MOD)
fact, fact_inv = fact.tolist(), fact_inv.tolist()


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod


ans = []
red = N - K

# i回操作する方法
for i in range(1, K + 1):
    #print("i=", i)
    res = 1

    # i分割するためには、i-1個ボールが必要
    if red < (i - 1):
        ans.append(str(0))
        continue

    # i分割する
    # i-1箇所に置く
    pat_split = 1
    pat_split *= mod_comb_k(K - 1, i - 1, MOD)

    #print("pat_split", pat_split)

    # 残りの玉を置く
    pat_rest = i - 1 + 2
    bal_rest = N - (i - 1) - K
    res *= mod_comb_k(pat_rest + bal_rest - 1, bal_rest, MOD)
    #print("res", res)
    res *= pat_split
    res %= MOD

    ans.append(str(res))

print("\n".join(ans))
