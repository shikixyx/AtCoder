import sys
import math
from decimal import *
import bisect

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    X, Y, R = input().split()
    P = 10 ** 4

    X = int(Decimal(X) * P)
    Y = int(Decimal(Y) * P)
    R = int(Decimal(R) * P)

    low = X - R
    high = X + R

    print(X, Y, R)

    low = low // P
    high = -(-high // P)

    ans = 0
    for i in range(low, high + 1, P):
        a = X - i
        p = (R * R - a * a) ** 0.5
        # p = (Decimal(R) ** 2 - Decimal(a) ** 2).sqrt()
        # p = R * R - a * a

        # top = Y * Y + p
        # top += bisect.bisect_right(SQ, p * 4)

        # bottom = Y * Y + p
        # bottom -= bisect.bisect_left(SQ, p * 4) + 1

        # bottom = math.ceil(Decimal(Y) - p)
        # top = math.floor(Decimal(Y) + p)

        bottom = -int(-(Y - p) // P)
        top = int((Y + p) // P)

        ans += top - bottom + 1

    print(ans)

    return


if __name__ == "__main__":
    main()
