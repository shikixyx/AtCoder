import sys
import math

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def extgcd(a, b):
    if b == 0:
        return a, 1, 0

    p, q = a // b, a % b
    d, x, y = extgcd(b, q)
    x, y = y, x - p * y
    return d, x, y


def solve():
    X, Y, P, Q = map(int, input().split())

    A = 2 * X + 2 * Y
    B = 2 * P + 2 * Q

    g = math.gcd(A, B)

    flg = False
    ans = 10 ** 20 + 100
    for y in range(1, Y):
        for q in range(1, Q):
            if y % g != q % g:
                continue

            d, p, q = extgcd(A, B)
            s = (q - y) // g
            ## t = y + s * 1

    return


T = int(input())
ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("/n".join(map(str, ans)))
