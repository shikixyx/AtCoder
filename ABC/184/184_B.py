import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, X = map(int, input().split())
    S = list(input())

    for s in S:
        if s == "o":
            X += 1
        else:
            X -= 1
            X = max(0, X)

    print(X)

    return


if __name__ == "__main__":
    main()
