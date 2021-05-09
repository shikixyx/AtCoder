import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())
    a, b, c = solve(N, K)
    print(a, b, c)
    return


def solve(N, K):
    a, b, c = 1, 1, 1

    for sm in range(3, ((N * 3) + 1)):
        print("sum: {}".format(sm))

        r = N * 3 - sm
        t = (r + 2) * (r + 1) // 2

        print("t: {}, K : {}".format(t, K))

        if t < K:
            K -= t
            continue

        ## 何個取っていくか
        for i in range(1, N + 1):
            if (i + 2) > sm:
                break

            r = sm - i
            t = 

    return a, b, c


if __name__ == "__main__":
    main()
