import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B, C, D = map(int, input().split())

    a = C * D - B

    if a <= 0:
        print(-1)
        return

    print(-(-A // a))

    return


if __name__ == "__main__":
    main()
