import sys
import numpy as np

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, input().split())


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


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod


MOD = 10 ** 9 + 7
U = (10 ** 5) * 5 + 10
fact, fact_inv = make_fact(U, MOD)

prev_acc_cnt = 1
c = M - N + 1
factr = 1
rest = 1
for i in range(1, N):
    # i個違う
    t = mod_comb_k(N, i, MOD)

    # 入れ替える
    factr *= c
    factr %= MOD

    # 引く
    p = factr - prev_acc_cnt
    p %= MOD

    # 何通り
    t *= p
    t %= MOD

    # 更新
    c += 1
    prev_acc_cnt += t
    prev_acc_cnt %= MOD

    rest += t
    rest %= MOD

    # print(i, t, prev_acc_cnt, factr)

total = fact[M] * fact_inv[M - N]
total %= MOD

ans = total * (total - rest)
ans %= MOD

print(ans)

