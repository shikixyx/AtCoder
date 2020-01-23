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


# N以下の素数を列挙
# make primes
U = 10 ** 6 + 10
is_prime = np.zeros(U, np.bool)
is_prime[2] = 1
is_prime[3::2] = 1
for p in range(3, U, 2):
    if p*p > U:
        break
    if is_prime[p]:
        is_prime[p*p::p+p] = 0


# nの素数判定
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# nの約数列挙
def divisor(n):
    ass = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass  # sortされていない


# nの素因数分解(O(n**0.5)
def prime_factor(n):
    ass = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass


# [[素因数,数]]を出力
def fctr1(n):
    f = []
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f


# n以下の素数列挙(O(n log(n))
def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass


# a以上b未満の素数列挙
def segment_sieve(a, b):
    ass = []
    is_prime_small = [True] * (int(b**0.5)+1)
    is_prime = [True] * (b-a)
    for i in range(2, int(b**0.5)):
        if is_prime_small[i]:
            j = 2*i
            while j**2 < b:
                is_prime_small[j] = False
                j += i
            j = max(2*i, ((a+i-1)//i)*i)
            while j < b:
                is_prime[j-a] = False
                j += i
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(a+i)
    if ass[0] == 1:
        del ass[0]
    return ass


# 最小公倍数を素因数で
def lcm_fctr(n, l):
    a = fctr1(n)
    for p, i in a:
        l[p] = max(i, l[p])
    return l


N = int(input())
A = list(map(int, input().split()))

l = defaultdict(int)
for a in A:
    lcm_fctr(a, l)

e = 1
for i in l.keys():
    e = (e * pow(i, l[i], MOD)) % MOD

ans = 0
for a in A:
    m = modinv(a, MOD)
    ans += (e * m) % MOD
    ans %= MOD

print(ans)
