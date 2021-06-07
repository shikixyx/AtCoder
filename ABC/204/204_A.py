import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    x, y = map(int, input().split())

    if x == y:
        print(x)
    else:
        print(3 - x - y)

    return


if __name__ == "__main__":
    main()
