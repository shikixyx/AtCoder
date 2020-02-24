import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 8)

# Wrong Answer
# WA


N, K = map(int, input().split())
MOD = 10 ** 9 + 7


@lru_cache(None)
def F(n, k, m, cnt):

    ret = 0

    if cnt < 0:
        return 0

    if n < 0:
        return 0

    if k == 1:
        return 1

    for i in range(m + 1):
        if i > 1:
            a = cnt - i
        else:
            a = cnt

        t = F(n - i, k - 1, m, a)

        t %= MOD
        ret += t

    return ret


a = F(N, N, min(K + 1, N), K)

print(a)
