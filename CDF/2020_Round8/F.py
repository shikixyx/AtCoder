import sys

N = int(input())

if N <= 3:
    print(0, flush=True)
    exit(0)


def printOn(arr):
    L = len(arr)
    A = [L] + arr
    print(" ".join(map(str, A)), flush=True)
    return


def search_4(arr):
    c = 0
    mc = 0
    e = -1
    for i in range(N + 1):
        if i == N:
            i = 0

        if c != 0 and arr[i]:
            c += 1

            if mc < c:
                mc = c
                e = i

    if mc <= 3:
        return (False, False)

    return


FLG = [False] * N

t = search_4(FLG)
