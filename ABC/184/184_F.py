import sys
import itertools
import bisect

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# TLE


def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    if N == 1:
        if A[0] <= T:
            print(A[0])
        else:
            print(0)
        exit()

    h = N // 2

    N1 = A[:h]
    N2 = A[h:]

    S1 = []
    for i in range(2 ** h):
        c = 0
        idx = 0
        while i:
            if i & 1:
                c += N1[idx]

            idx += 1
            i >>= 1

        S1.append(c)

    S1.sort()

    ans = 0
    for i in range(2 ** (N - h)):
        c = 0
        idx = 0
        while i:
            if i & 1:
                c += N2[idx]

            idx += 1
            i >>= 1

        if c > T:
            continue

        key = T - c
        k = bisect.bisect_right(S1, key)
        t = c
        if not (k - 1 < 0):
            t += S1[k - 1]
        ans = max(ans, t)

    print(ans)

    return


if __name__ == "__main__":
    main()
