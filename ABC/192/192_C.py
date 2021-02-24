import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())

    for _ in range(K):
        p = list(str(N))
        g1 = int("".join(sorted(p, reverse=True)))
        g2 = int("".join(sorted(p)))
        f = g1 - g2
        N = f

    print(N)

    return


if __name__ == "__main__":
    main()
