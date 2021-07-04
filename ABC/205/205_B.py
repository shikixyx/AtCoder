import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))

    l = len(set(A))

    if l == N:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
