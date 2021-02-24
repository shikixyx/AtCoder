import sys
import math
from decimal import *
import bisect

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

getcontext().prec = 100


def main():
    X, Y, R = map(float, input().split())

    low = math.ceil(X - R)
    high = math.floor(X + R)

    SQ = []
    for i in range(1, 10 ** 6):
        SQ.append(i * i)

    ans = 0
    for i in range(low, high + 1):
        a = X - i
        p = (Decimal(R) ** 2 - Decimal(a) ** 2).sqrt()
        # p = R * R - a * a

        # top = Y * Y + p
        # top += bisect.bisect_right(SQ, p * 4)

        # bottom = Y * Y + p
        # bottom -= bisect.bisect_left(SQ, p * 4) + 1

        bottom = math.ceil(Decimal(Y) - p)
        top = math.floor(Decimal(Y) + p)
        ans += top - bottom + 1

    print(ans)

    return


if __name__ == "__main__":
    main()
