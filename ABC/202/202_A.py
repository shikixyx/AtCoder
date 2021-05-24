import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    a, b, c = map(int, input().split())
    print(21 - a - b - c)
    return


if __name__ == "__main__":
    main()
