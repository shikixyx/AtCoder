import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B = map(int, input().split())
    T = A + B

    if T >= 15 and B >= 8:
        print(1)
    elif T >= 10 and B >= 3:
        print(2)
    elif T >= 3:
        print(3)
    else:
        print(4)

    return


if __name__ == "__main__":
    main()
