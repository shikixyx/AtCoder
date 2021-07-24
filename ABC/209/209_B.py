import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    t = 0
    for i, a in enumerate(A):
        if i % 2 == 1:
            t += a - 1
        else:
            t += a

    if X < t:
        print("No")
    else:
        print("Yes")

    return


if __name__ == "__main__":
    main()
