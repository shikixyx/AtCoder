import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    print(a * d - b * c)

    return


if __name__ == "__main__":
    main()
