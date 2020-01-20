import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
import math
import fractions
from heapq import heappush, heappop


#read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

MOD = 10**9+7


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


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
    # return (x * y) * modinv(fractions.gcd(x, y), MOD)


N = int(input())
A = list(map(int, input().split()))

lm = 1
s = 0

for i in range(N):
    lm = lcm(A[i], lm)
    #s += lm // MOD
    #lm %= MOD

lm %= MOD
# print(lm)
ans = 0
for i in range(N):
    m = modinv(A[i], MOD)
    ans += lm * m
    ans %= MOD

print(ans)
