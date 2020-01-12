import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappop, heappush
from fractions import Fraction

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


N = int(input())
X = list(map(int, input().split()))
MOD = 10**9+7

MAXN = N+5
fac = [1, 1] + [0] * MAXN
inv = [0, 1] + [0] * MAXN


for i in range(2, N):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = modinv(i, MOD)


c = 0
t = 0
f = fac[N-1]

for i in range(0, N-1):
    x = X[i+1] - X[i]
    c += f * inv[i+1]
    c %= MOD
    t += c * x
    t %= MOD

print(t)
