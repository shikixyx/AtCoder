import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B = map(int, input().split())

    if (1 * A) <= B <= (6 * A):
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
