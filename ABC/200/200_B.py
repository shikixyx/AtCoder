import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())

    for _ in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + "200")

    print(N)

    return


if __name__ == "__main__":
    main()
