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
        t = (sm - 1) * (sm - 2) // 2

        print("t: {}, K : {}".format(t, K))

        if t < K:
            K -= t
            continue

        ## 間が sm - 1こ
        for i in range(1, sm - 1):
            t = (sm - 1) - i
            print(t)
            if t < K:
                K -= t
                continue

            a = i
            b = K - i + 1
            c = sm - a - b
            return a, b, c

    return a, b, c


if __name__ == "__main__":
    main()
