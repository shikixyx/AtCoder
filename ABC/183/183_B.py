import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    x, y, a, b = map(int, input().split())

    ans = ((a - x) * y / (y + b)) + x

    print(ans)

    return


if __name__ == "__main__":
    main()
