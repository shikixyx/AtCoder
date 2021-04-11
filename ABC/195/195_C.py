import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    m = 1
    t = 10 ** 3
    ans = 0
    while t ** m <= N:
        ans += (N - t ** m) + 1
        m += 1

    print(ans)
    return


if __name__ == "__main__":
    main()
