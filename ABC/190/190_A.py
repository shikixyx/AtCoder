import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B, C = map(int, input().split())

    if A > B:
        print("Takahashi")
    elif B > A:
        print("Aoki")
    elif C == 0:
        print("Aoki")
    else:
        print("Takahashi")

    return


if __name__ == "__main__":
    main()
