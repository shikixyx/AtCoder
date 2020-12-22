import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, W = map(int, input().split())

    print(N // W)
    return


if __name__ == "__main__":
    main()
