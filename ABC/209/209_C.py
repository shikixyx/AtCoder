import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    C = list(map(int, input().split()))

    C.sort()

    ans = 1
    for i, c in enumerate(C):
        ans *= max(0, c - i)
        ans %= MOD

    print(ans)

    return


if __name__ == "__main__":
    main()
