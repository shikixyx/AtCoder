import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))

    # A1 ... AnのBIT(1-indexed)
    BIT = [0] * (N + 1)

    # A1 ~ Aiまでの和 O(logN)
    def BIT_query(idx):
        res_sum = 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    # Ai += x O(logN)
    def BIT_update(idx, x):
        while idx <= N:
            BIT[idx] += x
            idx += idx & (-idx)
        return

    AI = [(a, i) for i, a in enumerate(A)]
    AI.sort()

    t = 0
    s = 0
    for a, i in AI:
        t += s - BIT_query(i + 1)

        s += 1
        BIT_update(i + 1, 1)

    print(t)

    for i in range(N - 1):
        a = A[i]
        t += (N - a - 1) - a
        print(t)

    return


if __name__ == "__main__":
    main()
