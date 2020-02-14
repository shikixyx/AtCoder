import sys
sys.setrecursionlimit(10 ** 7)

T = int(input())


def calc(n, A):
    prev = A[0]
    m = 0
    k = 0
    nmin = 10 ** 9
    nmax = 0

    for i in range(1, n):
        ai = A[i]
        aip = A[i - 1]
        if ai == -1:
            if aip != -1:
                nmin = min(nmin, aip)
                nmax = max(nmax, aip)
        else:
            if aip == -1:
                nmin = min(nmin, ai)
                nmax = max(nmax, ai)
            else:
                m = max(m, abs(ai - aip))

    # diff
    # each diff
    if nmin != (10 ** 9) and nmax != 0:
        ndiff = nmax - nmin
        nm = -(-ndiff // 2)
        k = nmin + (ndiff // 2)
    else:
        nm = 0
        if nmin == 10 ** 9:
            k = nmax
        elif nmax == 0:
            k = nmin

    # chose max
    m = max(m, nm)

    return m, k


res = []
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))

    m, k = calc(n, A)
    res.append("{} {}".format(m, k))


print("\n".join(res))
