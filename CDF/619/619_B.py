import sys
sys.setrecursionlimit(10 ** 7)

T = int(input())

CASE = []
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    CASE.append([n, A])


res = []
for n, A in CASE:
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

            if i != n - 1:
                ain = A[i + 1]
                if ain != -1:
                    nmin = min(nmin, ain)
                    nmax = max(nmax, ain)
        else:
            if aip != -1:
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
    res.append("{} {}".format(m, k))

print("\n".join(res))
