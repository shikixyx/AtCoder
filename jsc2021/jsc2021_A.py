import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    X, Y, Z = map(int, input().split())
    ans = 0

    for i in range((10 ** 6) + 100)[::-1]:
        if (i / Z) < (Y / X):
            ans = i
            break

    print(ans)
    return


if __name__ == "__main__":
    main()
