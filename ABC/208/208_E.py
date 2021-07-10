import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())

    keta = len(str(N))
    dp = [
        [
            [[[[0] * 20 for _ in range(20)] for _ in range(60)] for _ in range(60)]
            for _ in range(2)
        ]
        for _ in range(keta + 5)
    ]

    arrN = [-1] + list(str(N))

    for i in range(1, keta + 1):
        # i桁目まで見て
        n_i = int(arrN[i])

        for t in range(10):
            if i == 0 and t == 0:
                continue

    return


if __name__ == "__main__":
    main()
