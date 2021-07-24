import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, A, X, Y = map(int, input().split())
    ans = 0
    ans += X * min(N, A)
    N -= A

    ans += Y * max(0, N)
    print(ans)

    return


if __name__ == "__main__":
    main()
