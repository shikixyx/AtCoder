import operator
import itertools
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 逆元求めるよう
MOD = 998244353


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


NAME = ["ZERO", "ONE", "a", "A"]
OPNAME = ['AND', 'OR', 'XOR']

ZERO = [0, 0]
ONE = [1, 1]
a = [0, 1]
A = [1, 0]

CHOICE = [ZERO, ONE, a, A]


cnt = [0] * 4
calcRes = [[[None] * 4 for _ in range(4)] for _ in range(3)]


def test(x, y, z, w):
    X = CHOICE[x]
    Y = CHOICE[y]
    Z = CHOICE[z]
    W = CHOICE[w]

    g = [0] * 2

    for i in range(2):
        g[i] = (X[i] & Y[i]) ^ (Z[i] | W[i])

    ret = None
    if g[0] == 0 and g[1] == 0:
        ret = 0
    elif g[0] == 1 and g[1] == 1:
        ret = 1
    elif g[0] == 0 and g[1] == 1:
        ret = 2
    elif g[0] == 1 and g[1] == 0:
        ret = 3

    cnt[ret] += 1

    return


for x, y, z, w in itertools.product(range(4), repeat=4):
    test(x, y, z, w)

print(cnt)
total = sum(cnt) % MOD
total_inv = modinv(total, MOD)
ANS = [x * total_inv % MOD for x in cnt]
print(" ".join(map(str, ANS)))
