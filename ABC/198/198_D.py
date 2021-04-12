import sys
import itertools
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A = input()
    B = input()
    C = input()

    D = set(list(A + B + C))

    if len(D) > 10:
        print("UNSOLVABLE")
        return

    D = list(D)
    L = len(D)
    c = 0

    index_a = {}
    index_b = {}
    index_c = {}

    for i in range(L):
        index_a[D[i]] = [n for n, v in enumerate(list(A)) if v == D[i]]
        index_b[D[i]] = [n for n, v in enumerate(list(B)) if v == D[i]]
        index_c[D[i]] = [n for n, v in enumerate(list(C)) if v == D[i]]

    ## 先頭見る
    fa = A[0]
    fb = B[0]
    fc = C[0]
    ia = D.index(fa)
    ib = D.index(fb)
    ic = D.index(fc)

    for x in itertools.permutations(range(10), L):
        if x[ia] == 0 or x[ib] == 0 or x[ic] == 0:
            continue

        NA = [0] * len(A)
        NB = [0] * len(B)
        NC = [0] * len(C)

        for i in range(L):
            d = D[i]
            y = str(x[i])

            for j in index_a[d]:
                NA[j] = y

            for j in index_b[d]:
                NB[j] = y

            for j in index_c[d]:
                NC[j] = y

        NA, NB, NC = int("".join(NA)), int("".join(NB)), int("".join(NC))

        if NA == 0 or NB == 0 or NC == 0:
            continue

        if (
            (NA + NB) == NC
            and len(str(NA)) == len(A)
            and len(str(NB)) == len(B)
            and len(str(NC)) == len(C)
        ):
            print(NA)
            print(NB)
            print(NC)

            return

    print("UNSOLVABLE")

    return


if __name__ == "__main__":
    main()
