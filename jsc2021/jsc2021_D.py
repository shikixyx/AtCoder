import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    MOD = 10 ** 9 + 7
    N, P = map(int, input().split())

    ans = (P - 1) * pow((P - 2), (N - 1), MOD)
    ans %= MOD

    print(ans)
    return


if __name__ == "__main__":
    main()
