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


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def solve():
    N, S, K = map(int, input().split())

    a = K
    b = N - S
    m = N

    ans = -1
    g = math.gcd(a, m)
    if g == 1:
        # 拡張Euclid
        d, x, y = extgcd(a, m)
        ans = x * b % m
    else:
        if b % g == 0:
            a //= g
            b //= g
            m //= g

            d, x, y = extgcd(a, m)
            ans = x * b % m

    return ans


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        a = solve()
        ans.append(a)

    print("\n".join(map(str, ans)))

    return


if __name__ == "__main__":
    main()
