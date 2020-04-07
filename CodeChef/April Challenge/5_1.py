import operator
from functools import reduce
import math
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def solve():
    DEBUG = False
    N = int(readline())
    A = list(map(int, readline().split()))

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            L = A[i:j]
            p = prod(L)

            if p % 4 == 0 or p % 2 == 1:
                cnt += 1

    return cnt


ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
