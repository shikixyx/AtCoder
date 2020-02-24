import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

N, A, B = map(int, input().split())

MOD = 10 ** 9 + 7


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


ans = myPow(2, N, MOD)
ans -= 1

# print("hoge")


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


fact, fact_inv = make_fact(B + 10, MOD)

arr = cumprod(list(range(N, N-B, -1)), MOD)

a = arr[A - 1] * fact_inv[A]
a %= MOD
b = arr[B-1] * fact_inv[B]
b %= MOD

# print(mb)
# print(fact_inv)

'''
a = ma * fact_inv[A]
a %= MOD

b = mb * fact_inv[B]
b %= MOD
'''

ans -= (a + b)
ans %= MOD

print(ans)
