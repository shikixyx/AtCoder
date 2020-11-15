import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    x = int(input())
    if x >= 0:
        print(x)
    else:
        print(0)

    return


if __name__ == "__main__":
    main()
