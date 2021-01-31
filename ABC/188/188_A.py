import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    X, Y = map(int, input().split())
    b, s = max(X, Y), min(X, Y)

    if (s + 3) > b:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
